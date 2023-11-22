# Chapter 05 Lab

# Objective

# In this lab you'll gain some experience of using a few of Python's inbuilt functions.

# Instructions

# Your task is to present some statistics on the following students' grades that are read from a file.

# 1- data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# 2- Create a file called grader.py

# 3- Copy the data string above into this file

import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# 4- To extract information from this string, you'll need to split it by ',' as delimiter. Put the resulting List into a variable called grades. Tip: use the string's split function and pass it ',' as delimiter.

grades = data.split(",")
# print(grades)

# 5- Display the minimum value of the grades Tip: use the min() function
newGradesList = [int(i) for i in grades]
print(newGradesList)

minGrade = min(newGradesList)
print("The minimum grade is:",minGrade)

# 6- Display the maximum value of grades Tip: use the max() function
maxGrade = max(newGradesList)
print("The maximum grade is:",maxGrade)

# 7- Test your code and check if the values are correct. Did your code display 100 for the minimum value and 99 for the maximum? But how can 100 be a minimum? Any ideas why this is so. Think about this before reading the next step.

# 8- OK, as you've guessed it, we're dealing with a list of strings who just look like a List of numbers! That is why "100" is less than "17" because the first character '1' is the same but the second character '0' is less than the letter '3'.

# 9- So, you need to cast every element of a List of strings into a List of integers. This is a common task and a hard one to code but the clever Python 3.0 gives us a tool called map to do this task. The map function was not covered in the lectures, so we'll cover this useful function here in this lab.

# Just after splitting the string into a list of strings called grades, type: grades = list(map(int, grades)) This line of code casts grades into a list of ints.
gradesByMapping = list(map(int, grades))
print(gradesByMapping)

# 10- Now, run your code again. Does it give the right values for min and max (14 & 100)?
minGrade = min(gradesByMapping)
mxGrade = max(gradesByMapping)
print("Min grade:",minGrade,"\nMax grade:", mxGrade)

# 11- Display the average of grades to 2 decimal points. Tip: use the sum(), len() and round() functions
lenOfGradesList = len(gradesByMapping)
average = sum(gradesByMapping) / lenOfGradesList
roundAverageToDecimals = round(average,2)

print("The average grades to 2 decimal points is:",roundAverageToDecimals)
# 12- Import the statistics library Tip: at the first line of your file type import statistics

# 13- Use the statistics' mean() function to get the average grade to 2 decimal places Tip: use the statistics.mean() function
stat = statistics.mean(newGradesList)
print("Using statitics' mean():",stat)

# 14- Display the median values using the statistics.median() function. Note: this is not the same as the mean value. Please investigate what a median is if you're not sure.
middleValue = statistics.median(newGradesList)
print("Using statitics' median ():",middleValue)

# 15- Use the string.format() function to display the min, max,average, mean() and median values.
print("From the grades list:\n1. The minimun value is {}\n2. The maximum value is {}\n3. The average grade is {}".format(minGrade, maxGrade, roundAverageToDecimals))