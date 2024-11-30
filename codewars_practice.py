


# create an interger variable for x
# x = 5
# # create an interger variable for y
# y = 3
# # put x and y in sum
# sum = x + y
# # tell user the answer
# print(sum)


# # ---------------------------------------------
#
#
# # Task: separate the url

# def sep_url(url):
#     new_url =
#     return new_url
#
#
# #
# url = 'www.codewars.com#about'
#
# print(sep_url(url))

# ----------------------------

# Write a method (or function, depending on the language) that converts a string to camelCase,
# that is, all words must have their first letter capitalized and spaces must be removed.

# join the words and Capitalize each word in words
# think, camel case equals capitalizing each word and joining them

# Split by underscores or spaces

# DID I GET IT RIGHT THE FIRST TIME? NO
# def to_camel_case(text):
#     words =
#     camel_case_words =
#     return camel_case_words
#
#
# print(to_camel_case('camel_case_word'))  # Outputs: "CamelCaseWord"

# --------Alternative where it doesnt capitalize the first word-----------

# def to_camel_case(text):
#     words = text.split('_') # 'camel' '_' 'case'
#     camel_case_words = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
#     return camel_case_words
#
#
# print(to_camel_case('camel_case_word'))

# # Hint: use .split() .join() and .capitalize() methods to capitalize and join the words separately.
#
# # -------------------------------------------------------
#
# # Task:
# # Given a list of integers, determine whether the sum of its elements
# # is odd or even.
# #
# # Give your answer as a string matching "odd" or "even".
# #
# # If the input array is empty consider it as: [0] (array with a zero).
# #
# # Examples:
# # Input: [0]
# # Output: "even"
#
# # Input: [0, 1, 4]
# # Output: "odd"
# #
# # Input: [0, -1, -5]
# # Output: "even"
# #
#
# def check_sum(x, y, z):
#     sum = x + y + z
#
#
#
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# z = int(input("Enter the third number: "))
#
# print(check_sum(x, y, z))

# -----------------------------------
#
# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls
# comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.
# def remove_vowels(comment):
#     vowels = "aeiouAEIOU"
#
# #     # Use list comprehension to filter out vowels
# #     # hint: join char for char in the comment if the char is not in vowels
#     comment =                                                                                                                                                                          ;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O;O.;;;OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#     #
#     return comment  #
#
#
# # # # Test the function
# print(remove_vowels("This website is for losers LOL!"))  # Output: "Ths wbst s fr lsrs LL!"

# ---------------------------------------------
# Create a function that removes the elements from a string and puts them in a list


# def is_vowel(word):
# #     # create local variables
#     vowels = "aeiouAEIOU"
#     for :
#']         if :
#             word =
#
#     return word
#
#
# # # # test case
# word = 'anthony'
# #
# print(is_vowel(word))
#
# -----------------------------------------


# def descending_order(numerals):
#     #call the reverse to be true to put it in reverse order
#
#     return numerals
#
#
# numerals = [1, 2, 3, 455, 5, 6, 7, 8, 9]
# print(descending_order(numerals))


# ------------- LESSON 5 INTERVIEW ALGORITHMS--------------------------
#
# How do we solve algorithm problems
#
# Understand a problem. Get an idea of
# what we need to do. Typically, every
# detail is needed to solve the problem.
#
# Use an example to make sure that you
# understand it correctly.
#
# Come up with a brute force algorithm
# (consider all possible solutions).
#
# Optimize (optional)
#
# Walk through your algorithm
#
# Code
#
# Test


# Create a variable called number. Set it to
# any number.
# Convert the number to negative and print it.
# Keep the number as is, if the number is
# already negative. 5 minutes
#
# Input: 5 => output: -5
# Input: -1 => output: -1

#       ###### NEW FUNCTION abs() ######

