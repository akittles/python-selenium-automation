# Homework Lesson 2 - Numbers - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 0 - This exercise is solved so you can have an ----------
# example of how we are expecting your answers to be.
#
# You are shopping online and found two items with prices $5.99
# and $3. Calculate and print the total cost.
item1_price = 5.99
item2_price = 3
total_cost = item1_price + item2_price
print(total_cost)

# ---------------------------------------------------------------------
# Exercise 1 - Travel Distance
# Alex is planning a road trip and wants to know the total distance
# he will be driving. He will travel at an average speed of 60 miles
# per hour and has 4 hours available for driving. Calculate the
# total distance he can cover and print the result.

average_speed = 60
hours_available = 4
total_distance = average_speed * hours_available # calculate here
print(total_distance)  # print the result

# ---------------------------------------------------------------------
# Exercise 2 - Pizza Slices
# A pizza is cut into 8 equal slices. Calculate and print how many
# slices each person will get if there are 4 people sharing the pizza.

pizza_slices = 8
people = 4
slices_per_person = pizza_slices / people
print(slices_per_person)

# ---------------------------------------------------------------------
# Exercise 3 - Shopping Discount
# Lisa wants to buy a pair of shoes that cost $80. The store is
# offering a 20% discount on the shoes.
# Create two variables: original_price and discount_percentage and
# assign the given values.
# Create final_price to calculate the price Lisa has to pay and
# print the result.
# The formula to count the discounted price:
# multiply the original price by the discount percentage and divide by 100.

original_price = 80
discount_percentage = 20
discount = original_price * discount_percentage / 100
final_price = original_price - discount
print(final_price)


# ---------------------------------------------------------------------
# Exercise 4 - Temperature Conversion
# You are designing a weather app and need to convert temperature
# from Celsius to Fahrenheit for display. Convert a given
# temperature and print the result.
# To convert Celsis to Fahrenheit you need to multiply
# the temperature in Celsius by 9/5 and add 32 to the result

celsius_temp = 30
fahrenheit_to_celsius = 9.0 / 5.0 * celsius_temp
print(fahrenheit_to_celsius)



# ---------------------------------------------------------------------
# Exercise 5 - Gardening
# You're planning a garden and need to calculate the area of
# a circular flowerbed with a radius of 3.5 meters. Calculate
# and print the area of the flowerbed.
# To calculate the area of a circle, multiply π (~3.141) with the square of
# the circle's radius.

radius = 3.5
pi = 3.141
area = pi * radius ** 2
print(area)


# ---------------------------------------------------------------------
# Exercise 6 - Convert Temperature
# You're building a weather app, and you want to display the current
# temperature rounded to the nearest whole number. The
# temperature data you received from the weather service is a float.
# Your task is to convert the float temperature to an integer
# temperature for display.
# As an example, if the temperature is 24.8ºC, you need to print 24.

temperature = 273.15
curr_temp = float(temperature)
print(curr_temp)


# ---------------------------------------------------------------------
# Exercise 7 - Baking Cookies
# You are baking cookies and have 17 chocolate chips. You
# want to distribute them evenly into 5 cookies. Calculate and
# print the number of chocolate chips in each cookie and the
# remaining chips.

cc = 17
cookies = 5
c_per_cookies = cc // cookies
remaining_chips = cc - (cookies * c_per_cookies)

print(f'There are {c_per_cookies} per cookie and {remaining_chips} remaining chips')

# ---------------------------------------------------------------------
# Exercise 8 - Fix the Code - Event total earnings
# FOR THIS EXERCISE YOU WILL HAVE AN EXISTING CODE THAT IS
# NOT WORKING CORRECTLY. YOUR TASK IS TO LOOK AT THE CODE
# AND FIX THE PROBLEM SO IT WORKS AS EXPECTED.
#
# Tip: Copy the code and try to run it alone. See the results
# and try to figure out why it is not working.
#
# You organized two events. The first event had 250 participants
# and the second event had 500 participants. With a ticket price
# of $1000, calculate and print the total earning of the two events
# together.
#
# For the values provided we are expecting a total earning of 750000,
# however the code is not working correctly. Can you fix it?
first_event_participants = 250
second_event_participants = 500
ticket_cost = 1000

total_earnings = (first_event_participants + second_event_participants) * ticket_cost
print(total_earnings)


# ---------------------------------------------------------------------
# Exercise 9 - Fix the Code - Student age mean
# FOR THIS EXERCISE YOU WILL HAVE AN EXISTING CODE THAT IS
# NOT WORKING CORRECTLY. YOUR TASK IS TO LOOK AT THE CODE
# AND FIX THE PROBLEM SO IT WORKS AS EXPECTED
#
# Tip: Copy the code and try to run it alone. See the results
# and try to figure out why it is not working.
#
# You're a teacher organizing a school event and need to
# calculate the mean age of three students participating in
# the event. The ages of the students are as follows:
#   Student 1: 15 years old
#   Student 2: 17 years old
#   Student 3: 13 years old
#
# For these ages, we expect an age mean of 15.0, but your code
# is returning 36.3. Fix the code to print the correct value.
student_1_age = 15
student_2_age = 17
student_3_age = 13

students_age_mean = (student_1_age + student_2_age + student_3_age) / 3
print(students_age_mean)

# ---------------------------------------------------------------------
# Challenge (OPTIONAL!): Separating Digits of a Number
# Given the number 1597, your task is to write a Python code
# that separates this number into four variables, each containing
# a digit of the number: 1, 5, 9, and 7. You'll use the
# knowledge of Python operators % and /, variable assignment,
# and working with integers to accomplish this task.

# Tip: To separate the digits of a number, think about how you
# can extract each digit using the remainder (%) and division (/)
# operators. Start by extracting the last digit and then move on
# to the next digits by dividing the number progressively.
# Remember that the remainder when dividing by 10 gives you
# the last digit, and integer division by 10 removes the last digit.
#
# The following code should help you to get an understanding on
# how to get the digits of the number
number = 1597

digit_1 = number % 10
number = number // 10
print(digit_1)
print(number)

digit_2 = number % 10
number = number // 10
print(digit_2)
print(number)

digit_3 = number % 10
number = number // 10
print(digit_3)
print(number)

digit_4 = number % 10
number = number // 10
print(digit_4)
print(number)

#----------------------NEXT LESSON--------------------------------

# Homework Lesson 2 - Strings

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Personalized Greeting
# Write a program that takes a user's name as input
# and then greets them using an f-string: "Hello, [name]!"
#
# Example Input: "Alice"
# Example Output: "Hello, Alice!"
name = input("Enter yor name: ")
print(f"Hello {name}")

# ---------------------------------------------------------------------
# Exercise 2: Greeting with User's Favorite Activity
# Write a program that takes a user's name and their
# favorite activity as input, and then greets them
# using the formatting method of your choice as:
# "Hello, [name]! Enjoy [activity]!"

# Example Input:
# Name: Emily
# Favorite Activity: hiking
# Example Output: "Hello, Emily! Enjoy hiking!"

name = input("Enter your name: ")
favorite_activity = 'hiking'
print(f'Hello, {name}! Enjoy {favorite_activity}')



# ---------------------------------------------------------------------
# Exercise 3: Membership Cards
# You are designing a simple registration system for a club.
# When new members sign up, you want to ensure their names
# are displayed in uppercase on their membership cards.
# Write a program that takes the new member's name as
# input and prints it in uppercase and prints a welcome message
# using .format()

# Example Input:
# Name: Emily
# Example Output: "Welcome, Emily! Your name in uppercase is: EMILY!"

name = input("Enter your name: ")
print(f'Welcome, {name}!','Your name in uppercase is',name.upper())


# ---------------------------------------------------------------------
# Exercise 4: User Profile Creation
# Build a user profile generator. Ask
# the user for their first name, last name, and age. Create
# a profile summary using .title(), .upper(), and .format().
#
# Example Input:
# First name: john
# Last name: smith
# Age: 28
#
# Example Output:
# Name: John Smith
# Age: 28

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input(str("Enter your age: "))


print("Name: ", first_name.title(), last_name.title())
print("Age: " + age)




# ---------------------------------------------------------------------
# Exercise 5: Text message limits
# You are developing a text messaging application that limits the
# number of characters in a single message. Your task is to create
# a Python program that takes a message as input from the user.
# The program should calculate and display the number of characters
# in the message, including spaces, and format the output using
# an f-string. This character count will help users ensure their
# messages fit within the allowed limit.

message = input("Enter your message: ")
print(f"Your message is: {len(message)} spaces long")




# ---------------------------------------------------------------------
# Exercise 6: Text Transformation Game
# Create a text transformation game. Ask the user
# to enter a sentence. Replace all vowels with '*'. Display the
# modified sentence.
#
# Example Input: "Hello, world!"
# Example Output: "H*ll*, w*rld!"
sentence = input("Enter a sentence: ")
transformed_sentence = sentence.replace('a', '*')
print(f'Your entry:', sentence, 'New sentence:', transformed_sentence)


# ------------------------------# ---------------------------------------------------------------------
# Exercise 7: Extracting Information
# The variable 'data' is a student record in the format "name:age"
# Use string slicing and string methods to extract the name and the age
# and print the result formatted.
#
data = "lucy smith:28"
#
# Expected output:
# Name: Lucy Smith
# Age: 28

Name = data[0:10].title()
Age = data[11:]

print(f"Name:{Name}")
print(f"Age: {Age}")


# ---------------------------------------------------------------------
# Exercise 8: Miles to Kilometers Conversion
# Write a program that converts a distance in miles to kilometers.
# Take the distance in miles as input, convert it to kilometers
# using the formula miles * 1.6, and display the
# result using f-strings.

# Example Input: 10
# Example Output: 10 miles is approximately 16.0 kilometers.

# We are converting the input string to float:
# Input: float("1.23")
# Output: 1.23
miles = float(input("Enter distance in miles: "))
kilometers = miles * 1.6
print(f"{miles} miles is approximately {kilometers} kilometers")




# ---------------------------------------------------------------------
# Exercise 9: Workouts calculator
# Write a Python program that asks the user to input the number
# of minutes spent on three different exercises: cardio, strength
# training, and yoga using the input() function. Convert the input
# strings to integers using the int() function. Calculate the
# total time spent on workouts by summing up the minutes from all
# three activities. Based on the total workout time, provide a
# motivational message using an f-string that encourages the user
# to stay consistent and reach their fitness goals. Display the
# motivational message to the user.

