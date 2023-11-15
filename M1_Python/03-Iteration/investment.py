# Task 3 - Investment

# 1- Create a text file called investment.py

# 2- Calculates how many years it will take an initial investment of £100 to grow to a target value of £1000 if the interest rate is 10% Tip: Do not start writing code until you have a plan of action!

# 3- Save and run.

# 4- Make your calculation more usable by inputting the following values: Initial investment Target value Interest rate

# 5- Save and run.

# currentValue = 100
# currentValue = float(currentValue)
# target = 1000
# target = float(target)
# numOfYears = 0

# while (currentValue < target):
#     currentValue = (currentValue / 100) * 10
#     numOfYears = numOfYears + 1

# print(numOfYears)
investment = float(100)
targetValue = float(1000)
years = 0 

while (investment < targetValue):
    investment = investment + ((investment/100) * 10)
    roundToNearest = "{:.2f}".format(investment)
    years = years + 1
    print("In year:",years,"your interest would be £", roundToNearest)
  