# def negative_abs(num):
#     """Returns the negative absolute value of a number.
#
#   Args:
#     num: The input number.
#
#   Returns:
#     The negative absolute value of the input number.
#     The absolute value of a positive number is the number itself.
#     The absolute value of a negative number is its opposite (the positive version).
#     The absolute value of 0 is 0
#
#     Write the return code using absolute value (always returns a negative number).
#   """
#     return
#
#
# num = int(input("Enter a number: "))
# print(negative_abs(num))


#----------what is the old code----------

# def number(num):
#     if :
# #       num =
# #       return num
# #   else:
# #     return
#
# #
# #
# # # Take input from the user
# num = int(input("Enter a number: "))
# # # Print the result from the function
# print(number(num))


# ----------------------------------------
# The largest of three 5 minutes

# 1. Assign values to three variables a, b, and c
# 2. Set if, elif and else statements to check if
# the valuables are larger than the other two
# 3. Feel free to use and operator to compare
# one variable with the other two
#
# 4. If the largest number is a, print a
#
# Find the max number from 3 values.
#
# Example: 124, 21, 32
# Result = 124

# def largest_number(a, b, c):
#
#
# #
# #
# a = 124
# b = 21
# c = 32
#
# print(largest_number(a, b, c))

# -------------------------------------

# Leap year 7 minutes

# Your goal is to decide if a given year is a leap year. A leap year is divisible by 4,
# except for centuries (divisible by 100) which must also be divisible by 400.

# Use modulus division to check if a number is divisible by 4, 100 and 400
# 1. Take user’s input for a year to check
# 2. Create if else conditions to check if it’s a leap year
# 3. First of all, check if the year is divisible by 4
#
#  If it’s divisible by 4, also check if it’s divisible by 100
#  If it’s divisible by 100, check if it’s divisible by 400
#
# year = int(input("Enter a year: "))

# A year is a leap year if it is divisible by 4
# but not by 100, unless it is also divisible by 400
#
# A year is # says the variable, year =
# leap year if it is divisible by 4 # says if year is % 4
# but not by 100 # says year is also not 100
# unless it is also % 400 # says

# def is_leap_year(year):
#     if
#         return 'Leap Year'
#     else:
#         return 'Not Leap Year'
#
#
# year = int(input('Enter a year: '))
# print(is_leap_year(year))

# ----------------------------------------------

# Slice a String 3 minutes

# s[start:end:step]

#  0  1  2  3  4
#  A  B  C  D  E
# -5 -4 -3 -2 -1

# How many right the last time? 11 out of 11

# s = "ABCDE"
# s[1:2] -?
# s[1:] - ?
# s[::2] - ?
# s[2:] - ?
# s[-2:] - ?
# s[:-2] - ?
# Output: ABC -? s[]
# Output: DE - ? s[]
# Output: ACE - ? s[]


# ----#### notice s[::2] and s[::-2] gets the same results
# meaning the start:end:step needs to be read that way not "goes
# backwards" way

# -----------------------------------------

# Reverse String 3 minutes

# s[start:end:step]

#  0  1  2  3  4 # START AT 3 AND GO TO 1
#  A  B  C  D  E # -1 MEANS THE STEPS ARE BACKWARDS
# -5 -4 -3 -2 -1

# Example
# reversed_string = s[3:1:-1] # Output: DC

#               OR

# see it, the -1 FIRST reverses s[] NOT the nums position
# [3:1] tells you to read it actually as [1:3] its -1,
# so picture s[3:1:-1] as s[1:3] since the s[] was reversed.

# O  1  2  3  4 # START AT 1 AND GO TO 3
# E  D  C  B  A
# -5 -4 -3 -2 -1

# Positive Indices:  0    1    2    3    4
# Characters:        A    B    C    D    E
#
# Negative Indices: -5   -4   -3   -2   -1
# Characters:        A    B    C    D    E

# reversed_string = s[3:1:-1] # Output: DC

# s = "ABCDE"
# s[2::-1] - ?
# s[:0:-1] -?
# Output: CB - ? s[]
# Output: BA- ? s[]
# ?
# ?
# s[]
# s[]