cardio = int(input("Enter time in minutes: "))
strength = int(input("Enter your minutes: "))
yoga = int(input("Enter your minutes: "))

total_time = (cardio + strength + yoga)
print(f'Your total time is {total_time}! Keep up the good work!')


# ---------------------------------------------------------------------
# Challenge 1 (OPTIONAL!): Reverse the negative integer -324 and keep
# the negative symbol. Expected output: -423
input_number = -324

# Convert the integer to a string to handle the negative symbol separately
num_str = str(input_number)
reversed_num_str = num_str[::-1] # 423-
reverse_num = reversed_num_str[:3] #423
print(f'-{reverse_num}')


# Reverse the digits (excluding the negative symbol) using slicing [::-1]
# Use this simple guide to help you slice the reversed string:
# http://bit.ly/3siP47n

# (ADD YOUR CODE BELOW)

# Add the negative symbol back to the reversed string
# reversed_num = (num_str[0] + reversed_num_str)

# Output the result
# (ADD YOUR CODE BELOW)

num_str = str(input_number)
reversed_num_str = num_str[::-1] # 423-
reverse_num = reversed_num_str[:3] #423
print(f'-{reverse_num}')
-423

# ---------------------------------------------------------------------
# Challenge 2 (OPTIONAL!): Formatting Average Speed
# In this exercise, we're developing a program to determine the
# average speed of a truck based on the distance traveled in miles
# and the total time taken in hours. Your task is to format and display
# this average speed accurately.
# Task:
# Your program should take the number of miles and the total number
# of hours traveled as input and calculate the average speed. Then,
# present the average speed in a user-friendly format, rounded to one
# decimal place.
#
# Example:
# If the driver covered 60 miles in 3 hours, the calculated average
# speed is 20.0 miles per hour. However, we want to display it as
# 'The average speed is 20.0 miles per hour'.
#
# Similarly, for 55 miles and 3 hours, the calculated speed is
#  approximately 18.33333333332, but we want to format and display
#  it as 'The average speed is 18.3 miles per hour'.
#
# Hints:
# Refer to the "Format examples" section in the official Python
# documentation for string formatting techniques:
# https://docs.python.org/3/library/string.html#format-examples
# Experiment with different formatting options to achieve the
# desired presentation of the average speed.

# Taking input for miles and hours
miles = int(input("Enter the number of miles: "))
hours = int(input("Enter the total number of hours: "))

# Calculating average speed
average_speed = miles / hours

# Formatting and displaying the result
# (Your code here)
rounded_speed = round(average_speed, 1)

print(f"The average speed is {rounded_speed} miles per hour")





# ---------------------------------------------------------

 Homework Lesson 4 - Conditionals

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Temperature Classification
# You're developing a weather application. Write a program that takes
# a temperature in Fahrenheit as input. If the temperature is above
# 85°F, print "Hot day ahead!".
temperature = int(input("Enter the temperature in Fahrenheit: "))

# <Your code here>

if temperature > 85:
    print("Hot day ahead")

# ---------------------------------------------------------------------
# Exercise 2: Grade Classifier
# As a teacher, you want to automate grading. Write a program that
# takes a student's score as input and prints "Pass" if the score is
# 50 or above, otherwise print "Fail".
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.

# <Your code here>

score = int(input("Enter your score: "))

if score >= 50:
    print("Pass")
else:
    print("Fail")

# ---------------------------------------------------------------------
# Exercise 3: Scholarship Eligibility
# Your university offers scholarships based on academic performance.
# Write a program that takes a student's GPA as input. If the GPA
# is greater than or equal to 3.5, print
# "Congratulations, you're eligible for a scholarship!". If it's
# between 3.0 and 3.49, print "You're on the waiting list."
# Otherwise, print "Keep up the good work."
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.
# The function int() converts the number to an integer, and the function
# float() converts the number to a float.

gpa = float(input("Enter your GPA: "))

# <Your code here>

if gpa >= 3.5:
    print("Congratulations, you're eligible for a scholarship!")
elif gpa >= 3.0 and 3.49:
    print("You're on the waiting list.")
else:
    print("Keep up the good work.")


# ---------------------------------------------------------------------
# Exercise 4: Shopping Discount
# A store is offering a discount on a product. Write a program that
# takes the original price and the discount percentage as input.
# If the discounted price is less than $50, print "Great deal!".
# Otherwise, print "Might want to wait for a better offer."
original_price = float(input("Enter product original price: "))
discount_percentage = float(input("Enter discount percentage: "))
discount = original_price * discount_percentage / 100

discounted_price = original_price - discount


if discounted_price > 50:
    print("Great deal!")
else:
    print("Might want to wait for a better offer.")

# <Your code here>



# ---------------------------------------------------------------------
# Exercise 5: Movie Night Decision
# You and your friends are deciding on a movie to watch. Write a
# program that takes two movie ratings as input. If both ratings
# are above 7, print "Let's watch both!". Otherwise,
# print "Let's just pick one."

# <Your code here>

rating1 = int(input("Enter your first rating: "))
rating2 = int(input("Enter your second rating: "))

if rating1 and rating2 > 7:
    print("Let's watch both!")
else:
    print("Let's just pick one.")

# ---------------------------------------------------------------------
# Exercise 6: Restaurant Recommendation
# You're building a restaurant recommendation system. Write a program
# that takes a person's mood (happy or sad) and hunger level
# (high or low) as input. If they're happy and hungry, recommend
# a fancy restaurant. If they're sad and hungry, recommend comfort food.
# For other cases, recommend a casual dining place.

# <Your code here>

mood = input("Enter your mood, happy or sad: ")
hunger = input("Enter your hunger, high or low: ")

if mood == 'happy' and hunger == 'high':
    print("Try a fancy restuarant")
elif mood == 'sad' and hunger == 'high':
    print("Try comfort food")
else:
    print("Try a casual restuarant")

# ---------------------------------------------------------------------
# Exercise 7: Exercise 7: Tax Bracket Calculator
# You're building a tax calculation system. Write a program that
# takes a person's annual income as input. Use conditionals
# to determine their tax bracket based on the following rules:

# - If income is less than $40,000, tax rate is 10%.
# - If income is between $40,000 and $100,000 (inclusive), tax rate is 20%.
# - If income is greater than $100,000, tax rate is 30%.

# Remember that a tax rate of 10% can be represented as 10/100 or 0.1

# Print the calculated tax amount for the given income.
annual_income = float(input("Enter your annual income: "))

if annual_income > 100000:
    tax_rate = 30
    print(f'Your tax rate is {tax_rate}')

elif annual_income >=40000 and annual_income <= 100000:
        tax_rate = 20
        print(f'Your tax rate is {tax_rate}')
else:
    tax_rate = 10
    print(f'Your tax rate is {tax_rate}')
# <Your code here>
tax_amount = annual_income * tax_rate / 100
# Print tax amount

print(f"Your tax amount is ${tax_amount}")

# ---------------------------------------------------------------------
# Exercise 8: Ticket Pricing System
# You're working on a ticket booking system for an amusement park.
# Write a program that takes a person's age as input and determines
# their ticket price based on the following rules:
# - Children (ages 3 to 12): $10
# - Adults (ages 13 to 64): $20
# - Seniors (ages 65 and above): $15
# Print the calculated ticket price for the given age.

# <Your code here>

age = int(input("Enter your age: "))

if age >= 65:
    price = 15
    print("Ticket price is $", price)
elif age >= 13 and age < 65:
    price = 20
    print("Ticket price is $", price)
else:
    price = 10
    print("Ticket price is $", price)

# ---------------------------------------------------------------------
# Exercise 9: Password Strength Checker
# Create a program that takes a password as input and checks its
# strength based on the following rules:

# If the password is less than 8 characters, print "Weak password."
# If the password is 8 to 12 characters long, print "Moderate password."
# If the password is more than 12 characters, print "Strong password

# You can use len() function to get the length of a given string.

password = input("Enter your password: ")

if len(password) > 12:
    print("Strong password")

elif len(password) >= 8 and len(password) <= 12:
    print("moderate password")

else:
    print("Weak password")

# <Your code here>

# ---------------------------------------------------------------------
# CHALLENGE (OPTIONAL): Course Enrollment Eligibility
# To solve this exercise, you will need to use the following concepts
# and methods:
# - String method .upper()
# - String slicing
# - if-elif-else conditional statements
#
# You're designing a course enrollment system. Write a program that
# takes a course code and a student's grade as input and determines
# whether the student is eligible to enroll in the course.

# 1. Ask the user to enter a course code (e.g., "CS101", "MATH202", ).
#    All courses ends with "101", "202" or "303". Slice the string
#    to get the last three character of the string to get the course
#    ending:
#
#    Hint:
#    test = "ABCDEF"  # Given this string
#    print(test[-2:])  # It will print "EF"

# 2. Ask the user to enter their grade (e.g., "A", "B", "C", "D", "F").
#    Use .upper() method to convert the course code and grade to uppercase,
#    allowing for case-insensitive input.
#
# Implement the following enrollment rules:
# - For courses with course codes ending in "101", students with
#   grades "A" or "B" are eligible.
# - For courses with course codes ending in "202", students with
#   grades "B" or "C" are eligible.
# - For courses with course codes ending in "303", students with
#   grades "C" or "D" are eligible.

# Print either "You are eligible to enroll." or "You are not eligible to enroll."
course_code = input("Enter the course code: ")
student_grade = input("Enter your grade: ")

# Convert input to uppercase for case-insensitive comparison
course_code = course_code.upper()
student_grade = student_grade.upper()

# Extract the last three characters of the course code (use string slicing)
course_suffix =  course_code[-3:]# your code here

# Check course code and grade to determine eligibility
if course_suffix == "101" and student_grade == "A" or student_grade == "B":
    print("You are eligible")
elif course_suffix == "202" and student_grade == "B" or student_grade == "C":
    print("You are eligible")
elif course_suffix == "303" and student_grade == "C" or student_grade == "D":
    print("You are eligible")
else:
    print("You are not eligible to enroll.")




# ------------------------------------------------------

# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5

num = -3

if num < 0:
    num = num * -1
    print(f'{num} has been changed to positive')
else:
    print(f'{num} is already positive')
# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”

x = "BinGo"
y = "Bin"
z = "Go"

numb = 1978

if numb % 3 == 0 and numb % 7 == 0:
    print(x)
    if numb % 3 == 0:
        print(y)
        if numb % 7 == 0:
            print(z)


# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3


num_list = [7, 3, 5]
sorted_list = sorted(num_list)
print(sorted_list[1])





# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

palidrome = '121'
rev_palidrome = str(palidrome[::-1])

if palidrome == rev_palidrome:
    print(True)
else:
    print(False)


# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

full_review = 'tcefreP!'
rev_review1 = str(review[:-1])
rev_review2 = rev_review1[::-1]

print(rev_review2 + "!")


# --------------------------------------------------------------------


# Homework: Lists

# 🔥Read carefully until the end before you start solving the exercises🔥

# Practice the Basics 💪🏻

# Empty, Pre-populated, and Lists within Lists

# You can uncomment or type the necessary code on each task

# ---------------------------------------------------------------------
# Task 1. Create three lists:

# List #1: Create an empty list and then use append() to populate it with the names of three of your friends.
# List #2: Create the same list, but use the syntax to create it pre-populated.
# List #3: Create the same list, but each element should be a list,
# where the first sub-element is the friend's name
# and the second sub-element is their age.

# List 1:
list_1 = []
list_1.append('Friend1')
list_1.append('Friend2')
list_1.append('Friend3')

# List 2:
list_2 = ['Anthony', 'Sam', 'Wife']
friend1 = 'Anthony'
friend2 = 'Sam'
friend3 = 'Wife'

# List 3:
list_3 = [
    47,
    46,
    52,
]

# ---------------------------------------------------------------------
# Task 2. Retrieve elements from a List

# Create print statements to retrieve the following elements from the previous lists:
# - From List 2: Retrieve the name of the second friend.
# - From List 3: Retrieve the age of the last friend you put in the list.

# Name of second friend
second_friend_name = list_2[1]
print(second_friend_name)

# Age of the last friend of the list
last_friend_age = list_3[2]
print(last_friend_age)



# ---------------------------------------------------------------------
# Task 3. Remove elements from a List

# From the lists provided, remove the requested elements. Easy peazy.

cities = ["Houston", "Dallas", "Austin"]
fruits = ["apple", "banana", "orange"]

# Remove Austin from cities without using its index
cities.remove('Austin')
print(cities)

# Remove the last element from fruits using negative indexes
del fruits[-1]
print(fruits)



# ---------------------------------------------------------------------
# Task 4. Verify if an element exists in a list

# Given the provided list, write code that prints `YES` if the list contains the word `cheese`

# The list
pantry = ["ham", "bread", "cheese"]

# Write code that prints YES if the list contains "cheese".

if 'cheese' in pantry:
    print('YES')
else:
    print('NO')

# ---------------------------------------------------------------------
# Task 5. Sorting and Reversing

# Given the provided list, write code that sorts and reverses it, as required.

numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Write code that sorts the list in ascending order without disturbing the original.
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

# Write code that reverses (flips) the list without disturbing the original.
# Remember that in this case, casting is required.
reversed_numbers = list(reversed(numbers))
print(numbers)
print(reversed_numbers)

# Write code that sorts the list in place, modifying the original.
numbers.sort()

# Write code that reverses (flips) the list in place, modifying the original.
numbers.reverse()

# ---------------------------------------------------------------------
# Task 6. Stitching and Slicing

# You are given two lists with names of days of the week:

# - `work_days` contains the work week days (Mon-Fri)
# - `rest_days` contains the weekend days (Sat-Sun)

# Create a third list that contains the _concatenation_ of the previous two.
# Call it 'full_week'

# Now, write python code that prints a slice from 'full_week' with the work days.

work_days = ['mon', 'tue',  'wed', 'thu', 'fri']
rest_days = ['sat', 'sun']

# Concatenate work_days and rest_rays
full_week = work_days + rest_days
print(full_week)

# Slice with the work days
print(full_week[0:5])

# ---------------------------------------------------------------------
# Task 7. Aggregators and Helpers

# Given a list of numbers, use helpers and aggregators to answer the questions:

# - What's the lowest number?
# - What's the highest number?
# - What's the sum of all the numbers in the list?
# - How many times is the number 9 in the list?
# - How many total elements are in the list?

numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Lowest number
print(min(numbers))

# Highest number
print(max(numbers))

# Sum of everything
print(sum(numbers))

# Count number 9s
print(numbers.count(9))

# Total number of elements
print(len(numbers))

## Exercises 🏋🏻

# ---------------------------------------------------------------------
# Exercise 1. The Biography Creator

# Create a program that will ask you for the following items and stores them in a list for later usage:

# - Your Name
# - Your Age
# - The name of the city where you were born

# The program should use a variable with a string that will be used as a template.
# This template should be a sentence that can be used to build the person's biography.

# Fox example:

# biography = "My name is <NAME>, I'm <AGE> years old and I was born in <CITY>."

# Tips:
# - Use f-strings with placeholders to build the actual template, with elements of the list as values.
# - Use input() to gather the data.
# - Use print() at the end, to show the user's biography.

# Declare an empty list
user_data = []

# Gather user input
name = input("Name: ")
age = input("Age: ")
city = input("City: ")

# Add user input to the list
user_data.append(name)
user_data.append(age)
user_data.append(city)

# Declare your template. Use list elements as values.
biography = f"My name is {name}, I'm {age} years old and I was born in {city}."

# Show the user's biography
print(biography)

# ---------------------------------------------------------------------
# Exercise 2. The Card Deck ♦️♥️♠️♣️

# You will be provided with a couple lists that contain the cards for a card deck.
# One of the lists contains the numbers, and the other one contains the faces.

# You will be asked to fill in the blanks to print out certain cards for a card game you've been working on.

# 🔥 Tip: You might want to stitch them together first.

# Here are the card decks.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
faces = ['J', 'Q', 'K']

# Concatenate them first.
card_deck = numbers + faces

even = []
for i in (card_deck[:10]):
    if int(i) % 2 == 0:
        even.append(i)
print(even)
# Print out the numbers 1 to 6.
print(card_deck[0:6])

# Print out the last 3. Do it using POSITIVE indexes.
print(card_deck[7:10])

# Print out the last 3 (same as before), but using NEGATIVE indexes.
print(card_deck[-4:-7:-1])

# Print out everything EXCEPT the first and last.
print(card_deck[-2:0:-1]) # print(card_deck[1:12])

# What would you use so the printout includes the following:
# Hint: It's every third card of the full deck.
# ['1', '4', '7', '10', 'K']
print(card_deck[0::3])

# Print out the EVEN numbers. No faces.
even = []
for i in (card_deck[:10]):
    if i % 2 == 0:
        i += even
    print(even)

# ---------------------------------------------------------------------
# Exercise 3. The Steps Tracker 👟

# Walking is a great way to improve one's health, and it can be fun!
# Doctors recommend 10,000 steps per day! You would like to know how many steps are YOU taking per day and per week.

# Write a program that will ask you the number of steps taken each day of the week, for one week.
# The program should put the step counts in a list, where index 0 is the number for Monday,
# index 1 is the number for Tuesday, and so on.

# Once you have all the steps counts, answer the following questions:
# - How many steps you took on Wednesday?
# - How many steps you took on the work days (Mon - Fri)?
# - How many steps total did you take over the whole week?
# - What was the least number of steps you took on a day?
# - What was the most number of steps you took on a day?

monday = int(input('Steps for Monday: '))
tuesday = int(input('Steps for Tuesday: '))
wednesday = int(input('Steps for Wednesday: '))
thursday = int(input('Steps for Thursday: '))
friday = int(input('Steps for Friday: '))
saturday = int(input('Steps for Saturday: '))
sunday = int(input('Steps for Sunday: '))

steps = []

# Steps on Wednesday
steps.append(int(monday))
steps.append(int(tuesday))
steps.append(int(wednesday))
steps.append(int(thursday))
steps.append(int(friday))
steps.append(int(saturday))
steps.append(int(sunday))
print(steps)

# Steps on the work days
work_days_steps = steps[:5]

work_days_totals = sum(work_days_steps)

print(f'Work day total steps: {work_days_totals}')

# Steps over the whole week
print(f'All steps: ', sum(steps))

# Least number of steps
print(min(steps))

# Highest number of steps
print(max(steps))

# ---------------------------------------------------------------------
# Exercise 4. Bonus Round: The Speech Reverser and Counter 🎤

# Python has a handy little method that allows you to split a string.
# In its most basic form it splits a string into a list using the spaces as separators:

# Example:

# phrase = "My Name is Joseph"
# words = phrase.split()
# print(words) -> ['My', 'Name', 'is', 'Joseph']

# More information about split: https://www.w3schools.com/python/ref_string_split.asp

# Now, armed with `split()` write a program that does the following:

# - Takes a string input from the user.
# - Splits it into words.
# - Prints out the string with the words in reverse order.
# - Prints out the word count.

# Get input from the user
user_input = input('Give me a phrase')

# Split user input into words
words = user_input.split()
print(words)

# Reverse the list and print it
reversed_words = list(reversed(words))
print(reversed_words)

# Print the length of the words list
print(len(words))


----------------------------------------

# ----------LESSON 7-----------------

# Homework: Loops

# 🔥Read carefully until the end before you start solving the exercises🔥

# Practice the Basics 💪🏻

# You can uncomment or type the necessary code on each task

# ---------------------------------------------------------------------
# Task 1. Create a basic for loop

# Complete the following code in such a way that this loop prints the characters
# of `name` one at a time.

name = "Joseph"
looped_name = []

for i in name:
    looped_name += i
print(looped_name)

# ---------------------------------------------------------------------
# Task 2. Create a basic `for` loop with a counter

# Complete the following code in such a way that the loop increments the counter
# and prints the number of characters in `name`name at the end.

name = 'Tom'
counter = 0

for i in name:
    counter += 1

# This should print '3'
print(counter)

# ---------------------------------------------------------------------
# Task 3. Create a basic 'while' loop

# Complete the following code in such a way that the loop exits after five iterations, without using break.

# 🔥 Hint: Think of it as: while counter is under 5, increment the counter and print its value🔥

"""
This should print:
1
2
3
4
5
"""
counter = 1

while counter <= 5:
    print(counter)
    counter += 1

# ---------------------------------------------------------------------
# Task 4. Exit a loop using break 🛑

# Take the previous example, and modify it so you exit the loop after five iterations,
# but this time do it using break.

counter = 1

while counter <= 5:
    print(counter)
    counter = counter + 1

    if counter == 5:
        break


print(counter)

# ---------------------------------------------------------------------
# Task 5. Range

