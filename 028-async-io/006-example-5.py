import asyncio
import time


async def fetch_data(param: int) -> str:
    print(f"Task {param} started")

    # Simulate a blocking operation.
    #
    # WARNING:
    # time.sleep() blocks the current thread. Since the asyncio event loop
    # runs on this thread, the entire event loop is blocked while sleeping.
    #
    # Mental model:
    # asyncio uses cooperative multitasking. Coroutines are expected to
    # periodically reach an "await", which voluntarily gives control back to
    # the event loop. time.sleep() never yields, so the event loop cannot run
    # any other Tasks until the sleep finishes.
    #
    # In production asyncio code, use:
    #     await asyncio.sleep(param)
    time.sleep(param)

    print(f"Task {param} finished")
    return f"Result of {param}"


# Mental model:
#   Coroutine function (async def)
#       ↓ called
#   Coroutine object
#       ↓ create_task()
#   Task (a specialized Future managed by the event loop)
#       ↓ scheduled
#   Event loop executes ready Tasks
#
# Scheduling multiple Tasks normally enables concurrency, but only if those
# Tasks cooperate by yielding control with "await".
async def main() -> list[str]:
    print("Scheduling task1...")
    task1 = asyncio.create_task(fetch_data(1))

    print("Scheduling task2...")
    task2 = asyncio.create_task(fetch_data(2))

    print("Both Tasks have been scheduled.")

    # Await task1.
    #
    # When main() reaches this await, it suspends and returns control to the
    # event loop. The event loop then begins executing scheduled Tasks.
    #
    # task1 starts first and immediately calls time.sleep(1), blocking the
    # entire event loop. While the event loop is blocked, task2 cannot start
    # and main() cannot resume.
    #
    # After task1 finishes, its Task is marked complete. This makes main()
    # ready to continue because "await task1" now has a result.
    #
    # However, "ready" does NOT mean "running immediately". The event loop
    # maintains a queue of ready Tasks and callbacks. Since task2 was already
    # scheduled, the event loop gives it a chance to run before resuming
    # main().
    #
    # task2 immediately calls time.sleep(2), blocking the event loop again.
    # As a result, main() cannot resume until task2 has also finished.
    result1 = await task1
    print("Task 1 fully completed")

    # task2 has already completed while main() was waiting.
    # Completed Tasks store their result, so awaiting them returns
    # immediately without suspending.
    result2 = await task2
    print("Task 2 fully completed")

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

    # Expected output:
    #   Scheduling task1...
    #   Scheduling task2...
    #   Both Tasks have been scheduled.
    #   Task 1 started
    #   Task 1 finished
    #   Task 2 started
    #   Task 2 finished
    #   Task 1 fully completed
    #   Task 2 fully completed
    #
    # Although both Tasks were scheduled immediately, the blocking
    # time.sleep() calls prevent the event loop from switching between them.
    # The sleeps therefore occur one after another instead of overlapping.
    #
    # Expected runtime:
    # Approximately 3 seconds (1 + 2), because the blocking operations execute
    # sequentially.
    print(f"Finished in {t2 - t1:0.2f} seconds")