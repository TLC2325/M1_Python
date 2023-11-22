from dotenv import load_dotenv

load_dotenv()

import os

PATH = os.getenv("PATH")
# print("-----------1---------",PATH)

# file = open(load_dotenv(".env.filePath"+"carSale.csv"), "r")
# print(file.read())


# _________________________________

# # Method 1: of opening a file in READ-Mode
# file = open("C:/Users/Thuy.LyChambers/Documents/dev/carSale.csv", "r")
# # Read the first line of a file
# line = file.readline()
# # Read every line of a file into memory
# allLines = file.readlines()
# # Must clode file afterwards
# file.close()

# _________________________________

# Method 2: of opening a file in READ-Mode using 'with' and not needing to declare 'READ-MODE' and not needing to close the file
# with open("C:/Users/Thuy.LyChambers/Documents/dev/carSale.csv") as file:
#     for line in file:
   
# _________________________________
# Step by step

# 1- Create two Lists as: 
# companies = []
# sales = []

# 2- Read all the lines from carSale.csv file

  
# 3- Loop through the resulting lines and place companies into the companies List (using the append() method) and then place the data line into the sales.

# Tip 1: you will need to go through the lines that you've read in steps of 2 like:
# for x in range(0, len(lines),2):

# Tip 2: you will need to make a numeric List out of the sales data line using code like
# data = line.strip().split(',')
# sales.append(list(map(int,data)))

# 4- Now that you've all the data in Lists you can do the calculations


with open("C:/Users/Thuy.LyChambers/Documents/dev/carSale.csv") as file:
    carList = file.readlines()

# print("----1-----",carList)

companies = []
sales = [] 
for i in carList:
  i = i.strip()
  if (
     i == "Ford Motor Company"
     or i == "Volkswagen UK"
     or i == "Mercedes-Benz UK"
     or i == "Vauxhall Motors"
     or i == "BMW"
  ):
      companies.append(i)
  else:
      sales.append(i)

# print(sales[0])
# arr = sales[0].split(",")
# hello = list(map(int, arr))
# print(hello)

# print("--------------------------------")
# print("Companies:",companies)
# print("\n")
# print("Sales:",sales)
# print("--------------------------------")

intSalesList = []
for i in sales:
    split = i.split(",")
    convertToInt = list(map(int, split))
    intSalesList.append(convertToInt)

# print("Sales as Int:", intSalesList)

# 4- Now that you've all the data in Lists you can do the calculation
# Instructions

# Your task is to read the data and display the following stats:

# 1- Sum of cars sold in each month.

carsSoldEachMonth = dict()
month = 1
index = 0
monthlySales = []

# for i = 0; in intSalesList:
#     print("Each company:",i)





# for sale in intSalesList:
#     monthlySales.append(sale[i])
#     carsSoldEachMonth.update({month : monthlySales})
#     print(carsSoldEachMonth)

# for index, val in enumerate(intSalesList):
#     print(index, val)
monthlySales = []
innerIndex = 0
for index in range(len(intSalesList)):
    value = intSalesList[index][innerIndex]
    monthlySales.append(value)
    # print(index, value)
    # print(monthlySales)

result = [0] * len(intSalesList[0])
print("-------", result)
print("-------", len(intSalesList[0]))

for subList in intSalesList:
    print(range(len(subList)))
    for i in range(len(subList)):
        result[i] += subList[i]
print(result)





# for index, val in enumerate(intSalesList, start=0):
#     print(index, val)


# 2- Total yearly sales by each manufacturer.
# yearlySaleKeys = dict.fromkeys(["Ford Motor Company", "Volkswagen UK", "Mercedes-Benz UK", "Vauxhall Motors", "BMW"])

totalSales = []
for i in intSalesList:
    amount = sum(i)
    totalSales.append(amount)
      
# finalYearlySales = dict(zip(yearlySaleKeys, totalSales))
# print(finalYearlySales)

   


# company: {
#     name: ford,
#     sales: {
#         jan: 123,
#         feb: 456,
#         march: 678
#     }
# }


outer = [
    [16629, 10390, 40755, 18074, 19892, 22049, 17049, 10764], 
    [13224, 7960, 38335, 15161, 15737, 20474, 15183, 11334],
    [12249, 6088, 33536, 11739, 14431, 14947, 12056, 5040],
    [12250, 4905, 37769, 10639, 13461, 15540, 10398, 4864], 
    [9553, 6870, 30330, 10868, 12415, 19985, 9198, 4853]
]

# result = []
# for (i=0; i<=outer.length; i++)
#   innerArray = outer[i]
#   for (inner=0; inner<=innerArray.length; inner++) {
#      result[i] = result[i] + innerArray[inner]
#   }

  


