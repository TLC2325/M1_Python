# Input the exam mark for a student. The integer must be between 1..100 If the mark is less than 1 or greater than 100 you'll display a suitable message

# 3- Input the student level. Currently we have two levels (1 or 2).

# 4- The rules for calculating a grade for level 1 are as follows (same as in Task 2):

# If the mark is less than 1 or greater than 100, display 'Error: marks must be between 1..100'

# Less than 50 Fail between 50..60 (inclusive) Pass between 61..70 (inclusive) Merit between 71..100 (inclusive) Distinction

# The rules for calculating a grade for level 2 are as follows:

# Less than 40 Fail between 40..50 (inclusive) Pass between 51..65 (inclusive) Merit between 66..100 (inclusive) Distinction

examMark = input("Input the exam mark for a student: ")
examMark = (int(examMark))
if (examMark < 1 or examMark > 100):
    print('Error: marks must be between 1..100')
    examMark = (int(input("Input the exam mark for a student: ")))

studentLevel = input("1 - Level 1 Students \n2 - Level 2 Students \nSelect option: ")
studentLevel = (int(studentLevel))

if (examMark and studentLevel == 1):
    if (examMark < 50):
        print('Failed')
    elif (examMark >= 50 and examMark<= 60):
        print('Pass')
    elif (examMark >= 61 and examMark<= 70):
        print('Merit')
    elif (examMark >= 71 and examMark<= 100):
        print('Distinction')
elif (examMark and studentLevel == 2):
    if (examMark < 40):
        print('Failed')
    elif (examMark >= 40 and examMark<= 50):
        print('Pass')
    elif (examMark >= 51 and examMark<= 65):
        print('Merit')
    elif (examMark >= 66 and examMark<= 100):
        print('Distinction')
else:
    print('Error: cannot perform grading. Try again.')