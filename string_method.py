txt = "hello, and welcome to my world!"

x= txt.capitalize()
print (x)

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "36 is my age."
x = txt.capitalize()
print (x)


txt = "Hello, And Welcome to my world!"
x = txt.casefold()
print (x)

txt = "banana"
x = txt.center(20)
print (x)

txt = "banana"
x = txt.center(20, "O")
print(x)

txt = "I Love my Wife, Nilima Tasnim Bappi (Nilima)"
x = txt.count("Nilima")
print (x)

txt = "I love my wife, Nilima tasnim bappi, Nilima"
x = txt.count("Nilima", 10 , 30)
print (x)

txt = "My love Nilima"
x = txt.encode()
print (x)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


txt = "Hello, welcome to my world."
x = txt.endswith(".")
print (x)

txt = "Hello, welcome to Her world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(5)
print(x)

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


txt = "Hello, welcome to my world."
x = txt.find("welcome")
print (x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))


txt = "Company12"
x = txt.isalnum()
print (x)

txt = "Company 12"
x = txt.isalnum()
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company10"
x = txt.isalpha()
print(x)

txt = "Company123"
x = txt.isascii()
print (x)

txt = "For only {price: .2f} dollers!"
print(txt.format(price = 49))

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print (x)

txt = "1234"
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

txt = "50700"
x = txt.isdigit()
print(x)

a = "0e030" #unicode for 0
b = "g00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())


txt = "Nilima"
x = txt.isidentifier()
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

txt = "hello world!"
x = txt.islower()
print(x)

txt = "Hello world!"
x = txt.islower()
print(x)

txt = "435345"
x = txt.isnumeric()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

txt = "Hello! Are you #1?"
x = txt.isprintable()
print (x)

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

txt = "   "
x = txt.isspace()
print(x)

txt = "   s   "
x = txt.isspace()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())

myTouple = ("Jone", "Peter", "Vicky")
x = "#" .join(myTouple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)


txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")