# How many right the last time? 0 out of 4

# -------------------------------


# Reverse integer 10 minutes
#
# Given an integer, return the integer with reversed digits.
#
# Note:
# Before reversing, the integer could be either positive or negative.
#
# After reversing:
# The negative integer should remain negative2
# The positive integer should remain positive.
#
# Example:
# -876 -> -678
# 876 -> 678

# 1. Convert the integer to a string to work
# with individual digits.
# string = str(n)
#
# 2. Create a condition to check if the first
# character of the string is a negative sign ('-').
# if string[0] == '-'
#
# 3. If the condition is true, reverse the string
# (excluding the negative sign) and convert the
# reversed string back to an integer with the
# negative sign. Concatenate it with a negative sign (‘-’)
#
# 4. If the integer is positive, reverse the entire string.

# n = int(input("Enter an integer: "))
# s = str(n)
# if s[0] == '-':
#     s =
# #     #split from '-' and get the [1] position then join a reverse string
#     print('-' + s)
# else:
#     s = s[::-1]
#     print(s)

# -----------------------------------------

# Palindrome 7 minutes

# A palindrome is a word, number, phrase,
# or other sequence of symbols that reads
# the same backwards as forwards:
#
# madam -> madam
# Racecar -> racecar
# Tacocat -> tacocat
#
# Write a program that will print True if the
# word is a palindrome and False if it is not.

# 1. Reverse the word
#
# 2. Compare the original and the reversed
# words
#
# word = 'tacocat'


# Reverse the word


# Check if the word is the same as this word backwards
# if
# print(True)
# else:
# print(False)

# What is the one-liner code?
#
# word = 'tacocat'
# print()

# --------------LESSON 8 INTERVIEW QUESTIONS--------------------------------


# Given a list.  5 MINUTES
#
# Calculate sum and multiplication
# of all elements.
#
# Print the list, sum and multiplication of
# elements.
#
# For example:
#
# Input: [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24

# numbers = [1,2,3,4]
#
# sum_result = 0
# mult_result = 1

# for number in numbers:
# Your code here

# ---------------------------------

# Anagram: steps   7 MINUTES
#
# Create two strings:
#
# str1 = 'cat'
# str2 = 'act'
#
# • Check if the lengths of the input strings s1 and s2 are
# the same. If the lengths are different, it means that the
# strings cannot be anagrams. Use the function. len()
#
# • Now that we know length is the same, compare the
# sorted string, using the function. sorted()

# ------------------------------------------

# Factorial: approach  5 MINUTES
#
# The factorial is a mathematical operation that
# involves multiplying a given whole number by
# all the whole numbers less than it down to 1.
#
# Factorial of 5 is equal to:
# 5! = 1 * 2 * 3 * 4 * 5
#
# Count the factorial for
# the following:
# 4!
# 3!

# 1. Set the initial result to 1 because multiplying by zero will result in zero.
#
# 2. Then, in each iteration multiply the result from the previous
# iteration by the current number.

# 1. Start with a variable result and set it to 1. This
# is our starting point for the multiplication.
# result = 1
#
# 2. Use a for loop to go through the range from 2
# up to n+1. Remember, the function
# doesn’t include the last digit so we add +1.
#
# range()
#
# 3. Inside the loop, multiply result by the current
# number (i) and update result.
#
# 4. After the loop finishes, we print out the final
# value of result, which is the factorial of n.

# number = 5
# result = 1

# for

# ---------------------------------

# Find Max number: code 5 MINUTES
#
# 1. Create a list: numbers = [1, 2, 42, 77, 99, -100]
#
# 2. Create a variable result and set it to the 1st item of the list
# result = numbers[0]
#
# 3. Create a loop to iterate over every number in the numbers and
# if number > result, set result to number
#
# 4. Print the result

# ----------------------------------------

