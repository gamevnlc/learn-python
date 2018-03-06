x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

print("Hello World")

print(x)

myfloat = 1.2
print(myfloat)

myfloat = float(1.2)
print(myfloat)

mystring = 'hi'
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloWorld = hello + " " + world
print(helloWorld)

a, b = 3, 4
print(a, b)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist)

for x in mylist:
    print(x)

number = 1 + 2 + 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
print(squared)


helloworld = "je" * 10
print(helloworld)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
print(all_numbers * 2)

name = "IK"
ki = 12
print("LP %s %d" % (name, ki))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%f"
test = format_string
print(format_string % data)

astring = "Hello world"
print(astring[3:7])
print(astring.upper())
print(astring.lower())
print(astring.startswith("1 "))
