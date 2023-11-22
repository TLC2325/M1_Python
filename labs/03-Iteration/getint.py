# Task 4 – Input an integer between two limits

# In this part you'll ask the user to input an integer between a minimum and maximum values.

# If the user fails to enter an acceptable value after three attempts then you stop asking!

# 1- Create a text file called getint.py

# 2- Create two variables for the min and max values. Set two values for these variables such as 1 and 100.

# 3- Write a while loop that attempts to get an integer from the user between the limits of min and max values.

# 4- If the user tries three times and fails then print None. If a valid value is entered, just end the loop and print its value. Note: None is a valid keyword in Python which is equivalent to null

maxAttempts = 3
numOfTries = 0

minValue = 1
maxValue = 100

while (numOfTries <= maxAttempts):
    userInput = input("Enter a number: ")
    num = int(userInput)
    if (num >= minValue and num <= maxValue):
        print("Acceptable number: ",userInput)
    numOfTries = numOfTries + 1
    if (numOfTries == 3):
        print(None)
        break

   
    