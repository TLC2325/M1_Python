# Task 2 - Time Calculator

# Your task is to write code that for a range of calculation on times. Times should be stored and inputted as strings in the format DD:HH:MM. Days, Hours and Minutes should be stored as integers.

# 1- Create a file called timecalculator.py

# 2- Input two day-time strings from the user. Your code will do calculations until the user selects option 9 (see below).

# 3- Print a main menu:

import time

# Original solution
# option = int(input(
# """
# ------------Time Calculator------------
# [1] Add 2 times
# [2] Find the difference between 2 times
# [3] Convert to Hours
# [4] Convert to Minutes
# [5] Convert Minutes to Time
# [6] Convert Hours to Time
# [7] Convert Days to Time
# [8] Exit 
# ----------------------------------------
# Select menu option: """
# ))

# menu = [1, 2, 3, 4, 5, 6, 7, 8]

# while (option in menu):
#     print("Enter time in format DD:HH:MM (Days, Hours and Minutes)")
#     time_1 = input("Enter time 1: ")
#     time_2 = input("Enter time 2: ")
#     # Convert the inputs into lists
#     time_1 = time_1.split(":")
#     time_2 = time_2.split(":")

#     time_1_days = int(time_1[0])
#     time_1_hours = int(time_1[1])
#     time_1_minutes = int(time_1[2])

#     time_2_days = int(time_2[0])
#     time_2_hours = int(time_2[1])
#     time_2_minutes = int(time_2[2])

#     if (option == 8):
#         break
#     elif (option == 1):
#         totalDays = time_1_days + time_2_days
#         totalHours = time_1_hours + time_2_hours
#         totalMinutes = time_1_minutes + time_2_minutes

#         if (totalHours >= 24):
#             days = totalHours / 24
#             totalDays += days
#             remainingHours =  totalHours % 24
#             print(remainingHours)
#             totalHours = remainingHours
        
#         if (totalMinutes >= 60):
#             hours = totalMinutes / 60
#             remainingMinutes =  totalMinutes % 60
#             totalHours += hours
#             totalMinutes = remainingMinutes

#         print('Add 2 times: %02d:%02d:%02d'%(totalDays,totalHours,totalMinutes))
        

#         option = int(input(
#         """
#         Select another option:
#         [1] Add 2 times
#         [2] Find the difference between 2 times
#         [3] Convert to Hours
#         [4] Convert to Minutes
#         [5] Convert Minutes to Time
#         [6] Convert Hours to Time
#         [7] Convert Days to Time
#         [8] Exit 
#         Select menu option: """
#         ))
#     elif (option == 2):
#         totalDays = time_1_days - time_2_days
#         totalHours = time_1_hours - time_2_hours
#         totalMinutes = time_1_minutes - time_2_minutes

#         if (totalHours >= 24):
#             days = totalHours / 24
#             totalDays += days
#             remainingHours =  totalHours % 24
#             print(remainingHours)
#             totalHours = remainingHours
        
#         if (totalMinutes >= 60):
#             hours = totalMinutes / 60
#             remainingMinutes =  totalMinutes % 60
#             totalHours += hours
#             totalMinutes = remainingMinutes

#         print('Find the difference between 2 times: %02d:%02d:%02d'%(totalDays,totalHours,totalMinutes))

        
#         option = int(input(
#         """
#         Select another option:
#         [1] Add 2 times
#         [2] Find the difference between 2 times
#         [3] Convert to Hours
#         [4] Convert to Minutes
#         [5] Convert Minutes to Time
#         [6] Convert Hours to Time
#         [7] Convert Days to Time
#         [8] Exit 
#         Select menu option: """
#         ))
#     elif (option == 3):
#         calculateDaystoHours = (time_1_days + time_2_days) * 24
#         print(calculateDaystoHours)
#         totalHours = time_1_hours + time_2_hours + calculateDaystoHours
#         totalMinutes = time_1_minutes + time_2_minutes
        
#         if (totalMinutes >= 60):
#             hours = totalMinutes / 60
#             remainingMinutes =  totalMinutes % 60
#             totalHours += hours
#             totalMinutes = remainingMinutes
        
#         print('Convert to Hours: %02d hours and %02d minutes'%(totalHours,totalMinutes))

#         option = int(input(
#         """
#         Select another option:
#         [1] Add 2 times
#         [2] Find the difference between 2 times
#         [3] Convert to Hours
#         [4] Convert to Minutes
#         [5] Convert Minutes to Time
#         [6] Convert Hours to Time
#         [7] Convert Days to Time
#         [8] Exit 
#         Select menu option: """
#         ))
#     elif (option == 4):
#         calculateDaystoHours = (time_1_days + time_2_days) * 24
#         totalHours = time_1_hours + time_2_hours + calculateDaystoHours
#         hoursToMinutes = totalHours * 60