# Remember that range(start, end, step) behaves somewhat like list slicing, so start is inclusive,
# end is exclusive, and step is optional.

# Figure out the values required for range() to generate the expected output.

# 0, 1, 2, 3, 4, 5 (use only one argument)
for i in range(6):
    print(i)

# 0, 1, 2, 3, 4, 5 (use two arguments: start and end)
for i in range(0,6):
    print(i)

# Odd numbers between 0 and 10: 1, 3, 5, 7, 9
for i in range(1,11,2):
    print(i)
# ---------------------------------------------------------------------
# Task 6. Using range() in a loop

# Remember that range() returns an iterable, so you will usually find it used in a for loop.

# Complete the following code so it prints the even numbers between 0 and 10;

for i in range(2,11,2):
    print(i)


# Exercises 🏋🏻

# ---------------------------------------------------------------------
# Exercise 1. Digits Only!

# Part one: Given a string of letters and digits, complete the program to print only the digits.
# For example, for the string '3catsand5tacos', output should be: 3 5

# Strategy:
# - Create variable to hold the string: my_string = '3catsand5tacos'
# - Create a string to represent the numbers: numbers = '1234567890'
# - Create a loop to iterate through characters of my_string.
# - If the character is a digit (`if character in numbers`) print it.

my_string = 's0m3 str1ng w1th numb3r5'
numbers = '1234567890'
num_in_my_string = []

for i in my_string:
    if i in numbers:
        num_in_my_string.append(i)
print(num_in_my_string)

# Part two: Modify the code to print the first digit only
print(num_in_my_string[0])


# ---------------------------------------------------------------------
# Exercise 2. Vowel Counter

# Imagine you're working on a text analysis tool that needs to count the number of vowels in a given string.
# As a simple practice, you have been provided with a famous quote.
# Your task is to count and display the total number of vowels in this quote.

quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
vowels = "aeiouAEIOU"
vowel_count = 0

# 'A' and 'a' are different in python, so we include both upper and lowercase
# vowels in our comparison string to account for this difference.
for char in quote:
    if char in 'aeiouAEIOU':
        vowel_count += 1
print(f"The number of vowels in the quote is: {vowel_count}")

# ---------------------------------------------------------------------
# Exercise 3. Sum of all Digits 🔢

# You have a mixed string that contains both letters and numbers, like an alphanumeric password or
# a serial key. Your task is to find all the numbers in this string and sum them up.

# Hint: You can put the numbers you find into a list (cast as `int`) and use `sum()` on the list at the end.

mixed_string = "abc123xyz456"
digits = "0123456789"
found_digits = []

for char in mixed_string:
    if char in digits:
        found_digits.append(int(char))

print(f"The total sum of numbers in the string is: {sum(found_digits)}")

# ---------------------------------------------------------------------
# Exercise 4. Password Strength Checker

# You are helping to develop a user registration page for a website. As part of the registration process,
# you need to ensure that submitted passwords are strong. A strong password should have at least 8 characters.

# Create a Python program to check the strength of a list of passwords and count how many are strong.

passwords = ['Passw0rd', 'hello', 'strongPass1', 'weak']
strong_password_count = 0

for password in passwords:
    if len(password) >= 8:
        strong_password_count += 1

print(f"Number of strong passwords: {strong_password_count}")

# ---------------------------------------------------------------------
# Exercise 5. The Red Crayon 🖍️

# Imagine you have a box of crayons, and you're looking for a "Red" crayon.
# You pull out one crayon at a time from the box.

# Use a while loop to simulate this scenario.  As soon as you find the "Red" crayon, stop the loop.

colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]
index = 0

# This should basically say: while the current color being evaluated is
# different than "Red", increment to the next color and try again.
while colors[index] != "Red":

    if colors[index] == "Red":
        break
    print(f"Found {colors[index]} crayon. Still looking for Red.")
    index += 1

print("Found the Red crayon!")


-----------------------------------------------------------

# ------------PRACTICE LESSON LESSON 8-------------

# -----------SUM AND MULTIPLICATION--------

numbers = [1, 2, 3, 4]
sum_result = 0
multi = 1

for number in numbers:
    sum_result = sum_result + number
    multi = multi * number
print(sum_result)
print(multi)


# ------------REMOVE VOWELS------------

s = 'hello, world'
vowels = 'aeiou'
removed_vowels = ''
for i in s:
    if i not in vowels:
        removed_vowels = removed_vowels + i
print(removed_vowels)


# ----------ANAGRAM------------

str1 = 'cat'
str2 = 'tac'

if len(str1) != len(str2):
    print('False, String is not an anagram')
elif sorted(str1) == sorted(str2):
    print('True, String is an anagram')
else:
    print('String is not an anagram')

# ------------FACTORIAL--------------

f = 5
result = 1

for f in range(1, 6):
    result = result * f
    # result *= f
print(result)

# ---------MAX NUMBER-----------------

numbers = [1, 2, 42, 77, 99, -100]
result = numbers[0]

for number in numbers:
    if number > result:
        result = number
print(result)

# ---------FIBONACCI----------

n = 10
fib_sequence = [0, 1]

for i in range(2, n):
    next_fib_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib_number)
print(fib_sequence)

# -------------------------------------------------------------


# Homework Lesson 8 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Two Lowest Elements
#
# Your task is to write a program that takes a list of numbers and finds
# the two smallest numbers in it. The two smallest numbers can be equal to
# each other or different.
#
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
#
# Hint: Start with sorting the list

arr = [5, 2, 9, 1, 5, 6]
sorted_arr = sorted(arr)
print(sorted_arr[:2])



# Your code here

# ---------------------------------------------------------------------

# Challenge 2
# Remove Spaces
#
# Imagine, you're trying to organize your files, and you notice that one
# of your file names contains several spaces, which could lead to errors
# or difficulties in file management. Your task is to remove all the spaces
# from the given file name using a `for` loop.
#
# Hint: Loop through each character and check if a character is NOT a space.
# If it’s not, add the character to the new file name. This way, you will
# exclude all spaces.

file_name = "My Summer Photos 2023"
new_file_name = ""

for i in file_name:
    if i != ' ':
        new_file_name += i

print(new_file_name)


# You can use the replace() method to remove spaces in a more concise way. Here’s how you
# would modify the code using replace():

file_name = "My Summer Photos 2023"
new_file_name = file_name.replace(" ", "")
print(new_file_name)
# Explanation: file_name.replace(" ", "") replaces all spaces (" ") in file_name with an empty
# string (""), effectively removing them.


# ---------------------------------------------------------------------

# Challenge 3
# Sum of digits
#
# Compute the sum of digits in all numbers from 1 to 5.
# When the result gets a number n, find the sum of digits
# in all numbers from 1 to 5.
#
# Example: number = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# Initialize 'number' variable to 5. This is the number up to which we will calculate the sum.

# Initialize 'result' variable to 0. This variable will hold the sum.

# Iterate through the range starting from 1 up to 'number + 1'.

# Add the current value of 'i' to 'result'

# Print the sum of integers from 1 to 'number'

n = 5
result = []

for i in range(1,6):
    result = result + [i]
print(sum(result))
# ---------------------------------------------------------------------

# Challenge 4
# Isogram
#
# Write a Python program that checks if a given word is an isogram
# — an isogram is a word with no repeating letters, such as ‘cat’, ‘taco’, or ‘dog’.
#
# Example:
# For "cat", print True
# For "mom", print False
#
# Choose any word, you’d like to check.
# If it’s an isogram, print True. If it’s not an isogram, print False.
#
# Hints:
# Use a for loop to iterate over every letter and conditional statements to check the condition
# Use the count() method (think how it can help you solve this problem!)

word = 'cat'
is_isogram = True

for i in word:
    if word.count(i) > 1:
        is_isogram = False

if is_isogram:
    print("Isogram")
else:
    print("Not Isogram")

# ---------------------------------------------------------------------

# Challenge 5
# Repeat digits
#
# Given a string “312”, your task is to create a new string where each
# digit from the original string is repeated a number of times equal to its value.
#
#
# For the input string "312," your program should output "333122."
#
# Hints:
# To make a digit appear as many times as its value (like turning “3” into "333"),
# you have to multiply the string by a number.
# In Python, multiplying a string by a number repeats the string that many times.
# Since our digit is a string, we need to convert it to a number using int() so we can repeat it correctly.
# Once the digit is a number, just multiply the character by this value to get the repeated string.

# Initialize an empty string called 'result' to store the result

# Loop through each character in the string

# Inside the loop, turn the character into a number using int()
# and store it as a current_num variable

# Multiply the character by its number value
# and add the repeated character to 'result'

# Print the final result
string = "312"
result = ''

for i in string:
    result += i * int(i) # place strings before int
print(result)

# -----------------------------------------------



# HOMEWORK: Functions
# Read carefully until the end before you start solving the exercises.

# Basic Function
# Define a basic function that only prints Hello. Create the definition using def and the call that executes it.

def greeting():
    print(f"Hello")
greeting()


# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Parameters
# Define a basic function that prints a greeting taking a given name.

def parameter(name):
    print(name)
parameter('Anthony')





    # Bust a move right here

# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Default Values
# Define a basic function that prints a greeting for a name, but if none is given, use stranger instead of the name,
# so it behaves like this:

# Prints: Hello, stranger!
# greeting()

def greet(name):
    print("Hello, stranger")
    print("Hello", name)

greet('Anthony')

# Prints: Hello, Tom!
# greeting('Tom')

# ----------------------------------------------------------------------------------------------------------------------

# Multiple Parameters
# Define a function that takes two parameters, add them up and prints the sum.

# Prints: The sum of 1 + 2 = 3
# add(1, 2)
def add(num1, num2=0):
    result = num1 + num2
    print(f"The sum of {num1} + {num2} = {result}")

# Example 1: Passing both arguments
add(1, 2)  # Output: The sum of 1 + 2 = 3

# Example 2: Passing only one argument, the second one will default to 0
add(1)  # Output: The sum of 1 + 0 = 1

# ----------------------------------------------------------------------------------------------------------------------

# Parameters out of order
# Define a function that takes a first_name and a last_name and prints a full_name. Define the function and create
# the function call in such a way that first_name and last_name can be given in any order and the printed full_name
# would still be correct.

# Prints: Nelson Mandela
# full_name("Nelson", "Mandela")

# Is there anything you can add to the line below, so the function also prints "Nelson Mandela"?
# full_name("Mandela", "Nelson")

