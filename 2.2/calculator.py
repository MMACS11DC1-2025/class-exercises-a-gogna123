"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

#Calculator Assignment
#Aaryan Gogna
#September 22, 2025
#I copy/pasted from Programiz

print("Hello, I'm a calculator!")

print("Please enter your first number.")
first_number = float(input())

print('Please enter the operation you want to use("+" for addition, "-" for subtraction, "*" for multiplication, and "/" for division.')
operation = input()

print("Please enter your second number.")
second_number = float(input())

if operation == "+":
    print(int(first_number + second_number))

elif operation == "-":
    print(int(first_number - second_number))
    
elif operation == "*":
    print(int(first_number * second_number))

elif operation == "/":
    print(int(first_number / second_number))