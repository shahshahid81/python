import asyncio
import time


async def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")

    # Simulate a non-blocking I/O operation.
    #
    # Unlike time.sleep(), asyncio.sleep() suspends only this coroutine.
    # When execution reaches this await, the coroutine yields control back
    # to the event loop, which can continue running other scheduled Tasks.
    await asyncio.sleep(param)

    print(f"Done with {param}")
    return f"Result of {param}"


# Mental model:
#   Coroutine function (async def)
#       ↓ called
#   Coroutine object
#       ↓ create_task()
#   Task (a Future managed by the event loop)
#       ↓
#   Event loop runs scheduled Tasks concurrently
#       ↓
#   Each Task eventually stores its result
#
# Concurrency comes from scheduling multiple Tasks before awaiting them.
async def main() -> list[str]:
    # create_task() immediately schedules both coroutines on the event loop.
    # They become eligible to run concurrently as soon as the event loop
    # gets control.
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    # Await task2 first.
    #
    # Important distinction:
    # Awaiting a Task means "wait until its result is available."
    # It does NOT mean "run only this Task."
    #
    # While main() is suspended here, the event loop continues running every
    # ready Task, including task1. Since task1 only waits for 1 second, it
    # completes before task2.
    result2 = await task2

    # task1 finished while main() was waiting for task2.
    # Because the Task has already completed and stored its result,
    # this await returns immediately without suspending again.
    result1 = await task1

    return [result1, result2]


if __name__ == "__main__":
    t1 = time.perf_counter()

    # asyncio.run():
    # 1. Creates an event loop.
    # 2. Schedules main() to run.
    # 3. Runs the loop until main() completes.
    # 4. Cleans up the event loop.
    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()

    # Expected output order:
    # - Both "Do something with ..." messages usually appear first because
    #   both Tasks begin before either sleep completes.
    # - "Done with 1" appears before "Done with 2" because its timer expires
    #   first, even though task2 is awaited first.
    #
    # Expected runtime:
    # The 1-second and 2-second waits overlap because both Tasks were
    # scheduled together. The total runtime is therefore approximately
    # 2 seconds, which is the longest individual wait.
    print(f"Finished in {t2 - t1:0.2f} seconds")