def full_name(first, last):
    full_name = f"{first} {last}"
    print(f"Hello {full_name}")

full_name("John", "Doe")
full_name(last="Smith", first="John")
# ----------------------------------------------------------------------------------------------------------------------

# Returning Values
# Define a validator function that you can use to determine if a word is longer than 8 characters.
# After creating the function, make sure to test it. Create a list of words and iterate over this
# list using a for loop.

# Tip: Validator functions return True / False which we can use in conditionals to do things like print a message.


def new_password(password):
    return len(password) > 8

passwords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', '135234nine']

for password in passwords:
    pass_length = len(password)
    if new_password(password):
        print(f'Password {password} length: {pass_length}, STRONG')
    else:
        print(f'Password {password} length: {pass_length}, WEAK')


# ----------------------------------------------------------------------------------------------------------------------

# You're going to revisit some of the algorithms you've already solved. But this time, there's a twist! Your challenge
# is to solve and encapsulate each algorithm into its own Python function. This will not only help you review these
# algorithms but also give you valuable practice in defining and using functions.

# FizzBuzz
# You remember FizzBuzz, right?
# You print Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both 3 and 5.

# Now, your task is to take your existing FizzBuzz code and wrap it into a function called fizzbuzz.

# Requirements:
# - Create a function named fizzbuzz that takes a single argument, number.
# - If the number is a multiple of both 3 and 5, the function should return: FizzBuzz
# - If the number is a multiple of 3, the function should return: Fizz
# - If the number is a multiple of 5, the function should return: Buzz
# - Otherwise, the function should return the number.

# Call the function here

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
            return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return (n)

print(fizzbuzz(5))

# ----------------------------------------------------------------------------------------------------------------------

# Anagram
# Your next challenge is to implement a function that checks if two given strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. For example,
# "listen" is an anagram of "silent".

# What You Need to Check
# - The two strings must have the same length.
# - The sorted form of the first string must be equal to the sorted form of the second string.

# Approach
# - Create a function that takes two strings as arguments.
# - Check if the lengths are equal. If they're NOT equal, return False (anagrams are always same length).
# - Sort both strings. If the sorted versions are equal, they're anagrams!

# Test your function with these strings
# test_str1 = 'abcde'
# test_str2 = 'edcba'

def is_anagram(test_str1, test_str2):
    if len(test_str1) != len(test_str2):
        return False
    return sorted(test_str1) == sorted(test_str2)

test_str1 = 'abcde'
test_str2 = 'edcb6a'

print(is_anagram(test_str1, test_str2))

# ----------------------------------------------------------------------------------------------------------------------

# Find Max number
# Create a function to find the largest number in a list without using the built-in max() function.

# - Define a function called find_max that takes a list of numbers as an argument.
# - Initialize a variable result and set it to the 1st item of the list using [0]
#   - This variable will hold the largest number as we iterate through the list.
# - Loop through each number in the list.
# - Check if number > result
#   - If it is, update result with the new greater number.
# - return result

# Define your function here
def find_max(numbers):
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result


# Test the function with a sample list of numbers.

numbers = [1, 2, 30, 4]

# Output should be the maximum number in the list.
print(find_max(numbers))

# ----------------------------------------------------------------------------------------------------------------------

# Even/Odd Checker Function
# Your task is to write a function that determines if a given integer is even or odd. The function should
# print Even for even numbers and Odd for odd numbers.

# What You Need to Check
# - Determine whether the input number is even or odd.
# - An even number can be exactly divided by 2 without a remainder.
# - An odd number leaves a remainder of 1 when divided by 2.

# Define a function is_even_odd(number) here

def is_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(float(input("Enter a number: ")))
is_even_odd(number)

# Test the function calling it using a variety of numbers like: 1, 10, 5.5, 9


# ---------------------------------------------------------------------

# -----SUM OF 3 DIGITS------------------

def sum_of_digits(number):
    result = 0

    while number > 0:  # Continue until all digits are processed
        result = result + (number % 10)  # Add the last digit
        number = number // 10  # Remove the last digit
    return result

number = 349

print(sum_of_digits(number))

#-----BELOW AVERAGE-----------

def below_arith_mean(arr):
     arith_mean = sum(arr) / len(arr)
     below_mean = []

     for i in arr:
         if i < arith_mean:
             below_mean.append(i)
     return below_mean

arr = [1, 2, 3, 4, 5]
print(below_arith_mean(arr))

# --------FIND MISSING ELEMENT---------


