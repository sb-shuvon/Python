def greeting(name):
    print("Hello, " + name)

import mymodule

mymodule.greeting("Jonathan")

import mymodule as mx

mx.greeting("Rahim")

from mymodule import greeting

greeting("Karim")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

print(mymodule.person1["age"])
