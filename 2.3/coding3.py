"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""

#McDonald's Program
#Aaryan Gogna
#Sep 23, 2025

print("Would you like a burger for $5?")

response_1 = input().lower()

print("Would you like fries for $3? ")

response_2 = input().lower()

if response_1 == "yes" and response_2 == "yes":
    print("Your total is $9.12.")
    
elif response_1 == "yes" and response_2 == "no":
    print("Your total is $5.70.")
    
elif response_1 == "no" and response_2 == "yes":
    print("Your total is $3.42.")
    
elif response_1 == "no" and response_2 == "no":
    print("Have a nice day, your total is $0.")
    
else:
    print("Sorry, I don't understand what you said.")