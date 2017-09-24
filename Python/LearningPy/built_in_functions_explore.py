"""
bin(x)
Convert an integer number to a binary string.
The result is a valid Python expression.
If x is not a Python int object, it has to define an __index__() method that returns an integer.

"""


t = bin(15)
print("t = ",t)
ascii_char = chr(97)
print("ascii_char = ",ascii_char)
x = hex(255)
print("x = ",x)

type_x = id(x)
print("type_x = ",type_x)

power_of = pow(3,5)
print("power_of 3^5 = ",power_of)

print(range(0,-10,-1))