#         totalMinutes = time_1_minutes + time_2_minutes + hoursToMinutes
        
#         print('Convert to Minutes: %02d minutes'%(totalMinutes))
# print("Exiting from loop.")


while True:
    option = int(input(
    """
    ------------Time Calculator------------
    [1] Add 2 times
    [2] Find the difference between 2 times
    [3] Convert to Hours
    [4] Convert to Minutes
    [5] Convert Minutes to Time
    [6] Convert Hours to Time
    [7] Convert Days to Time
    [8] Exit 
    ----------------------------------------
    Select menu option: """
    ))
    
    if (option == 1 or option == 2 or option == 3 or option == 4): 
         #Ask user inputs
        print("Enter time in format DD:HH:MM (Days, Hours and Minutes)")
        time_1 = input("Enter time 1: ")
        time_2 = input("Enter time 2: ")

        # Convert the inputs into lists
        time_1 = time_1.split(":")
        time_2 = time_2.split(":")

        time_1_days = int(time_1[0])
        time_1_hours = int(time_1[1])
        time_1_minutes = int(time_1[2])

        time_2_days = int(time_2[0])
        time_2_hours = int(time_2[1])
        time_2_minutes = int(time_2[2])
    
        if (option == 1):
            totalDays = time_1_days + time_2_days
            totalHours = time_1_hours + time_2_hours
            totalMinutes = time_1_minutes + time_2_minutes

            if (totalHours >= 24):
                days = totalHours / 24
                totalDays += days
                remainingHours =  totalHours % 24
                print(remainingHours)
                totalHours = remainingHours
            
            if (totalMinutes >= 60):
                hours = totalMinutes / 60
                remainingMinutes =  totalMinutes % 60
                totalHours += hours
                totalMinutes = remainingMinutes

            print('Add 2 times: %02d:%02d:%02d'%(totalDays,totalHours,totalMinutes))
        elif (option == 2):
            totalDays = time_1_days - time_2_days
            totalHours = time_1_hours - time_2_hours
            totalMinutes = time_1_minutes - time_2_minutes

            if (totalHours >= 24):
                days = totalHours / 24
                totalDays += days
                remainingHours =  totalHours % 24
                print(remainingHours)
                totalHours = remainingHours
            
            if (totalMinutes >= 60):
                hours = totalMinutes / 60
                remainingMinutes =  totalMinutes % 60
                totalHours += hours
                totalMinutes = remainingMinutes

            print('Find the difference between 2 times: %02d:%02d:%02d'%(totalDays,totalHours,totalMinutes))

        elif (option == 3):
            calculateDaystoHours = (time_1_days + time_2_days) * 24
            print(calculateDaystoHours)
            totalHours = time_1_hours + time_2_hours + calculateDaystoHours
            totalMinutes = time_1_minutes + time_2_minutes
            
            if (totalMinutes >= 60):
                hours = totalMinutes / 60
                remainingMinutes =  totalMinutes % 60
                totalHours += hours
                totalMinutes = remainingMinutes
            
            print('Convert to Hours: %02d hours and %02d minutes'%(totalHours,totalMinutes))

        elif (option == 4):
            calculateDaystoHours = (time_1_days + time_2_days) * 24
            totalHours = time_1_hours + time_2_hours + calculateDaystoHours
            hoursToMinutes = totalHours * 60

            totalMinutes = time_1_minutes + time_2_minutes + hoursToMinutes
            
            print('Convert to Minutes: %02d minutes'%(totalMinutes))

    elif (option == 5):
        minutes = int(input("Enter minutes to convert: "))
        totalHours = minutes / 60
        totalMinutes = minutes % 60
        totalDays = 0

        if (totalHours >= 24):
            totalDays = totalHours / 24
            totalHours =  totalHours % 24
        
        print('Convert Minutes to Time: %02d:%02d:%02d'%(totalDays,totalHours,totalMinutes))
    
    elif (option == 6):
        hours = int(input("Enter hours to convert: "))
        totalDays = 0

        if (hours >= 24):
            totalDays = hours / 24
            totalHours =  hours % 24
              
        print('Convert Hours to Time: %02d:%02d:00'%(totalDays,totalHours))
    
    elif (option == 7):
        days = int(input("Enter days to convert: "))
      
        print('Convert Days to Time: %02d:00:00'%(days))
    
    elif (option == 8):
        print("Exiting loop, goodbye")
        break

    else:
        print("Error, try again")
        


    
