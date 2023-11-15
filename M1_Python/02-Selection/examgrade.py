# Input the exam mark for a student. The integer must be between 1..100 if the mark is less than 1 or greater than 100 you'll display a suitable message (see below)

# 3- The rules for calculating a grade is as follows: If the mark is less than 1 or greater than 100, display 'Error: marks must be between 1..100'

# Less than 50 Fail between 50..60 (inclusive) Pass between 61..70 (inclusive) Merit between 71..100 (inclusive) Distinction

examMark = input("Input the exam mark for a student: ")
examMark = (int(examMark))

if (examMark < 1 or examMark > 100):
    print('Error: marks must be between 1..100')
elif (examMark < 50):
    print('Failed')
elif (examMark >= 50 and examMark<= 60):
    print('Pass')
elif (examMark >= 61 and examMark<= 70):
    print('Merit')
elif (examMark >= 71 and examMark<= 100):
    print('Distinction')
else:
    print("Exam mark must be a number from 1 to 100.")
