import asyncio
import time


async def fetch_data(param: int) -> str:
    # Simulate a non-blocking I/O operation.
    #
    # When execution reaches this await, the coroutine suspends itself and
    # returns control to the event loop. The event loop can run other ready
    # Tasks while this coroutine waits.
    await asyncio.sleep(param)

    return f"Result of {param}"


async def main():
    # ------------------------------------------------------------------
    # Example 1: create_task() + individual await
    # ------------------------------------------------------------------

    # create_task() wraps each coroutine in a Task and immediately schedules
    # it on the event loop.
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    # Awaiting task1 suspends main(), not the event loop.
    # While main() is suspended, both Tasks continue making progress.
    result1 = await task1

    # task2 has been running concurrently since it was scheduled.
    # If it has already completed, this await returns immediately.
    result2 = await task2

    print(f"Task 1 and 2 awaited results: {[result1, result2]}")

    # ------------------------------------------------------------------
    # Example 2: asyncio.gather() with coroutine objects
    # ------------------------------------------------------------------

    # Calling an async function creates coroutine objects only.
    # They have not started executing yet.
    coroutines = [fetch_data(i) for i in range(1, 3)]

    # gather() accepts awaitables.
    #
    # If coroutine objects are provided, gather() automatically wraps them
    # in Tasks, schedules them on the event loop, and waits until they have
    # all completed.
    #
    # return_exceptions=True causes exceptions to be returned in the result
    # list instead of immediately propagating.
    results = await asyncio.gather(*coroutines, return_exceptions=True)

    print(f"Coroutine Results: {results}")

    # ------------------------------------------------------------------
    # Example 3: asyncio.gather() with existing Tasks
    # ------------------------------------------------------------------

    # These Tasks are scheduled immediately.
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]

    # Unlike the previous example, gather() does not need to schedule these
    # Tasks because they are already running. It simply waits for all of
    # them to finish and returns their results in the same order they were
    # passed to gather(), regardless of completion order.
    results = await asyncio.gather(*tasks, return_exceptions=True)

    print(f"Task Results: {results}")

    # ------------------------------------------------------------------
    # Example 4: TaskGroup (Python 3.11+)
    # ------------------------------------------------------------------

    # TaskGroup provides structured concurrency.
    #
    # Tasks created inside the group are automatically awaited when leaving
    # the "async with" block.
    #
    # If one Task raises an exception, the remaining Tasks are cancelled
    # before the exception is propagated, making TaskGroup safer than
    # manually managing many independent Tasks.
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch_data(i)) for i in range(1, 3)]

    # Exiting the TaskGroup guarantees every Task has either completed or
    # been cancelled, so calling result() is now safe.
    print(f"Task Group Results: {[task.result() for task in tasks]}")

    return "Main Coroutine Done"


if __name__ == "__main__":
    t1 = time.perf_counter()

    # asyncio.run():
    # 1. Creates an event loop.
    # 2. Schedules main().
    # 3. Runs the loop until main() completes.
    # 4. Cleans up the event loop.
    result = asyncio.run(main())
    print(result)

    t2 = time.perf_counter()

    # Mental model:
    #
    # Each section schedules two operations that wait for 1 and 2 seconds.
    # Since the waits overlap, each section takes about 2 seconds instead of
    # 3 seconds.
    #
    # The four sections execute one after another, so the total runtime is
    # approximately:
    #
    #     2 + 2 + 2 + 2 = 8 seconds
    #
    # (plus a small amount of overhead).
    print(f"Finished in {t2 - t1:0.2f} seconds")