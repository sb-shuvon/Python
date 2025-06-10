a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200
if b > a and a < 100:
    print("Both conditions are True")

a = 33
b = 200
if b > a or a > 100:
    print("At least one of the conditions is True")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
