# Task 2 - Time Calculator

# Your task is to write code that for a range of calculation on times. Times should be stored and inputted as strings in the format DD:HH:MM. Days, Hours and Minutes should be stored as integers.

# 1- Create a file called timecalculator.py

# 2- Input two day-time strings from the user. Your code will do calculations until the user selects option 9 (see below).

# 3- Print a main menu:

import time

# # Convert the inputs into lists
# time_1 = time_1.split(":")
# time_2 = time_2.split(":")

# #wait for 1 second
# time.sleep(1)

option = int(input("""
Time Calculator
[1] Add 2 times
[2] Find the difference between 2 times
[3] Convert to Hours
[4] Convert to Minutes
[5] Convert Minutes to Time
[6] Convert Hours to Time
[7] Convert Days to Time
[8] Exit 
Select menu option: """))

menu = [1, 2, 3, 4, 5, 6, 7, 8]
menuLength = len(menu)

while (option in menu):
    if (option == 8):
        break
    elif (option == 1):
        print("------1-----")
        # Request input from user
        print("Enter time in format DD:HH:MM (Days, Hours and Minutes)")
        time_1 = input("Enter time 1: ")
        time_2 = input("Enter time 2: ")
        c = time_1 + time_2
        print(c)

        time.sleep(1)

        option = int(input("""
Select another option:
[1] Add 2 times
[2] Find the difference between 2 times
[3] Convert to Hours
[4] Convert to Minutes
[5] Convert Minutes to Time
[6] Convert Hours to Time
[7] Convert Days to Time
[8] Exit 
Select menu option: """))
    elif (option == 3):
        print("------3-----")
        break
    elif (option == 4):
        print("------4-----")
        break
    elif (option == 5):
        print("------5-----")
        break
    elif (option == 6):
        print("------6-----")
        break
print("Goodbye")

