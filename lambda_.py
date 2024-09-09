import os

# Python Program to find numbers divisible
# by thirteen from a list using anonymous
# function

# Take a list of numbers.
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

# use anonymous function to filter and comparing
# if divisible or not
result = list(filter(lambda x: (x % 13 == 0), my_list))

# printing the result
print(result)

x = lambda a : a + 10
print(x(5))

