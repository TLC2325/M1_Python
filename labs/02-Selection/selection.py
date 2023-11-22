# PART 1
# 2- Create an IF statement to see if the person is equal to 18 or over.
# a. Display 'You are in catergory A'
print('Task 2;3;4 - create if statements:')
personAge = 10
if (personAge >= 18):
  print("You are in catergory A")

# 3- Create an IF statement to see if the person is 16 or over
# a. Display 'You are in catergory B'
if (personAge >= 16):
  print("You are in catergory B")

# 4- Create another IF statement to see if the person is under 16 years of age.
# a. Display 'You are in catergory C'
if (personAge < 16):
  print("You are in catergory C")

# 5- Save and run your code and enter 19 for age.

# 6- As you see, there are too many confusing messages! Simple IF statements work fine but not in a chain of IF statements such as these

# ------------------------------------------------------------

# 7- Create an if…elif statement to examine the age in one statement.
print('Task 7 - create an if...elif statement:')
age = 16
if (age >= 18):
  print("You are in catergory A")
elif (age >= 16):
  print("You are in catergory B")
else:
  print("You are in catergory C")



