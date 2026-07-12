import asyncio
import time


async def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")

    # Simulate a non-blocking I/O operation.
    #
    # Unlike time.sleep(), asyncio.sleep() does NOT block the current thread.
    # When execution reaches this await, the coroutine suspends itself and
    # returns control to the event loop. The event loop can then run other
    # scheduled Tasks until this timer expires.
    await asyncio.sleep(param)

    print(f"Done with {param}")
    return f"Result of {param}"


# Mental model:
#   Coroutine function (async def)
#       ↓ called
#   Coroutine object (describes work that has not started)
#       ↓ create_task()
#   Task (a Future managed by the event loop)
#       ↓ scheduled for execution
#   Event loop decides when each Task runs
#       ↓
#   Task eventually completes and stores its result
#
# A Task is a specialized Future that executes a coroutine and provides
# access to its eventual result.
async def main() -> list[str]:
    # Calling create_task() does two things:
    #   1. Wraps the coroutine in a Task.
    #   2. Immediately schedules that Task on the event loop.
    #
    # Scheduling is NOT the same as executing. The Tasks are now eligible to
    # run whenever the event loop gets control.
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    # Await task1.
    #
    # Mental model:
    # main() pauses here until task1 finishes. While main() is suspended,
    # the event loop continues running other ready Tasks. When task1 reaches
    # asyncio.sleep(), it also suspends, allowing task2 to execute.
    result1 = await task1

    # task2 has been running concurrently ever since it was scheduled.
    # If it has already completed, this await returns immediately.
    # Otherwise, main() suspends again until task2 finishes.
    result2 = await task2

    return [result1, result2]


if __name__ == "__main__":
    t1 = time.perf_counter()

    # asyncio.run():
    # 1. Creates an event loop.
    # 2. Schedules main() on that loop.
    # 3. Runs the loop until main() completes.
    # 4. Cleans up the event loop.
    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()

    # Expected output order:
    # - Both "Do something with ..." messages usually appear first because both
    #   Tasks start before either sleep completes.
    # - "Done with 1" appears before "Done with 2" because its 1-second timer
    #   expires before the 2-second timer.
    #
    # Expected runtime:
    # Both Tasks spend most of their time waiting asynchronously. Since those
    # waits overlap, the total runtime is approximately the longest individual
    # wait (about 2 seconds), not the sum of both waits (3 seconds).
    print(f"Finished in {t2 - t1:0.2f} seconds")