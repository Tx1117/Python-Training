# # Develop a game where the computer randomly selects a number within a specified range, and the user has to guess the number.
# Provide hints if the guessed number is too high or too low.
# After user guess correct number display guess attempts and the exact answer too.
# Make sure user does not input other than integer, if its other data type show them invalid input.

# Generate a random number between 1 and 100
# import random
# def number_guessing_game():
    
#     secret_number = random.randint(1, 100)
#     attempts = 0

#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")

#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#             attempts += 1

#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number {secret_number} correctly!")
#                 print(f"It took you {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a Number.")

# number_guessing_game()



# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters: 3
# No. of Lower case Characters : 12
# Note: If you can take string input from user you can do it . 


# user_Input = str(input("Plz Enter Any String:"))

# def countUpperLower(user_Input):
#     count ={
#     "Upper_Case" : 0,
#     "Lower_Case" : 0
# }
#     for character in user_Input:
#         if character.isupper():
#             count["Upper_Case"] += 1
#         elif character.islower():
#             count["Lower_Case"] += 1
#         else:
#             pass

#     print("Your String ", user_Input)
#     print("No. OF Upper Characters:", count["Upper_Case"])
#     print("No. OF Lower Characters:", count["Lower_Case"])

# countUpperLower('This is a Game ')