def missing_element(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[-1]

arr1: [1, 2, 3, 4, 5, 6, 7]
arr2: [3, 7, 2, 1, 4, 6]

print(missing_element(arr1, arr2))

# -----ALMOST A PALINDROME-----------
# Your function is_almost_palindrome is correctly designed to check whether a given
# string can be transformed into a palindrome by removing exactly one character.


def is_almost_palindrome(str1):
    for i in range(len(str1)):
        current_str = str1[:i] + str1[i + 1:]# Removes the character at index i
        if current_str == str1[::-1]:# Check if the modified string is a palindrome
            return True
    return False

str1 = 'rakdar'
print(is_almost_palindrome(str1)) #Output: False

# word = 'radkar' #
# print(word[:0]) # makes an empty list
# print(word[1:]) # prints out all after the first letter 'adkar'

def to_camel_case(text):
    # Split by underscores
    words = text.split('_')
    # Capitalize each word and join them together
    camel_case_text = ''.join(word.capitalize() for word in words)
    return camel_case_text

# Example
text = 'To_Camel_Case'
print(to_camel_case(text))  # Output: "ToCamelCase"


# components = snake_str.split('_')
# for component in components:
#     snake_str = snake_str.replace(component, '')
# print(components)


to_camel_case(components[0])

# ----BEST TIME TO BUY AND SELL STOCK------

def buy_and_sell_stock(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            max_profit = max_profit + prices[i+1] - prices[i]
    return max_profit

prices = [10, 20, 10, 20, 30]
print(buy_and_sell_stock(prices))



# Homework Lesson 10 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Multiplication of a three-digit number
#
# A program gets a three-digit number and has to multiply all its digits.
# For example, if a number is 349, the code has to print the number 108, because 3*4*9 = 108.
#
# Hints:
# Use the modulus operator % to get the last digit.
# Use floor division to remove the last digit

def multiplication_of_three(number):
    result = 1

    while number > 0:  # Loop until all digits are processed
        result = result * (number % 10)  # Multiply by the last digit
        number = number // 10  # Remove the last digit
    return result

number = 349
print(multiplication_of_three(number))
# Your code here


# ---------------------------------------------------------------------

# Challenge 2
# Sum and multiplication of even and odd numbers.
#
# You are given an array of integers. Your task is to calculate two values: the sum of
# all even numbers and the product of all odd numbers in the array. Please return these
# two values as a list [sum_even, multiplication_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].

def sum_even_and_product_odd(arr):
    sum_even = 0
    product_odd = 1

    for i in arr:
        if i % 2 == 0:
            sum_even += i
        else:
            product_odd *= i

    return sum_even, product_odd

arr = [1, 2, 3, 4]
print(sum_even_and_product_odd(arr))

# -------ALTERNATIVE CODE----------------

def sum_even_and_product_odd(arr):
    sum_even = 0
    product_odd = 1
    has_odd = False  # To track if we have any odd numbers

    for i in arr:
        if i % 2 == 0:  # Correct condition for even numbers
            sum_even += i
        else:  # Correct condition for odd numbers
            product_odd *= i
            has_odd = True

    if not has_odd:  # If no odd numbers were found, return 0 for product
        product_odd = 0

    return [sum_even, product_odd]

arr = [1, 2, 5, 4]
print(sum_even_and_product_odd(arr))  # Output: [6, 5]





# ---------------------------------------------------------------------

# Challenge 3
# Invert a list of numbers
#
# Given a list of numbers, return the inverse of each. Each positive becomes a negative,
# and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]

def invert_list(arr):
    inverted_list = []

    for i in arr:
        i *= -1
        inverted_list.append(i)

    return inverted_list


arr = [1, 5, -2, 4]
print(invert_list(arr))

#--------ALTERNATIVE CODE-----

def invert_list(arr):
    return [-i for i in arr]

arr = [1, 5, -2, 4]
print(invert_list(arr))



# ---------------------------------------------------------------------

# Challenge 4
# Difference between
#
# Implement a function that returns the difference between the largest and the
# smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
#
# Example:
# Input: [3, 5, 7, 2]
# Output: 7 - 2 = 5

def max_diff(arr):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    # If the list is not empty,
    # proceed with the rest of the code.

    # Your code here
    if len(arr) == 0:
        return 0
    else:
        sorted_list = sorted(arr)
        result = sorted_list[-1] - sorted_list[0]
    return result

arr = [3, 5, 7, 2]
print(max_diff(arr))






# ---------------------------------------------------------------------

# Challenge 5
# Sum between range values
# You are given an array of integers and two integer values, min and max.
# Your task is to write a function that finds the sum of all elements in the
# array that fall within the range [min, max], inclusive.
#
# Example:
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)
#
# Hint:  Iterate through each number (num) in the array (arr) and check if the current number  falls within the range [min_val, max_val].

def sum_between_range(arr, min_val, max_val):
    sorted_arr = sorted(arr)
    new_arr = 0
    short_arr = []
    for i in sorted_arr:
        if i >= min_val and i <= max_val:
            short_arr.append(i)
            new_arr += i

    return f'{new_arr}, {short_arr}'

arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
print()
print(sum_between_range(arr, min_val, max_val))

# --------BETTER CODE---------

def sum_between_range(arr, min_val, max_val):
    new_sum = 0
    filtered_arr = []

    for i in arr:
        if min_val <= i <= max_val:  # Check if i is within the range
            filtered_arr.append(i)
            new_sum += i  # Add to sum

    return new_sum, filtered_arr  # Return the sum and the filtered list

arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7

# Print the result
result_sum, result_list = sum_between_range(arr, min_val, max_val)
print(f'Sum: {result_sum}, Numbers in range: {result_list}')


# ------------------LESSON 11---------------------------------------------

def process_word(word):
    letters = {}
    for char in word:
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1

    print(letters)

def word_processor():
    while True:
        word = input('Enter a word: ')

        if word == 'end':
            break

        process_word(word)


word_processor()

# HOMEWORK: Dictionaries
# Read carefully until the end before you start solving the exercises.

# Basic Dictionary

# Create an empty dictionary and then add a few of your friends. Make the key their email (can be fake)
# and the value their name. When you're done, create the same dictionary as a pre-populated dictionary.

friends = {}
friends['ak@gmail.com'] = 'Anthony',
friends['sk@gmail.com'] = 'Bob',
friends['tk@gmail.com'] = 'Tara',

print(friends)


friends = {
    'ak@gmail.com': 'Anthony',
    'sk@gmail.com': 'Bob',
    'tk@gmail.com': 'Tara',
}

print(friends)


# ----------------------------------------------------------------------------------------------------------------------

# Nested Dictionary

# Create a nested dictionary for a list of 5 company employees.
# The key should be their employee id (an integer from 1-5 will do)
# and the value should be a dictionary with
# the name, department and salary of the employee.

company ={
    1: {
        "name": 'Anthony',
        'department': 'shoes',
        'salary': 150000,
    },
    2: {
        'name': 'Bob',
        'department': 'dress',
        'salary': 20000,
    },
    3: {
        'name': 'Joe',
        'department': 'mens',
        'salary': 30000,
        },
    4: {
        'name': 'Rick',
        'department': 'dress',
        'salary': 20000,
    },
    5: {
        'name': 'Bob',
        'department': 'dress',
        'salary': 20000,
    }
}
def print_employee_info(company):

    for employee_id, details in company.items():
        name = details['name']
        salary = details['salary']
        print(f'Name: {name}, Salary: {salary}')

print_employee_info(company)
# ----------------------------------------------------------------------------------------------------------------------

# Accessing Values

# Use the previous nested dictionary and write some print statements that
# will answer the following:

# - Print a list of the employee IDs
# - Print the employee data for employee with the ID 3.
# - Loop over the employees and print all their names and salaries.

print(company.keys())
print(company[3])
def print_employee_info(company):

    for employee_id, details in company.items():
        name = details['name']
        salary = details['salary']
        print(f'Name: {name}, Salary: {salary}')

print_employee_info(company)

# ----------------------------------------------------------------------------------------------------------------------

# Updating Values

# We have the following dictionary with employee salaries.

salaries = {
    'james' : 10000,
    'tom' : 15000,
    'ryan' : 16000,
    'julia' : 17000
}

# We need to increase everyone's salary by 1,000 and also add a new employee
# joseph with a salary of 18,000.
# Please come up with a way to do this using update()

for employee in salaries:
    salaries[employee] += 1000

# Use update() to add a new employee 'joseph' with a salary of 18,000
salaries.update({'joseph': 18000})

# Print the revised salaries
print(salaries)

# ----------------------------------------------------------------------------------------------------------------------

# Deleting Values

# You remember those employees from Updating Values section?
# Well, Julia got fired, so we need to remove her
# name from the salaries dictionary. How would you do that?

del salaries['julia']
# ----------------------------------------------------------------------------------------------------------------------

# Iterating over Dictionaries

# Given the list of movies below, please use view objects (keys(), values(), items() -
# where necessary) to answer
# the questions:

# - Is Black Panther in the list of movies?
# - Is there any movie for the year 2021?
# - Print a message for each element that shows the year,
# the title and the position in the dictionary (1-5).
#   Hint: use a counter.

films = {
   2016: "Star Wars: Episode VII - The Force Awakens",
   2017: "Star Wars: Episode VIII - The Last Jedi",
   2018: "Black Panther",
   2019: "Avengers: Endgame",
   2020: "Bad Boys for Life"
}
if "Black Panther" in films.values():
    print(f'Yes, "Black Panther" is in the list of films')
else:
    print(f'No, "Black Panther" is not in the list of films')

counter = 1
for year, title in films.items():
    print(f'{counter}: Year: {year}, Title: {title}')
    counter += 1

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 1. Animal Shelter Volunteer

# You volunteer in a local animal shelter and you've stored information
# about different pets in a Python dictionary.
# Your task is to create a Python program that helps you:

# - Access the age of specific pets by their names.
# - Find out which pets are not yet adopted.
# - Identify the most common animal type in the shelter (e.g., dog, cat).

# Pre-code
# Initialize the shelter_pets dictionary
shelter_pets = {
  'Whiskers': {'Age': 2, 'Type': 'Cat', 'Adopted': False},
  'Fido': {'Age': 4, 'Type': 'Dog', 'Adopted': True},
  'Patch': {'Age': 1, 'Type': 'Dog', 'Adopted': False},
  'Snowball': {'Age': 3, 'Type': 'Rabbit', 'Adopted': True}
}
#
print(shelter_pets['Whiskers']['Age'])  # Should output 2
# #
# # # # Access and print if Patch is a dog or cat
print(shelter_pets['Patch']['Type'])
# # #
# # # # Access and print if Snowball is adopted or not
print(shelter_pets['Snowball']['Adopted'])
#
# # Find out which pets are not yet adopted and print their names

def if_not_adopted(shelter_pets):
    for pet, info in shelter_pets.items():
        if not info['Adopted']:
            print(f'{pet} is not adopted')

if_not_adopted(shelter_pets)


def most_common_animal(shelter_pets):
    print('Most common animal')
    for pet, types in shelter_pets.items():
        animal_count = {}  #create a dictionary to count types
        # this is what the new dictionary looks like
        # animal_count = {
        #                   'Cat': 1,
        #                   'Dog': 2,
        #                   'Rabbit: 1'
        #               }
        # }
        animal_type = types['Type'] #create a variable for the types
        if animal_type in animal_count: #from created dictionary
            animal_count[animal_type] += 1 #counts the animal types in the dictionary
        else:
            animal_count[animal_type] = 1 #

most_common =  max(animal_count, key=animal_count.get)
#example of the .get() method and how it works for dictionaries not lists
# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# # Retrieve value for key 'b'
# print(my_dict.get('b'))  # Output: 2
print(f'{most_common} is the most common pet')

most_common_animal(shelter_pets)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Best - selling books

# Create a Python program to manage a collection of best-selling books
# and their publication years. Your initial list of best-selling books may have inaccuracies
# or could be outdated. Therefore, you'll also practice updating single and multiple entries
# in your dictionary. Specifically, you will:

# - Update the title of a book for a specific year due to a naming convention change.
# - Update the titles for multiple books at once based on new sales data.
# - Delete a book and its year from the collection as it's no longer considered a best-seller.
# - Print the title of the book published in a specific year.

# Pre-code:
# Initialize a dictionary called best_selling_books to store your collection.

best_selling_books = {
  1997: "Harry Potter and the Philosopher's Stone",
  1984: "Neuromancer",
  2003: "The Kite Runner",
  2015: "Go Set a Watchman"
}

# The U.S. title for the Harry Potter book published in 1997 is "Harry Potter and the Sorcerer's Stone".
# Update the title to its U.S. version.
best_selling_books[1997]  = "Harry Potter and the Sorcerer's Stone"

# New sales data reveals that "The Hunt for Red October" was the actual best-seller for 1984
# and "The Da Vinci Code"  for 2003.
# Update these in a single operation.

best_selling_books.update({
  1984: "The Hunt for Red October",
  2003: "The Da Vinci Code"
})
print(best_selling_books)

# The book published in 2015, "Go Set a Watchman," is no longer considered a best-seller.
# Use the del keyword to remove this entry from the dictionary.

del best_selling_books[2015]

# Print the updated dictionary of best selling books.
print(best_selling_books)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Manage Music Collection
# Create a Python program that manages a collection of music albums and their release years.
# You will use a dictionary where the keys are the release years and the values are the
# names of albums.
# The program should allow you to:

# - Print all the release years (keys) from the dictionary.
# - Print all the album names (values) from the dictionary.
# - Print both the release years and album names together.
# - Check if a particular year or album exists in the collection.


# Steps and pre-code
# Initialize a dictionary to store Bob Dylan's albums
dylan_albums = {
  1962: "Bob Dylan",
  1963: "The Freewheelin' Bob Dylan",
  1975: "Blood on the Tracks",
  1997: "Time Out of Mind"
}

# Use .keys() to loop through and print out all the release years
for year in dylan_albums.keys():
    print(year)

# Use .values() to loop through and print out all the album names
for album in dylan_albums.values():
    print(album)

# Use .items() to loop through and print out both the release year and album name
for year, album in dylan_albums.items():
    print(year, album)

# Use the 'in' keyword to check if a particular year or album is in the dictionary (pick any year and any album)
# Remember the keyword by default checks only the keys, not the values.

for year, album in dylan_albums.items():
    if year == 1963:
        print(year, album)

# If you want to check if a particular value (in this case, an album name),
# you need to specify that you're searching within the dictionary's values.

for year, album in dylan_albums.items():
    if album == 'Time Out of Mind':
        print(year, album)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. Remove duplicates
# Remove duplicates from the following dictionary:
person = {
  'first': 'Jeff',
  'name': 'Jeff',
  'last': 'Smith',
  'last_name': 'Smith',
  'state': 'CA',
  'age': 55
}

# Steps:
# - Create a dict person
# - Create an empty dictionary result = {}
# - Make a for loop to iterate over person dictionary
# - If item’s value not in result dict, add key value part into result.
result = {}
for key, value in person.items():
    if value not in result.values():
        result[key] = value
print(result)

# ---------or-------------

def updated_person(person):
    result = {}
    for key, value in person.items():
        if value not in result.values():
            result[key] = value
    print(result)

updated_person(person)

# ----------------------------------------------------------------------------------------------------------------------
# Exercise 5. Find the highest score
# Create a Python function named find_max_score that takes a dictionary of names and scores as an argument.
# The function should return the name and score of the person with the highest score in the form of a dictionary.

# Sample test_scores dictionary
test_scores = {
  'James': 83,
  'Julia': 91,
  'Ryan': 90,
  'Maria': 80,
  'David': 79,
  'Adam': 96,
  'Jennifer': 97,
  'Susan': 77
}

#  Find the person with the highest test score and display both their name and score

# Steps:
# - Define a function called find_max_score that takes one argument, scores_dict,
# which is a dictionary of names
#   (as keys) and scores (as values).
# - Create an empty result variable
# - Assume the initial maximum score is 0
# - Iterate over each key-value pair in the test_scores, using the .items() method
# - Check if the current score (v) is >= to the current maximum score
# - If so, update the max score and assign the key-value pair to the result
# - Return result and test the function

def find_max_score(scores_dict):
    result = {}
    max_score = 0
    for key, value in scores_dict.items():
        if value >= max_score:
            max_score = value
            result[key] = value
    return result

highest_score = find_max_score(test_scores)
print(highest_score)

# ---------EXPLANATION OF THE ARGUMENT scores_dict--------
# How the Function Works
# 1.Function Argument:
#         The function is defined to accept an argument named scores_dict.
#         This means that when you call the function, you can provide any dictionary that
#         contains names (as keys) and scores (as values).
#
# 2.Iterate Over scores_dict:
#         The for key, value in scores_dict.items(): line allows you to loop through
#         all key-value pairs in the dictionary you pass in. This makes the function
#         flexible, as it does not depend on a specific dictionary but rather works
#         with whatever dictionary you provide.

# Summary
# The function find_max_score can take any dictionary of scores as an argument, allowing
# it to be reused with different data.
#
# It iterates over the passed dictionary using scores_dict.items(), making it adaptable
# and flexible to handle various input scenarios.
#
# This design is a fundamental principle of programming: writing functions that can
# work with different inputs helps create reusable and maintainable code!




# --------------------------LESSON 12----------------------------------------------


class Animal:
    def __init__(self, name,):
        self.name = name

    def greeting(self, name):
        print(f"Hello {name}, I'm {self.name}")

class Dog(Animal):
    def greeting(self, name):
        print(f'Hello {name}, my name is {self.name} and I\'m a dog')

class Cat(Animal):
    def greeting(self, name):
        print(f'Hello {name}, my name is {self.name} and I\'m a cat')

dog = Dog('Fido')
dog.greeting('Anthony')
cat = Cat('Sushi')
cat.greeting('Anthony')




# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

# - Create an empty class HouseForSale
# - Create two instances.
# - Add number_of_rooms and price as instance attributes.
# - Create print statements that show the attribute values for the instances.

class HouseForSale:
    pass

house1 = HouseForSale()
house2 = HouseForSale()


house1.number_of_rooms.room = '4'
house1.price = '10k'

house2.number_of_rooms.room = '6'
house2.price = '100k'

print(f'House 1 {house1.number_of_rooms} and cost is {house1.price}')
print(f'House 2 {house2.number_of_rooms} and cost is {house2.price}')

# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.
# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
# - Create an instance of the Computer class then call each method.

class Computer:
    def turn_on(self):
        print("Turning on")

    def turn_off(self):
        print("Turning off")

comp1 = Computer()
comp2 = Computer()

comp1.turn_on()
comp2.turn_off()

# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.
# - Dog should have a method say_name that prints the name of the dog.

class Dog:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'Hello {self.name}')