# Fibonacci
#
# The Fibonacci sequence is a series of
# numbers where each number is the sum of
# the two preceding ones.
#
# Print out the Fibonacci sequence until the
# given n-th in the sequence.
#
# Example: ,
# Print out the sequence:
#
# n = 7
#
# 0, 1, 1, 2, 3, 5, 8
#
# Fibonacci Sequence
#
# Default
#
# 0 1 1 2 3 5 8
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8

# Fibonacci: code
#
# 1. Set the number of Fibonacci numbers you
# want to generate
# n = 10
#
# 2. Initialize the list with the first two Fibonacci
# numbers
# fib_sequence = [0, 1]
#
# 3. Calculate the next Fibonacci number
# next_fib_number fib_sequence[-1] + = fib_sequence[-2]
#
# 4. Append the new Fibonacci number to the list
# using the function append()

# n = 10
# fib_sequence = [0, 1]

# for
#     next_fib_number = fib_sequence[-1] + fib_sequence[-2]


# -----------FINAL LESSON INTERVIEW ALGORITHMS-------------
#
################## Nested loops #####################

# THINK----> if there only 1 list
#               for element in list (outer loop)
#                 for the same element in list (inner loop)
#                   print out both results until done with list
#
#      ----> if there is multiple list
#               for element in first list
#                   for element in second list
#                       print out both results until done with list


# Let’s imagine we have a list lst = ["a", "b", "c"].
# You want to print all possible two-character combinations.
#
# Output: aa, ab, ac, ba, bb, bc, ca, cb, cc
#
# lst = ["a", "b", "c"]

# 2nd example
# Create a Python script that generates a simple
# multiplication table for numbers ranging from 1 to 10.

# USE RANGE()


# -----------------------------------
#
# Create a Python script that generates all possible
# combinations of given adjectives and fruits. Practice 5 minutes
# 5 MINUTES
#
# adj = ["red", "ripe", "tasty"]
# fruits = ["apple", "banana", "cherry"]



# ----------------------------------------

# 1. You have a list of recipes, where each recipe contains the ingredients each recipe needs:
#
# recipes = [
# ["yeast","flour"],
# ["bread","meat"],
# ["flour","meat"]
# ]
#
# 2. You also have a list of available ingredients.
#
# ingredients = ["yeast","flour","meat"]
#
# 3. Return a list of all recipes that can be made with the ingredients you have.
#
# Output: [["yeast","flour"], ["flour","meat"]]

# 10 MINUTES

# A list of recipes: code
#
# • Initialize an empty list to hold recipes that can be made
# with available ingredients
# • Loop through each recipe in the recipes list (outer loop)
# • Assume initially that the recipe can be made
#
# can_make = True
#
# • Loop through each ingredient in the current recipe
#
# (inner
# loop). If an ingredient is not available, mark the recipe as
# unmakeable
#
# • Break out of the inner loop as one missing ingredient is
# enough to make the recipe unmakeable
# • If all ingredients for the recipe are available, add it to the
# makeable_recipes list

# recipes = [["yeast","flour"],["bread","meat"],["flour","meat"]]
#
# ingredients = ["yeast","flour","meat"]
#
# def makeable_recipes(recipes, ingredients):
# Your code here


# ----------------------------------------

# TwoSum

# Given an array of integers, and an integer target, return
# two numbers such that they add up to target.
# Assume there’s only one unique pair of numbers that
# will sum up to the target and you may not use the same
# element twice.
#
# You can return the answer in any order.
#
# Example:
# Input: nums = [1, 2, 3, 7, 5], target = 10
# Output: [3, 7]

# TwoSum: code
# def two_sum(arr, target):

# • Check if the array has fewer than 2 elements. If yes,
# return None.
#   if len(arr) < 2:
#     return

# • Create an empty dictionary called 'sum_dict to keep
# track of numbers we've already seen as we go through
# the array.


# • Loop through 'arr', using 'num' to represent each number.

# • Calculate the 'partner' as 'target - num'.

