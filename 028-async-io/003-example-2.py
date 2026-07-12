import asyncio
import time


async def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")

    # Simulate a non-blocking I/O operation.
    #
    # Unlike time.sleep(), asyncio.sleep() does not block the current thread.
    # When execution reaches this await, the coroutine suspends itself and
    # returns control to the event loop. The event loop can run other ready
    # tasks while this coroutine waits for the timer to expire.
    await asyncio.sleep(param)

    print(f"Done with {param}")
    return f"Result of {param}"


# Mental model:
#   Coroutine function (async def)
#       ↓ called
#   Coroutine object (describes work that has not started yet)
#       ↓ awaited
#   Event loop executes the coroutine
#       ↓ coroutine reaches an await
#   Coroutine suspends and yields control back to the event loop
#       ↓ event loop resumes it later
#
# No Tasks are created in this example, so the event loop has only one active
# coroutine to execute at a time.
async def main() -> list[str]:
    # Calling an async function creates coroutine objects.
    # At this point, neither coroutine has started executing.
    coroutine1 = fetch_data(1)
    coroutine2 = fetch_data(2)

    # Awaiting coroutine1 starts (or resumes) its execution.
    # When it reaches asyncio.sleep(), main() also pauses until coroutine1
    # eventually finishes. Since coroutine2 has not been awaited or scheduled,
    # it has not started yet.
    result1 = await coroutine1
    print("Fetch 1 fully completed")

    # coroutine2 only begins executing now, after coroutine1 has completely
    # finished. Although this program uses asyncio, these operations still run
    # sequentially because there is no concurrent scheduling.
    result2 = await coroutine2
    print("Fetch 2 fully completed")

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

    # Expected runtime:
    # coroutine1 waits about 1 second, then coroutine2 waits about 2 seconds.
    # Because the second coroutine does not begin until the first has finished,
    # the waits do not overlap. The total runtime is therefore approximately
    # 1 + 2 = 3 seconds (plus a small amount of overhead).
    print(f"Finished in {t2 - t1:0.2f} seconds")