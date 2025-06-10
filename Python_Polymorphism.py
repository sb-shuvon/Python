print(len("hello"))
print(len([10, 20, 30]))
print(len({"name": "Alice", "age": 25}))

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

def make_sound(animal):
    animal.sound()

c = Cat()
d = Dog()

make_sound(c)
make_sound(d)

class Animal:
    def speak(self):
        print("Some sound")

class Bird(Animal):
    def speak(self):
        print("Chirp")

class Lion(Animal):
    def speak(self):
        print("Roar")

animals = [Animal(), Bird(), Lion()]

for a in animals:
    a.speak()