# • If 'partner' is not in 'sum_dict', add 'num' to it.


# If 'partner' is in 'sum_dict', return the pair [partner, num].

# • If loop ends without finding a pair, the function implicitly
# returns None.---THIS ALSO IN THE FIRST LINE OF CODE ALREADY

# ------------------------------------------------------------

# Mountain Array
# You’re given an array.Find if givenarray is in a
# form of mountain or not.
#
# There exists some index i such that:
# arr[0] < arr[1] < ... < arr[i]
# arr[i] > arr[i + 1] > ... > arr[-1]
#
# Basically, find if there is an increasing subarray
# followed by a decreasing subarray
# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true
#
# The length of the list is longer or equal to 3.
#
# Mountain array: approach
#
# 1. First, go through the numbers and check
# if each next number is larger than the one
# before it. This identifies the climb up the
# "mountain."
# Once this pattern breaks, it assumes a peak
# has been reached.
#
# 2. After finding the peak of the "mountain,"
# check for a decreasing sequence, where
# each next number is smaller than the
# previous one. This checks the descent down
# the mountain.
#
# Mountain array: first loop
#
# To solve this task, we are going to use 2
# while loops.
#
# In the first while loop, iterate over the list as
# long as:
# • each number arr[i] is bigger than the one
# before it arr[i-1]
# • you haven’t reached the end of the list
# len(arr)
#
# After the loop, check if i is at the start i == 1
# or the end i == len(arr) of the list. In this case,
# the pattern isn't a mountain, return False.
#
# Mountain array: write the second loop
#
# In the second while loop, keep increasing i
# as long as you're not at the end of the list i
# < len(arr) and each number arr[i] is smaller
# than the one before it arr[i-1].
#
# • After this loop, if i is at the end of the list i
# == len(arr), then the list forms a mountain.
#
# • If this condition is not met, it means the
# loop was terminated before reaching the
# end of the list, which implies the list is not a
# mountain. Function returns False.
#
# 7 minutes
#
# def is_mountain_array(arr):
# # Check the increasing sub-array
# i = 1
# while i < len(arr) and arr[i - 1] < arr[i]:
# i += 1
# if i == 1 or i == len(arr):
# return False
# Check the decreasing sub-array
# Your code here


# --------------------------------

# Move Zeros: approach • Start Point: Pick the first spot in the list
# to place non-zero numbers [i].
#
# • Scan List: Go through each number from
# start to end.
#
# • Move Non-Zeros: If a number isn't zero,
# move it to the spot you originally picked.
# If it’s a zero, don’t do anything.
#
# • Next Spot: After you move a non-zero,
# move the spot for the next non-zero one
# step to the right.
#
# 'i' marks where to place the next non-
# zero number.
#
# Default i = 0
#
# Move Zeros: approach
#
# 1. Fill in Zeros: Once you've looked at every
# number, you'll have a spot that tells you
# where the non-zeros end. Fill in zeros
# from this spot to the end of the list.
#
# 2. Finished List: At this point, all zeros will
# be at the end, and the other numbers will
# be at the beginning in their original order.
#
# Move zeros: code
#
# 1. Initialize a variable 'i' to 0 to track where to place non-zero numbers.
# 2. Using a for loop go through each number in the list 'arr'.
# 3. Check if the current number is not zero.
#
# If it's not, place it at the index 'i'
#
# in the list arr[i] = num.
# 4. Increase 'i' by 1. That’s where you will put the next non-zero number.
# 5. After checking all the numbers, 'i' will point to where the non-zeros end
# and where zeros should start.
#
# 6. To fill in zeros, use a 'while' loop that runs as long as i < len(arr). This means
# the loop will go from the current 'i' value up to the last spot in the list.
# 7. Again, increase 'i' by 1 to fill the next position with zero.
# 8. Done! The list now has all the zeros at the end, and you can return it.
#
# 10 minutes
#
# def move_zeros(arr):
# # Your code here
#

# __________________________________________________
