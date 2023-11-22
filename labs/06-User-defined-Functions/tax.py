# Chapter 06 Labs

# Objective

# In this lab you'll gain some experience of using a few of Python's inbuilt functions. In this lab you'll write a function for calculating personal tax in UK.

# Instructions

# The rules for simple tax calculation is as follows:
# Personal allowance: £11,850
# 0 to 34,500 taxed at 20%
# 34,501 to 150,000 taxed at 40%
# Over 150,000 taxed at 45%

# Step-by-step instructions:

# 1- Create a new file called tax.py

# 2- Create a function called getIncomeTax()

# 3- Calculate the income tax based on the simple tax calculation rules as seen above. Tip: You'll need to pass the salary to this function. Use a parameter called salary and base your calculations on the value held by the salary parameter.

# 4- After the calculation is finished you can return the tax amount.

# 5- In the main part of your code, just below where you defined the function, write code to call getIncomeTax() and print the returned value. To test your code, pass different values to the function to test its functionality.

def getIncomeTax(salary):
  if (salary.isdigit() != False):
    print("not a digit")
  salary = float(salary)
  if (salary >= 11850):
    taxableSalary = salary - 11850
    if (salary >= 1 and salary <= 34500):
      tax = (taxableSalary * 0.2)
      formatTaxToString = format(tax,".2f")
      return ("You are taxed at 20%.\nYou need to pay " + "£" + formatTaxToString + " income tax.")
    elif (salary >= 34501 and salary <= 150000):
      tax = taxableSalary * 0.4 
      formatTaxToString = format(tax,".2f")
      return ("You are taxed at 40%.\nYou need to pay " + "£" + formatTaxToString + " income tax.")
    elif (salary >= 150001):
      tax = taxableSalary * 0.45 
      formatTaxToString = format(tax,".2f")
      return ("You are taxed at 45%.\nYou need to pay " + "£" + formatTaxToString + " income tax.")
  else:
    return "No tax, you keep what you earn."
  

print(getIncomeTax("jhfkdf"))