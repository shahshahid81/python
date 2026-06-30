import decimal
from decimal import Decimal

print(decimal.getcontext())

ctx = decimal.getcontext()
ctx.prec = 5

print(decimal.getcontext())
ctx.prec = 6

print(decimal.getcontext())

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(decimal.getcontext())

d1 = Decimal("123.456789")
print(repr(d1))
print(d1 + Decimal(1))

print(round(Decimal("100.445"), 2))

ctx = decimal.getcontext()
ctx.prec = 28
ctx.rounding = decimal.ROUND_HALF_EVEN
print(round(Decimal("100.445"), 2))

print("Before: ", decimal.getcontext())

# we have a copy of the context in the block that we can change without modifying the original one, same as file getting closed automatically after block end.
with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print("Local context:", ctx)
    print("Inside context:", round(Decimal("123.445"), 2))

print("After contxt:", round(Decimal("123.445"), 2))
