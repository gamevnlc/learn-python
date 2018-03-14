# Conditions
x = 2
print(x == 2)

# Boolean operatos

a = 1
b = 2
if a == 1 and b == 2:
    print('hei')

if a == 1 or a == 2:
    print('ha')

# The "in" operators

if a in [1, 2]:
    print('Hiii')

x = 3

if x == 2:
    print('Hii')
else:
    print('Heee')

# The 'is' operators
q = [1, 2, 3]
w = [1, 2, 3]
print(q == w)
print(q is w)

# The 'not' operators
print(not False)
print((not False) == (False))

# change this code
number = 16
second_number = False
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
