def fib(n):  # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)

print(fib)
f = fib
f(100)
# function with no return statement return None
print(f(100))


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


f100 = fib2(100)  # call it
print(f100)  # write the result


# default parameters
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


# ask_ok("Do you really want to quit?")
# ask_ok("OK to overwrite the file?", 2)
# ask_ok("OK to overwrite the file?", 2, "Come on, only yes or no!")

# Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
# For example, the following function accumulates the arguments passed to it on subsequent calls


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))


def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print()
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM")  # 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)  # 2 keyword arguments
parrot("a million", "bereft of life", "jump")  # 3 positional arguments
parrot("a thousand", state="pushing up the daisies")  # 1 positional, 1 keyword

# Invalid method calls
# parrot()                     # required argument voltage missing

# non-keyword argument after a keyword argument, Positional arguments must come before keyword arguments.
# Python sees:
# First argument: voltage=5.0 → OK, goes to voltage
# Second argument: 'dead' → Problem: Where does this go?
# Python doesn't allow mixing keyword arguments first, then positional, because:
# It would complicate argument resolution.
# It could create ambiguous or conflicting assignments.
# parrot(voltage=5.0, 'dead')

# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# *param must come before **param
def cheeseshop(kind, *arguments, **keywords):
    print()
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Limburger",
    "It's very runny, sir.",  # goes to arguments in tuple
    "It's really very, VERY runny, sir.",  # goes to arguments in tuple
    shopkeeper="Michael Palin",  # goes to keywords in dictionary
    client="John Cleese",  # goes to keywords in dictionary
    sketch="Cheese Shop Sketch",  # goes to keywords in dictionary
)


# parameters before / are positional only, meaning we cannot call f with pos1= or pos2=
# parameters after * are keyword only, meaning we cannot call them as f('1','2'), we need to call as f(kwd1='1', kwd2='22')
# parameters in between / and * can be called in both ways
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# can be both positional and keyword
standard_arg(1)
standard_arg(arg=2)

# can be both positional only
pos_only_arg(3)
# pos_only_arg(arg=4)

# can be both keyword only
kwd_only_arg(arg=5)
# kwd_only_arg(6)

# valid
combined_example(1, 2, kwd_only=3)

# invalid
# pos_only cannot be called using keyword
# combined_example(2, pos_only=1,kwd_only=3)
# kwd_only cannot be called as positional
# combined_example(1,2,3)


def foo(name, **kwds):
    return "name" in kwds


# since we can accept name as keyword as well and send it in dictionary, below call is invalid
# print(foo(1, **{'name': 2}))


# Here it is valid since name is positional only
def foo(name, /, **kwds):
    return "name" in kwds


print(foo(1, **{"name": 2}))

print(list(range(3, 6)))  # normal call with separate arguments

args = [3, 6]
# *args unpacks the list, like spread operator
print(list(range(*args)))  # call with arguments unpacked from a list


def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.", end=" ")
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# ** unpacks the dictionary, like spread operator
parrot(**d)


def make_incrementor(n):
    # lambda keyboard is used to create a lambda, only single expression allowed
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# sort by name
pairs.sort(key=lambda pair: pair[1])
print(pairs)