dog = Dog('Bob')
dog.say_name()


# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.

# animal = Animal()
# animal.say_name()   # Prints: I don't have a name yet.
# animal.speak()      # Prints: I can't speak!
#
# dog = Dog('Fido')
# dog.say_name()      # Prints: Fido
# dog.speak()         # Prints: Woof!
#
# cat = Cat('Max')
# cat.say_name()      # Prints: Max
# cat.speak()         # Prints: Meow!

class Animal:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def speak(self):
        print("I can't speak!")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")


# Example usage
# You now need to provide a name for Animal as well
animal = Animal('NoName')
animal.say_name()  # Prints: NoName
animal.speak()  # Prints: I can't speak!

dog = Dog('Fido')
dog.say_name()  # Prints: Fido
dog.speak()  # Prints: Woof!

cat = Cat('Max')
cat.say_name()  # Prints: Max
cat.speak()  # Prints: Meow!

# ------------OR------------------

class Animal:
    def __init__(self, name=None):
        self.name = name

    def say_name(self):
        if self.name:
            print(self.name)
        else:
            print("I don't have a name yet.")

    def speak(self):
        print("I can't speak!")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")


# Example usage
animal = Animal()  # No name provided
animal.say_name()  # Prints: I don't have a name yet.
animal.speak()  # Prints: I can't speak!

dog = Dog('Fido')
dog.say_name()  # Prints: Fido
dog.speak()  # Prints: Woof!

cat = Cat('Max')
cat.say_name()  # Prints: Max
cat.speak()  # Prints: Meow!

# ----------------------------------------------------------------------------------------------------------------------
# Exercises
# Exercise 1: Books and Authors

# Create an empty class called Book. Then create three instances.
# Add the following attributes for each of the instances: title, author, and publication_year.
# Create print statements to display the attributes of each one of the instances.

# Pre-code:
class Book:
   pass

book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication_year = 1960

book2 = Book()
book2.title = 'Bible'
book2.author = 'Anthony Kittles'
book2.publication_year = 1990

book3 = Book()
book3.title = 'Birds'
book3.author = 'Thomas Terrell'
book3.publication_year = 1990

# Your code here

print(book1.title, book1.author, book1.publication_year)
print(book2.title, book2.author, book2.publication_year)
print(book3.title, book3.author, book3.publication_year)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"
# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.

class Vehicle:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_type(self):
        print(f'{self.name}, {self.type}')

class Car(Vehicle):
   pass

class Bike(Vehicle):
   pass

car = Car('Ford','focus')
bike = Bike('Harvey','bike')

bike.show_type()
car.show_type()


# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

# Pre-code
class Car:
   def __init__(self, model, year): # added self parameter
       self.model = model # fixed self with self.model
       self.year = year # fixed year with self.year

my_car = Car("Toyota", 2024) # added year argument

print(my_car.model)
print(my_car.year)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
#
# send_notification() should print a notification including the home_name and location.

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices

# Call the send_notification() method for each instance,
# passing a message reminding to turn off the lights.

class SmartHome:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices

    def send_notification(self):
        print(f'Home: {self.home_name}| Location: {self.location}| Num of devices: {self.number_of_devices}')
        print('TURN OFF YOUR LIGHTS')

home1 = SmartHome('Villa Rosa', 'New York', 15)
home2 = SmartHome('Green House', 'California', 10)
home3 = SmartHome('Sea View', 'Florida', 20)

home1.send_notification()
home2.send_notification()
home3.send_notification()

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name, age):
        self.name = name # added self to name
        self.age = age # added self to age

class Mammal(Animal): # changed Animals to Animal
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs
        print(f'Name: {self.name}, age: {self.age}, num_legs: {num_legs}')# Added print statement

class Bird(Animal):
    def __init__(self, name, age, can_fly): # corrected constructor to accept name and age
        super().__init__(name, age)  # calls Animal's constructor
        self.can_fly = can_fly
        print(f'Is a bird that can fly: {self.can_fly}') # Added print statement

class Fish(Animal): # changed parameter from Mammal to Animal
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins
        print(f'Name: {self.name}, age: {self.age}, num_fins: {num_fins}')# Added print statement

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird(True)
goldfish = Fish('Goldfish', 2, 'Many')


# -----------------------LESSON 13-------------------
# --------------------INTERVIEW QUESTIONS-------------

# ----NESTED LOOPS

adj = ["red", "ripe", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for j in fruits:
        print(i, j)

# ----LIST OF RECIPES (CHECKING INVENTORY/MEMBERSHIPS)

def make_recipe(recipe, ingredient):
    makeable_recipes = []

    for recipe in recipes:
        can_make = True

        for ingredient in recipe:
            if ingredient not in ingredients:
                can_make = False
                break

        if can_make:
            makeable_recipes.append(recipe)
    return makeable_recipes

recipes = [["yeast","flour"],["bread","meat"],["flour","meat"]]
ingredients = ["yeast","flour","meat"]

result = make_recipe(recipes, ingredients)
print(result)


# ------TWOSUM (CHECKING MEMBERSHIP)

num = [1,2,3,7,5]
target = 10


def two_sum(arr, target):
    if len(arr) < 2:
        return

    sum_dict = {}
    for num in arr:
        partner = target - num

        if partner not in sum_dict:
            sum_dict[num] =  num
            # print(sum_dict)

        else:
            return (partner, num)


result = two_sum(num,target)
print(result)

# Breakdown:
# Left side (sum_dict[num]):
    # This part means you're creating or updating an entry in the sum_dict dictionary where
    # the key is num. For example, if num = 3, it adds or updates the dictionary to have an
    # entry with 3 as the key.
#
# Right side (num):
#    This is the value that you're storing in the dictionary for the key num. In this case,
#    you are storing the number itself as the value, so if num = 3, you are essentially
#    storing {3: 3} in the dictionary.

# if added print function to 2nd block of code, this is the output of the sum_dict
                            # {1: 1}
                            # {1: 1, 2: 2}
                            # {1: 1, 2: 2, 3: 3}
                            # (3, 7)
# -----REAL LIFE USAGE

# Why would you do this?
    # In this specific scenario, the value being stored (num) isn’t being used for anything.
#   The dictionary is more about checking the existence of numbers (using the keys) rather
#   than the values. Using True or None as the value is more common in situations like this
#   where you just want to check for membership.

# -------MOUNTAIN ARRAY-------

def is_mountain_array(arr):
# Check the increasing sub-array
    i = 1
    while i < len(arr) and arr[i - 1] < arr[i]:
        i += 1
    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i - 1] > arr[i]:
        i += 1
    if i == len(arr):
        return True

    return False

arr = [3,4,5,7,3,2]
result = is_mountain_array(arr)

print(result)

# ---REAL LIFE USAGE

# Website Traffic Monitoring:
# Websites may experience traffic spikes followed by declines
# (e.g., during events or promotions). Detecting a "mountain" pattern in visitor numbers
# can help marketing teams analyze the impact of campaigns or product launches.
# If traffic rises sharply and falls, it might indicate the end of interest in an event
# or sale.

# Product Sales Trends:
# For businesses monitoring product sales, a "mountain" pattern could represent a
# popular product launch. The initial rise could show a sharp increase in sales after
# a release, followed by a gradual decrease once demand has been satisfied.

# -------MOVE ZEROS--------

def move_zeros(arr):
    i = 0
    for num in arr:
        if num != 0:
            arr[i] = num
            i = i + 1

    while i < len(arr):
        arr[i] = 0
        i = i + 1

    return arr

result = move_zeros([0, 4, 0, 3, 12])
print(result)
# Output: [4, 3, 12, 0, 0]


# index also means position in the array
# Code also goes through for loop before getting to the while loop

# Initial list: [0, 4, 0, 3, 12]

# i starts at 0.

# Iteration 1 (num = 0):
# num is 0, so it doesn't do anything.
# i remains 0.
# The list remains unchanged: [0, 4, 0, 3, 12].

