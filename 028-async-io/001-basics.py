import asyncio
import time


def sync_function(test_param: str) -> str:
    print("This is a synchronous function")

    # Blocks the current thread for 0.1 seconds.
    # Mental model:
    # While time.sleep() is running, Python cannot execute anything else on
    # this thread. If this function were called directly from an asyncio
    # coroutine, it would pause the entire event loop during the sleep.
    time.sleep(0.1)

    return f"Sync Result: {test_param}"


async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function")

    # asyncio.sleep() does NOT block the thread.
    # Instead, it tells the event loop:
    # "Resume this coroutine after 0.1 seconds, and run other ready tasks
    # in the meantime."
    await asyncio.sleep(0.1)

    return f"Async Result: {test_param}"


# Mental model:
#   Coroutine function (async def)
#       ↓ called
#   Coroutine object (describes work to be done)
#       ↓ awaited or scheduled
#   Task (managed by the event loop)
#       ↓ eventually finishes
#   Future (holds the eventual result or exception)
#
# In asyncio, Task is a specialized Future that executes a coroutine.


# Calling a coroutine function does NOT immediately execute its body.
# It returns a coroutine object, which is simply an awaitable object
# representing work that has not started yet.
#
# Top-level coroutine execution usually begins with asyncio.run(),
# which creates an event loop, runs the coroutine to completion,
# and then cleans up the loop.
async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)

    # The currently running event loop coordinates all scheduled asyncio work.
    loop = asyncio.get_running_loop()

    # A Future represents a value that will become available later.
    # Unlike a Task, a plain Future does not perform work by itself.
    # It is simply a container for a result that some other code will provide.
    future = loop.create_future()
    print(f"Empty Future: {future}")

    # Complete the Future manually.
    future.set_result("Future Result: Test")

    # await works with awaitable objects (such as coroutine objects,
    # Tasks, and Futures).
    #
    # Mental model:
    # If the awaited object is already complete, execution continues
    # immediately. Otherwise, the current coroutine pauses here,
    # gives control back to the event loop, and resumes later when the
    # awaited object completes.
    future_result = await future
    print(future_result)

    # Calling an async function creates a coroutine object.
    # No code inside async_function() has executed yet.
    coroutine_object = async_function("Test")
    print(coroutine_object)

    # Awaiting the coroutine starts executing it.
    # When execution reaches "await asyncio.sleep(...)", this coroutine
    # pauses, the event loop is free to run other ready tasks, and this
    # coroutine resumes after the sleep completes.
    coroutine_result = await coroutine_object
    print(coroutine_result)

    # Schedule the coroutine as a Task.
    #
    # Important distinction:
    # - Creating a coroutine object does NOT schedule it.
    # - Creating a Task immediately schedules it on the event loop.
    task = asyncio.create_task(async_function("Test"))
    print(task)

    # Although the Task has already been scheduled, we immediately await it.
    # Because nothing else is running concurrently in this example, the overall
    # behavior remains effectively sequential.
    task_result = await task
    print(task_result)


if __name__ == "__main__":
    # asyncio.run():
    # 1. Creates a new event loop.
    # 2. Schedules main() to run on that loop.
    # 3. Runs the loop until main() completes.
    # 4. Cleans up the event loop.
    asyncio.run(main())