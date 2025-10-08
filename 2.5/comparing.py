"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# Data Analysis Assignment
# Aaryan Gogna
# September 30, 2025

# Algorithm:
# 1. Read the file
# 2. Ask for two names
# 3. Compare all 8 answers, if both people have the same answer for one topic, add +1 for the same results.
# 4. Show 2 interesting observations at the end(It will show whos digit is higher,
#    and if how many similarities they have together out of 8. Lastly, based on )

# Testing: 
# 1. Inputting "Ethan Wong" as the first name, and "Leland Lei" as the second name:
#    Expected outputs: There should only be 1 similarity. Leland's digit is higher than Ethan's.
#    Testing Results: They only had 1 similarity, and Leland's digit was higher than Ethan's.

# This opens the file and reads through it, then discards it.
file = open("2.4/responses.csv")
lines = file.readlines()

# Makes every row into a list by using split. 
rows = []
for line in lines[1:]:
    line = line.strip()
    data = line.split(",")
    if rows == []:
        rows = [data]
    else:
        rows = rows + [data]

# Prints all classmates names starting from the second row.
print("Classmates:")
for r in rows:
    print(r[1])

# Asks user input first and second name to compare.
name1 = input("Enter first name: ").strip()
name2 = input("Enter second name: ").strip()

# Both people are blank since we dont know who they are.
person1 = ""
person2 = ""

# Reads through every file and checks if both names are there.
for r in rows:
    if r[1].lower() == name1.lower():
        person1 = r
    if r[1].lower() == name2.lower():
        person2 = r

# If both names are in the data, initilaize the similarites to 0. 
if person1 == "" and person2 == "":
    print("Both not found")
elif person1 == "":
    print("First not found")
elif person2 == "":
    print("Second not found")
else:
    same = 0
    print("\nComparing answers...\n")

    # 1) Checks the favourite digit after the first comma for both names and compares them.
    d1 = int(person1[2])
    d2 = int(person2[2])
    print("Favourite Digit: " + str(d1) + " vs " + str(d2))
    if d1 == d2:
        print("Result: Same digit")
        same = same + 1
    else:
        print("Result: Different digits\n")

    # 2) Checks the favourite pet after the second comma for both names and compares them.
    print("Favourite Pet: " + person1[3] + " vs " + person2[3])
    if person1[3].lower() == person2[3].lower():
        print("Result: Same")
        same = same + 1
    else:
        print("Result: Different\n")

    # 3) Checks the favourite subject after the third comma for both names and compares them.
    print("Favourite Subject: " + person1[4] + " vs " + person2[4])
    if person1[4].lower() == person2[4].lower():
        print("Result: Same")
        same = same + 1
    else:
        print("Result: Different\n")

    # 4) Checks the favourite sport to play after the fourth comma for both names and compares them.
    print("Favourite Sport to Watch: " + person1[5] + " vs " + person2[5])
    if person1[5].lower() == person2[5].lower():
        print("Result: Same")
        same = same + 1
    else:
        print("Result: Different\n")

    # 5) Checks the favourite sport to watch after the fifth comma for both names and compares them.
    print("Favourite Sport to Watch: " + person1[6] + " vs " + person2[6])
    if person1[6].lower() == person2[6].lower():
        print("Result: Same")
        same = same + 1
    else:
        print("Result: Different\n")

    # 6) Checks the favourite type of music to listen to after the sixth comma for both names and compares them.
    print("Favourite Type of Music to listen to: " + person1[7] + " vs " + person2[7])
    if person1[7].lower() == person2[7].lower():
        print("Result: Same\n")
        same = same + 1
    else:
        print("Result: Different\n")

    # 7) Checks the favourite type of movie to watch after the seventh comma for both names and compares them.
    print("Favourite Type of Movie to Watch: " + person1[8] + " vs " + person2[8])
    if person1[8].lower() == person2[8].lower():
        print("Result: Same")
        same = same + 1
    else:
        print("Result: Different\n")

    # 8) Checks the favourite restaurant in the local area after the eighth comma for both names and compares them.
    print("Favourite Restaurant in the Local Area: " + person1[9] + " vs " + person2[9])
    if person1[9].lower() == person2[9].lower():
        print("Result: Same")
        same = same + 1
    else:
        print("Result: Different\n")

    print("\nThey have " + str(same) + " answers that are the same out of 8.")

    print("\nObservations that I observed:")
    if same > 6:
        print(person1[1] + " and " + person2[1] + " have a lot in common.")
    elif same == 5 or same == 4:
        print(person1[1] + " and " + person2[1] + " have some things in common.")
    elif same <= 3:
        print(person1[1] + " and " + person2[1] + " do not have a lot of things in common.")

    if d1 > d2:
        print(person1[1] + " picked a higher favorite digit than " + person2[1] + ".")
    elif d1 < d2:
        print(person2[1] + " picked a higher favorite digit than " + person1[1] + ".")
    else:
        print("They both picked the same favorite digit.")