# Iteration 2 (num = 4):
# num is 4 (non-zero), so it replaces arr[0] with 4.
# i is incremented to 1.
# The list is now: [4, 4, 0, 3, 12] (The first zero has been replaced by 4).

# Iteration 3 (num = 0):
# num is 0, so it doesn't do anything.
# i remains 1.
# The list remains unchanged: [4, 4, 0, 3, 12].

# Iteration 4 (num = 3):
# num is 3 (non-zero), so it replaces arr[1] with 3.
# i is incremented to 2.
# The list is now: [4, 3, 0, 3, 12].

# Iteration 5 (num = 12):
# num is 12 (non-zero), so it replaces arr[2] with 12.
# i is incremented to 3.
# The list is now: [4, 3, 12, 3, 12].

# At the end of the for loop, the list is: [4, 3, 12, 3, 12], and i = 3.
#
# Now, the while loop will take over to fill the remaining spots with zeroes:
#
# While Loop Iterations:
# arr[3] = 0, now the list is [4, 3, 12, 0, 12].
# arr[4] = 0, now the list is [4, 3, 12, 0, 0].
# Finally, the output is [4, 3, 12, 0, 0].

#-----USAGE---------

# A real-life scenario for this code could be managing a warehouse or inventory system
# where you're shifting important items to the front and pushing unimportant or
# unavailable items (represented by zeros) to the back.
#
# For example, imagine you have a list of items in a warehouse where non-zero values
# represent available stock, and zeros represent items that are out of stock. The system
# might want to rearrange the list so that available stock is prioritized at the front of
# the list, making it easier for warehouse workers to pick from.
#
# The move_zeros function in this context would "move out-of-stock items to the back"
# while keeping available stock in the front.

# ---------------------------------------------------



# Homework Lesson 13 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Common Elements Finder

# Given two lists of integers, find and return a new list containing elements
# that appear in both lists.
# Make sure the resulting list does not contain duplicates.

# Example:

# Input:
# List 1: [1, 2, 3, 4, 5]
# List 2: [4, 5, 6, 7, 8]
# Output: [4, 5]

# Hints:
# You'll need to use nested loops: The outer loop will iterate over elements in the first list,
# and the inner loop will check if that element exists in the second list.
# Keep track of the common elements found so far to ensure no duplicates are added to the resulting list.
# To ensure no duplicates are added to the resulting list,
# check if an element is already present in the "common" list before appending it.

def find_common_elements(list1, list2):
    common = []
    for i in list1: #The outer loop will iterate over elements in the first list
        if i in list2: #the inner loop will check if that element exists in the second list
            common.append(i)
    return common

List1 = [1, 2, 3, 4, 5]
List2 = [4, 5, 6, 7, 8]

result = find_common_elements(List1, List2)
print(result)



# ---------------------------------------------------------------------

# Refresher
# One of the key skills during job interviews
# is to be able to modify the code you've created.
# The following two tasks are the extension of the recipe problem you solved in class.

# Let's refresh the problem you solved in the class.
# You have a list of recipes, where each recipe contains the ingredients each recipe needs:
# recipes = [
# ["yeast","flour"],
# ["bread","meat"],
# ["flour","meat"]
# ]

# Solution
def find_makeable_recipes(recipes, ingredients):
    makeable_recipes = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe:
            if ingredient not in ingredients:
                can_make = False
                break
        if can_make:
            makeable_recipes.append(recipe)
    return makeable_recipes


test_recipes = [["yeast", "flour"], ["bread", "meat"], ["flour", "meat"]]
test_ingredients = ["yeast", "flour", "meat"]
test_result = find_makeable_recipes(test_recipes, test_ingredients)
print(test_result)


# ---------------------------------------------------------------------

# Challenge 2
# Missing ingredients

# You have a new list of recipes and ingredients.

# recipes = [
# ["yeast", "flour"],
# ["bread", "meat", "flour"]
# ]

# ingredients = ["yeast","bread"]

# Return the list of missing ingredients for all the recipes.

# Output: ["flour","meat"]


def find_missing_ingredients(recipes, ingredients):
# Create an empty list to store the missing ingredients
    missing_ingredients = []

# In the outer loop iterate through each recipe in the list of recipes.
    for recipe in recipes:
        can_make = True

# In the inner loop check each ingredient in the recipe.
        for ingredient in recipe:

# Check if the ingredient is not in the list of available ingredients
# and is not already in the list of missing ingredients.
            if ingredient not in ingredients and ingredient not in missing_ingredients:
# If both conditions are met, add the ingredient to the missing_ingredients list.
                missing_ingredients.append(ingredient)
# Return the list of missing ingredients required for all the recipes.
    return missing_ingredients

recipes = [
["yeast", "flour"],
["bread", "meat", "flour"]
]

ingredients = ["yeast","bread"]

results = find_missing_ingredients(recipes, ingredients)
print(results)


# ---------------------------------------------------------------------

# Challenge 3
# The best recipe

# You have a new list of recipes, where each recipe contains the ingredients it needs.

# recipes = [
# ["yeast","flour"],
# ["bread","meat"],
# ["flour","meat", "yeast"]
# ]

# You also have a list of available ingredients.
# ingredients = ["yeast","flour", "meat", "salt"]

# Return the list of the best recipe (the one that uses most of ingredients).

# Output: ["flour","meat", "yeast"]


def find_best_recipe(recipes, ingredients):
    # Initialize variables to remember the best recipe and the most ingredients used.
    best_recipe = None
    max_used_ingredients = 0

    # Create an outer for loop to go through each recipe in the list of recipes.
    for recipe in recipes:

    # Create an empty list (used_ingredients) to store the ingredients we can use from this recipe.
        used_ingredients = []
    # Create an inner foor loop to look at each ingredient in this recipe.
        for ingredient in recipe:

    # Check if the ingredient is in our list of available ingredients.
            if ingredient in ingredients:

    # If it's available, add it to our list of used ingredients.
                used_ingredients.append(ingredient)

    # Check if the current recipe uses more ingredients (using `len` to count)
    # than the highest count we've recorded so far (max_used_ingredients).
            if len(recipe) > max_used_ingredients:

    # If the current recipe has a higher ingredient count, update max_used_ingredients.
    # Then set this recipe as the new best.
                max_used_ingredients += 1
                best_recipe = recipe
    # Finally, return the best recipe that uses the most ingredients.
    return best_recipe
    # Define the list of recipes and available ingredients.
recipes = [
["yeast","flour"],
["bread","meat"],
["flour","meat", "yeast"]
]
ingredients = ["yeast","flour", "meat", "salt"]
    # Call the function to find the best recipe and print the result.
result = find_best_recipe(recipes, ingredients)
print(result)


# ---------------------------------------------------------------------

# Challenge 4
# Find a peak element
# You are given an array of integers, and your goal is to find a "peak" element in the array.
# A peak element is an element that is strictly greater than its adjacent elements
# (elements on the left and on the right).

# Write a Python function find_peak_element(arr) that takes an array of integers as input
# and returns the index of the peak element in the array.

# Handle edge cases:
# - If the array has fewer than three elements, return -1.

# Check each element in the array:

# - If an element is strictly greater than both its adjacent elements (if they exist),
# consider it a peak element.
# - Return the index of the first peak element you find.
# - If no peak elements are found, return -1.

# Example:
# arr1 = [1, 3, 20, 4, 1, 0]
# result1 = find_peak_element(arr1)
# print(result1)  # Output: 2 (Peak element: 20)

# arr2 = [1, 2, 3, 4, 5]
# result2 = find_peak_element(arr2)
# print(result2)  # Output: -1 (No peak elements)

# arr3 = [5, 10, 20, 15]
# result3 = find_peak_element(arr3)
# print(result3)  # Output: 2 (Peak element: 20)


def find_peak_element(arr):
    n = len(arr)  # Find out how many elements are in the array

    # Check for the edge case (less than 3 elements)
    if n < 3:
        return -1  # If the array has fewer than 3 elements, it's impossible to have a peak

    # Check the first and last element separately as they don't have neighbors
    # Check the first element (only has a right neighbor)
    if arr[0] > arr[1]:
        return 0

        # Check the last element (only has a left neighbor)
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # Iterate over the range, excluding the first and last indices, as they lack one neighbor.
    for i in range(1, n - 1):
        # find out if the current index is > previous index and if the current index is > next index
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i

    # Return -1 # if no peak element is found.
    return -1  # If the array has fewer than 3 elements, it's impossible to have a peak


arr1 = [1, 3, 20, 4, 1, 0]
result1 = find_peak_element(arr1)
print(f'Peak element is {result1} is {arr1[result1]}')

# Created by Owner at 10/31/2024



# ---------------------------------------------------------------------

 # Challenge 5 (optional)
# Delete duplicates in sorted lists

# Given a sorted list of integers, write a program that:

# - Removes all duplicate values from the list.
# - Shifts the unique values to the left to fill any emptied indices.
# - Fills the remaining rightmost indices with zeroes.
# - Returns the count of unique values in the list.

# - Example:
# Input: [1, 2, 2, 3, 4, 4, 4, 5]
# Output: [1, 2, 3, 4, 5, 0, 0, 0], 5 (5 unique values)

# Hints:
# - Sequential Comparison: Since the list is sorted, duplicates will always be adjacent to each other.
# Compare each element to the previous one to detect duplicates.
# - Updating in Place: You can modify the original list as you find unique numbers
# and move them to the correct position. Think of this position as where the next unique number should go.

def delete_duplicates(arr):
    if not arr:
        return arr, 0
# 'write_index' points to where the next unique element should be written.
    # Start at index 1, since the first element is always unique in a sorted array.
    write_index = 1

# Iterate over the list's length, starting from the second element because
# the first element doesn't have a previous element to compare against.

# Compare the current element with its immediate previous element.

# If they're different, it's not a duplicate.
# Place the current element at the 'write_index' position.

# Then increment 'write_index' by 1 to prepare for the next unique element.

# Once you have shifted all unique elements to the left,
# fill the remaining positions in the list with zeroes.
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]: # If the current element is not a duplicate (different from the previous one),
            arr[write_index] = arr[i] # move it to the position pointed to by 'write_index'.
            write_index += 1

        # After placing all unique elements, fill the rest with zeroes.
    for i in range(write_index, len(arr)):
        arr[i] = 0
    # Return the modified array and the number of unique elements (write_index).
    return arr, write_index

result, unique_count = delete_duplicates([1, 2, 2, 3, 4, 4, 4, 5])
print(result, unique_count)

# Return the modified list for visualization and the count of unique elements.