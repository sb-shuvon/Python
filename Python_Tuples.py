thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print("banana" in thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
