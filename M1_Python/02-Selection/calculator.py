# PART 2

# Inputs two numbers (int or float, your choice) Tip: Use two input() statements. Don't forget to cast the text to either int or float.

# 10- Display a typical calculator menu such as Tip: Use simple print() statements

# 11- Ask the user to choose what operation to perform. For example if they select + then you should display the sum of the two numbers. Tip: Use input() statements. There is no need to cast the text. You'll need a single if…elif statement to examine the operator and display the result.

# 12- Save and run.
print('Perform a Calculation')
input_1 = input('Enter the first number:')
input_2 = input('Enter the second number:')

if int(input_1) % 1 == 0:
    firstNumber = int(input_1)
else:
    firstNumber = float(input_1)

if int(input_2) % 1 == 0:
    secondNumber = int(input_2)
else:
    secondNumber = float(input_2)


input_3 = input(
    """
    1 - Add (+)
    2 - Subtract (-)
    3 - Multiply (*)
    4 - Divide (/)
    5 - Square (s)
    Enter the calculation symbol you would like to perform:
    """
)

if (input_3 == "+"):
    print(firstNumber,"+",secondNumber,"=",(firstNumber + secondNumber))
elif (input_3 == "-"):
    print(firstNumber,"-",secondNumber,"=",(firstNumber - secondNumber))
elif (input_3 == "*"):
    print(firstNumber,"*",secondNumber,"=",(firstNumber * secondNumber))
elif (input_3 == "/"):
    print(firstNumber,"/",secondNumber,"=",(firstNumber / secondNumber))
elif (input_3 == "s"):
    print(firstNumber,"squared","=",(firstNumber ** secondNumber))
else:
    "Calculation error, try again."
