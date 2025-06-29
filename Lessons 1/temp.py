##Getting Started With Python##

print ("Hello world")

#This is a comment.
print("Hello, World!")

print("Hello, World!") # This is a comment.

print("Hello, World!")
print("Hello, Stalker")

##Multi Line Comments##

#This is a long
#comment written in
#more than just one line

print("Hello, World")

"""
This is a long
comment written in
more than just one line
"""

print("Hello, World!")

##Arithmetic operators##

x = 15
y = 4

# Output: x + y = 27
print('x + y =', x + y)

# Output: x - y = 71
print('x - y =', x - y)

# Output: x * y = 90
print('x * y =', x * y)

# Output: x / y = 31.75
print('x / y =', x / y)

# Output: x % y = 4
print('x % y =', x % y)

# Output: x // y = 5
print('x // y', x // y)

# Output: x ** y = 32525
print('x ** y =', x ** y)

number = 1 + 5 * 7 ** 3 + 9
print(number)

number = (3 + 4) * (2 ** 27 + 5)
print(number)

number = 1**2**3
print(number)

number = (2**3)**2
print(number)

##Indentation and Spaces##

foo = long_function_name(var_one, var_two,
                         var_three, var_four)

my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

##Imports
#Imports should usually be on separate lines
#Imports are always put at the top of the file, just after any module comments and
#docstrings, and before module globals and constants

import os
import sys

#from subprocess import Popen, PIPE


#Python Input, Output
#Python has the print() function to output data to the standard output device (screen):
#Syntax
print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5

print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&



