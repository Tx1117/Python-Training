# Task 1
# Write a python program to display students grade
# First ask user score using input method
# Check if user score above 90, print your grade is A
# Check if user score above 75, print your grade is B
# Check if user score above 65, print your grade is C
# Check if user score below 40, print your grade is Fail 


# score = int(input("Enter your score: "))

# score > 100
# print("Plz Enter Valid Score ")

# if score<=100:
#     if score > 90:
#         print("Your grade is A")    
#     elif score > 75:
#         print("Your grade is B")
#     elif score > 65:
#         print("Your grade is C")
#     else:
#         print("Your grade is Fail")

# else:
#     print("error")


# write a program to calculate the electricity bill according to the following data.

# units = int(input("Enter your unit for Payment"))
# cost = 0
# if units <= 100:
#     print("No charge")
# elif units > 100:
#     cost = (units - 100) * 5
# elif units > 150:
#     cost = (150* 10) + (100*5)
# print("Your bill cost",{cost})


# Loop in python  with else exampleclear

# fruits = ["apple", "banana", "grapes"]
# for index in range (len(fruits)):
#     print(fruits[index])
# else:
#     print(len(fruits))

# While loop

# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Programmers")

# while loop with else statement 

# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Suraj ")
# else:
#     print("In Else Block")

# Nested loop

# adj = ["red", "big", "Tasty"]
# fruits = ["apple", "grapes", "Cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,'\t',y,'\n')  # \t for  one space

# nested for loop statement 

# for i in range (1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# i = 1
# while i < 10:
#  j = i
# while j < 10:
#   print(f"{j}", end=' ')
#   j = j +1
# print("")
# i= i+1
# print("Complete")

# Day -3 Task

# Q1. Write a program to print multiplication table of a given number(accept number from user)
# eg. if user input 3
# 3 x 1 = 3
# 3 x 2 = 6 and so on

# number = int(input("Enter Your Number U Want Table: "))
# for i in range (1, 11):
#    result = number * 1
#    print(f"{number} * {i} = {result}")

# Q2. Accept 10 numbers from user and display average of it.

# numbers = []
# for i in range (10):
#    num = int(input(f"Enter Number {i+1} : "))
#    numbers.append(num)
# avg = sum(numbers)/ len(numbers)
# print(f"The Sum of 10 Number:{avg}")


# Q3. Write a program to display numbers which is divisible by only 11 from 100 to 300.

# print("The number divible by 11 from 100 - 300 are :")
# for num in range (100, 301):
#    if num % 11 == 0:
#       print(num)
      
