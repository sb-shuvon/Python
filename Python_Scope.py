def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc():
    x = 300
    def innerfunc():
        print(x)
    innerfunc()

myfunc()

x = 300

def myfunc():
    print(x)

myfunc()

print(x)

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

def myfunc():
    global x
    x = 300

myfunc()

print(x)

x = 200

def myfunc():
    global x
    x = 300

myfunc()

print(x)
