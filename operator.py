# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)     # Addition
print("a - b =", a - b)     # Subtraction
print("a * b =", a * b)     # Multiplication
print("a / b =", a / b)     # Division (float)
print("a // b =", a // b)   # Floor Division
print("a % b =", a % b)     # Modulus
print("a ** b =", a ** b)   # Exponentiation
print()

# Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)    # Equal
print("a != b:", a != b)    # Not equal
print("a > b:", a > b)      # Greater than
print("a < b:", a < b)      # Less than
print("a >= b:", a >= b)    # Greater than or equal
print("a <= b:", a <= b)    # Less than or equal
print()

# Logical Operators
x = True
y = False
print("Logical Operators:")
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT
print()

# Bitwise Operators
print("Bitwise Operators:")
print("a & b =", a & b)     # Bitwise AND
print("a | b =", a | b)     # Bitwise OR
print("a ^ b =", a ^ b)     # Bitwise XOR
print("~a =", ~a)           # Bitwise NOT
print("a << 1 =", a << 1)   # Bitwise Left Shift
print("a >> 1 =", a >> 1)   # Bitwise Right Shift
print()

# Assignment Operators
c = 5
print("Assignment Operators:")
c += 2
print("c += 2 =>", c)
c -= 1
print("c -= 1 =>", c)
c *= 3
print("c *= 3 =>", c)
c /= 2
print("c /= 2 =>", c)
c %= 3
print("c %= 3 =>", c)
c **= 2
print("c **= 2 =>", c)
c //= 2
print("c //= 2 =>", c)
print()

# Membership Operators
list1 = [1, 2, 3, 4]
print("Membership Operators:")
print("2 in list1:", 2 in list1)
print("5 not in list1:", 5 not in list1)
print()

# Identity Operators
m = [1, 2]
n = m
p = [1, 2]
print("Identity Operators:")
print("m is n:", m is n)
print("m is p:", m is p)
print("m is not p:", m is not p)