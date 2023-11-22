# Create a file called ageslist.py

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# 2- Record the length of the ages List in a variable (you'll need it later) Display the length. Test your code
ageLength = len(ages)
print("Exercise 2:")
print(ageLength)

# 3- Display these ages one on each line: Tip: Use a for loop to read each number.
# Test your code
# Answer:
# index = 0
# for i in ages:
#     print(index,"=",i)
#     index += 1

# 4- Add one year to every age! Tip: ages[n] is the nth element of ages. To increase (say) element 2 you may do ages[2] += 1 len(ages) will return the length of the ages List.

# Redisplay ages to test your code
# x = 0
# for i in ages:
#     newAge = i + 1
    # print(x,"=",newAge)
    # x += 1

# 5- Our code only takes into account those people in the age range of 16-65 (inclusively) Please delete all ages which are outside this range Tip: There are other ways of achieving this task but one way is to use a for loop that uses the len() function to examine each item and then use the del() function to remove an item at certain index.

# Redisplay ages to test your code
validAgeList = []
for age in ages:
    if (age >= 16 and age <=65):
        validAgeList.append(age)
print("\n")
print("Exercise 5:")
print(validAgeList)
    
# 6- Display the count of 16-25 year olds

# Test your code
counter = 0
for age in ages:
    if (age >= 16 and age <=25):
        counter += 1

print("\n")
print("Exercise 6:")
print("Displaying the count for 16-25 year olds:",counter)


# 7- Invoke the sort method on the ages List. Tip: Use this line of code: ages.sort()

# Display the ages List to make sure they are sorted.
agesInOrder = ages.copy()
agesInOrder.sort()
print("\n")
print("Exercise 7:")
print(agesInOrder)

# 8- What proportion of ages fall between 16-25? Test your code by displaying this value

calculatePercentage = ((ageLength - counter) / ageLength * 100)
portion = 100 - calculatePercentage
roundToNearest = round(portion, 2)

print("\n")
print("Exercise 8:")
print(roundToNearest,"%")

