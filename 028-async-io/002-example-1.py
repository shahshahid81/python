import time


def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")

    # Simulate a blocking I/O operation.
    #
    # Mental model:
    # time.sleep() pauses the current thread. While it is sleeping, this
    # thread cannot execute any other Python code. The function does not
    # return until the sleep has finished.
    time.sleep(param)

    print(f"Done with {param}")
    return f"Result of {param}"


# Mental model:
#   Synchronous execution means one operation runs to completion before the
#   next one begins. There is no overlap between these function calls.
def main() -> list[str]:
    # fetch_data(1) runs from start to finish before the next line executes.
    result1 = fetch_data(1)
    print("Fetch 1 fully completed")

    # This call cannot begin until the previous call has returned.
    result2 = fetch_data(2)
    print("Fetch 2 fully completed")

    return [result1, result2]


if __name__ == "__main__":
    # perf_counter() measures elapsed (wall-clock) time with high precision,
    # making it suitable for timing how long a program takes to run.
    t1 = time.perf_counter()

    results = main()
    print(results)

    t2 = time.perf_counter()

    # Expected runtime:
    # fetch_data(1) blocks for about 1 second.
    # fetch_data(2) then blocks for about 2 seconds.
    # Because the calls happen sequentially, the total runtime is
    # approximately 1 + 2 = 3 seconds (plus a small amount of overhead).
    print(f"Finished in {t2 - t1:0.2f} seconds")