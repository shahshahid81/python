# all data types are object, no primitive in python
print(1)
print(-10)
print(1.0)
print(True)
print(False)
print(0.1)
# 0.1 is not exactly 0.1 since float is represented using IE754 floating point
# Scientific notation:
# a×10^n
# Example: 4500 = 4.5 × 10³
# IEEE 754 uses binary scientific notation:
# 1.f*2&^e (f = fraction, e = exponent same as n in scientific)
# Example: 20 = 10100₂ = 1.0100 × 2⁴
# Exponent = how many places the point moves during normalization.
print(format(0.1, ".25f"))
print(format(0.125, ".25f"))
print(1 + 1 + 1 == 3)
print(0.125 + 0.125 + 0.125 == 0.375)
# false since not exactly equal, check above comment
print(0.1 + 0.1 + 0.1 == 0.3) 
print(format(0.1 + 0.1 + 0.1, ".25"))
print(format(0.3, ".25"))
print(abs((0.1 + 0.1 + 0.1) - 0.3) < 0.001)
