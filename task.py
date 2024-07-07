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
#    result = number * i
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

# Python Data Base

# myString = "PythonProgramming"

# print(myString[-11::])

# User = "Python " + "Programming"
# print(User)

# password = " Hello  U"
# new = password.strip()
# print(password)
# print(new)  

# Upadating string character in python
# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1)

# list1 = list(String1)
# list1[2] = 'p'
# String2 = "".join(list1)
# print("\nUpadating character at 2nd Index: ")
# print(String1)

# String3 = String1[0:2] + 'p' + String1[3:]
# print(String3)


# Formating 
# age = 18
# text = f"My name is John, I am  {age}"
# print(text)


# name = "Suraj"
# age = 18
# location = 'kapan'

# print(f"Hi, My name is {name} and my age is {age} and My location is {location}")

# Adding list items
# Change item list
# thislist = ["apple", "Banana", "Cherrt"]
# thislist[1] = "BlackCurrent"
# print(thislist)

# #Using Extend method

# thislist = ["apple", "Banana", "Cherrt"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# # Deleting list Items
# # Using del keyword
# thislist = ["apple", "Banana", "Cherrt"]    
# del thislist[0]
# print(thislist)

# # Loop through the list

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)


# # Using loop with range 

# thislist = ["apple", "banana", "cherrt"]
# for i in range(len(thislist)):
#     print(thislist[i])


# # Tuple
# fruitsData = ("apple", "banana", "cherry")
# print(fruitsData)


#Unpacking Tuple
# fruitsData = ("apple", "banana", "cherry", "strawberry","Rasberry")
# (green, yellow ,*red) = fruitsData

# print(green)
# print(yellow)
# print(red)

# Dictionaries Data Type
# Adding , Upadate, Removing
# carDetails = {
#     "brand":"ford",
#     "model" : "mustang",
#     "year" : "2020"
# }
# # print(carDetails["brand"])
# # print(carDetails["model"])
# # print(carDetails["year"])
# # print(carDetails.keys())
# # print(carDetails.values())  
# carDetails["color"] = "Red"
# carDetails.update({"mielage": 8})
# carDetails.pop("mielage")
# carDetails.popitem()
# print(carDetails)

# loop through Dictionary

# Student = {
#     "name" : "John",
#     "age" : 25,
#     "grade" : "XII"
# }
# for x in Student:
#  print(x)

# for x in Student.values():
#  print(x)

# for x, y in Student.items():
#  print(x, y)

# texasStudent = {
#     "firstYear" :{
#         "name" : "John",
#         "course": "BIT",
#         "batch":"2020"
#     },
#     "secondYear" :{
#         "course" : "BHM",
#         "batch" : "2021"
#     },
#     "thirdYear" :{
#         "course" : "BBA",
#         "batch" : "2022"
#     }
# }
# print(texasStudent["firstYear"])

# Dictionary Items
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : "1964",
#     "color": ["black", "white", "red"],
# }
# print(thisdict["color"][1])

# Function
# zip() Function
# list1 = [1, 2, 3]
# list2 = ['a','b','c']
# zipped = zip(list1, list2)
# print(list(zipped))
# print(zipped)

# User Defined Function

# with Argument

# def combine (fname, lname):
#     print(fname + " " + lname)

# # Calling the function
# combine("john", "Doe")

# With parameter
# def combine (fname= "john", lname= "Doe"):
#     print(fname + " " + lname)

# # Calling the function
# combine()

# Return Statement
# def square (num):
#     output =num * num
#     return output

# def display():
#     value = square(7) 
#     print(f"Hello Number is {value}")
# display()

# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))
