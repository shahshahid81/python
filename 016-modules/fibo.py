def fib(n):
    """Write Fibonnaci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()


def fib2(n):
    """Return the fibonnaci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# This block is executed when python fibo.py 10(arg) is called
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
