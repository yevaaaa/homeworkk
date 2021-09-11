"""
Problem 1
You have a list, you want to iterate over it and return the numbers that are divisible by 5.
If you iterate over a number larger than 500, stop the loop.
"""

# ls = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]

# for num in ls:
#     if num % 5 == 0:
#         print(num)
#     elif num > 500:
#         break

"""
Problem 2
Create a loop to print the reverse of a list. 
"""
# list1 = [1, 2, 3, 4, 5]
# list1.reverse()
# print(list1)

"""
Problem 3
Write a function to get a number and return the factorial of the number. Use loops. 
ex. factorial of 5 is 1*2*3*4*5
You can't count factorial of negative numbers, and the factorial of 0 is 1. 
"""

# num = int(input('Input a number: '))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers.")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num , "is", factorial)

"""
Problem 4
Write a code that would print list items that are at even positions. 
ex. in list = [10, 11, 12], 10 is at index 0, 11 - index 1 (odd), 12 - index 2 (even)
Use loops.
"""

list2 = [1, 2, 3, 4, 17, 24, 38, 45, 50, 64, 79, 82, 91]

# for i in list2:
#     if list2.index(i) % 2 == 0:
#         print(i)

"""
Problem 5
Write a function that gets a list of names and returns the ones that start with A.
Notice that some list items begin and end with spaces, or start with @. Get rid of space and @ before printing the name.
"""
names = [' Anna', "Lily", " Anahit ", "@Bob", "@Ani@", " Luiza@", "@@Armen"]
#
# for x in names:
#     x = names.strip("@")
# print(names)

"""
Problem 6
Write a program that checks if a number is prime (պարզ) or not. Try not to google. :) 
"""
# number = int(input("Input a number: "))
#
# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")
# else:
#     print(number, "is not a prime number")

"""
Problem 7 (OPTIONAL)
Write a loop that will print this pattern
* 
* * 
* * * 
* * * * 
* * * * *

Hint: print("\r") -> for printing on a new line, 
      print('*', end=' ') -> for printing on the same line

"""
#
# def func(x):
#     for i in range(0, x):
#         for i in range(0, i+1):
#             print("*", end="")
#         print("\r")
# x = 5
# func(x)
