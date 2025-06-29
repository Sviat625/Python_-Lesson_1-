#1
#Write a program that will ask the user the following questions:
#
#    "What is your name?"
#
#    "How old are you?"
#
#    "Where do you live?"
#
#After receiving the answers, the program should display the following messages:
#
#    "Hello, (answer to the name question) !"
#
#    "Your age is (answer to the age question) ."
#
#    "You live in (answer to the city question) ."


name = input("What is your name?\n")
age = input("How old are you?\n")
city = input("Where do you live?\n")

print("---------------")

print("Hello",  name, "!")
print("Your age is",  age, ".")
print("You live in",  city, ".")

#2
#Write a program that will calculate the sum, difference, product, exponentiation, etc., of two numbers a and b that the program reads from the console (data entered by the user) and will output the appropriate results:
#    "a + b = " ...
#   "a - b = " ...
#    "a * b = " ...
#    "a / b = " ...
#    "a**b = " ...
#    "a//b = " ...
#    "a%b = " ...

a = float(input("Enter the first number (a):\n"))
b = float(input("Enter the second number (b):\n"))

print(f"a + b = {a + b} ")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a**b = {a**b}")


