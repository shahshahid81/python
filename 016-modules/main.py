from fibo import fib as fibonacci
import fibo as fb
from fibo import *
from fibo import fib, fib2
import fibo

# Using methods by module name
fibo.fib(1000)
print(fibo.fib2(1000))
print(fibo.__name__)

# assigning module function to variable
fib = fibo.fib
fib(1000)

fib(1000)

fb.fib(1000)

fibonacci(1000)
