import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")

    # This is intentionally a blocking function.
    #
    # Normally, calling time.sleep() from the event loop thread would freeze
    # the entire event loop. In this example, however, fetch_data() will run
    # inside worker threads or worker processes, so blocking here does NOT
    # block the event loop.
    time.sleep(param)

    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    # Mental model:
    #
    # asyncio.to_thread() is an async function. Calling it creates a coroutine
    # object that represents "run this blocking function in a worker thread."
    #
    # Wrapping that coroutine in create_task() schedules it immediately on the
    # event loop. When the Task runs, the blocking function is submitted to the
    # thread pool, allowing the event loop to continue running other Tasks.
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))

    # Awaiting task1 suspends main(), but the event loop remains free to
    # monitor both worker threads. Since both functions were submitted almost
    # together, their sleeps overlap.
    result1 = await task1
    print("Thread 1 fully completed")

    # task2 has been running in parallel in another worker thread.
    # If it has already finished, this await returns immediately.
    result2 = await task2
    print("Thread 2 fully completed")

    loop = asyncio.get_running_loop()

    # ProcessPoolExecutor runs synchronous functions in separate Python
    # processes instead of threads.
    #
    # Unlike asyncio.to_thread(), run_in_executor() directly returns an
    # asyncio.Future. A Future represents a result that will become available
    # later, so it can be awaited without wrapping it in create_task().
    with ProcessPoolExecutor() as executor:
        future1 = loop.run_in_executor(executor, fetch_data, 1)
        future2 = loop.run_in_executor(executor, fetch_data, 2)

        # While waiting for future1, both worker processes continue executing.
        result1 = await future1
        print("Process 1 fully completed")

        # future2 has likely already completed because it started at nearly the
        # same time as future1.
        result2 = await future2
        print("Process 2 fully completed")

        return [result1, result2]


if __name__ == "__main__":
    t1 = time.perf_counter()

    # asyncio.run():
    # 1. Creates an event loop.
    # 2. Schedules main().
    # 3. Runs the loop until main() completes.
    # 4. Cleans up the event loop.
    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()

    # Expected runtime:
    #
    # Thread demonstration:
    #   fetch_data(1) and fetch_data(2) run concurrently in worker threads,
    #   so this section takes about 2 seconds.
    #
    # Process demonstration:
    #   The same work then runs concurrently in worker processes, taking
    #   another ~2 seconds.
    #
    # Since these demonstrations happen one after the other, the total runtime
    # is approximately 4 seconds (plus a small amount of overhead).
    print(f"Finished in {t2 - t1:0.2f} seconds")