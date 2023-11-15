# Task 6 - Exam Average

# 1- Create a text file called examaverage.py

# 2- Code a program that:

# a. Has code to calculate the average of three exam marks

# b. If the average mark is >= 65 output a "Pass"

# c. If it is < 65 output a "Fail"

# 3- In the main body of the program input the marks for a student for Math, English and ICT exams

# 4- Marks should be an integer between 0 and 100

# a. Use a loop until the user enters a valid mark

# b. Calculate and display their average mark and overall result

# c. Please also display the average mark and print out the average.

# 5- Save and run.

englishMark = int(input("Enter English Mark: "))
if (englishMark < 1 or englishMark > 100):
    print('Error: English mark must be between 1..100')
    englishMark = (int(input("Enter English mark: ")))

mathMark = int(input("Enter Math Mark: "))
if (mathMark < 1 or mathMark > 100):
    print('Error: Maths mark must be between 1..100')
    mathMark = (int(input("Enter Maths mark: ")))

icTMark = int(input("Enter ICT Mark: "))
if (icTMark < 1 or icTMark > 100):
    print('Error: ICT mark must be between 1..100')
    icTMark = (int(input("Enter ICT mark: ")))

averageMarks = (englishMark + mathMark + icTMark) / 3

if (averageMarks >= 65):
    print("Student - Pass")
elif (averageMarks < 65):
    print("Student - Fail")
else:
    print("Could not perform calculation, try again.")