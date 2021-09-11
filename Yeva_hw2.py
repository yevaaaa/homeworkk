# HOMEWORK 3

# Problem 1
# Create a program to check if a number entered by a user is even or odd.
# Use input() function to save user's input.



# n = input("Input your number: ")
# print(type(n))
# n = int(n)
# if n % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd")




# Problem 2
# Create a program to check if the number is divisible by 3.


# num = input("Input the number: ")
# print(type(num))
# num = int(num)
#
# if num % 3 == 0:
#     print("The number is divisible by 9.")
# else:
#     print("The number is NOT divisible by 9.")


# Problem 3
# Write a program that allows user to enter their grade and tells them which letter they got.
#  Grade                       Letter Grade
#  > 95                             A
#  85 - 95                          B
#  65 - 84                          C
#  < 65                             D


# x = input("Enter your grade: ")
# print(type(x))
# x = int(x)
#
# if x > 95:
#     print("Your letter grade is A.")
# elif x >= 85 and x <= 95:
#     print("Your letter grade is B.")
# elif x >= 65 and x < 84:
#     print("Your letter grade is C.")
# elif x < 65:
#     print("Your letter grade is D.")
# else:
#     print("Wrong input")



# Problem 4.
# Create a program that takes a number (1-7) from user and returns a day of the week.
# Like 1 for Monday, 2 for Tuesday, etc.



# x = input("Input the number: ")
# print(type(x))
# x =  int(x)
# if x == 1:
#     print("Monday")
# elif x == 2:
#     print("Tuesday")
# elif x == 3:
#     print("Wednesday")
# elif x == 4:
#     print("Thursday")
# elif x == 5:
#     print("Friday")
# elif x == 6:
#     print("Saturday")
# elif x == 7:
#     print("Sunday")
# else:
#   print("Wrong input")



# Problem 5
# Create a program that tells if a person can get a driving license or no.
# Required age for driving license is 17.
# If they are older than 17, check the score of their test (which can be from 0 to 10).
# If the score is 9 or 10, they get a license, if it is less than 9 they don't get a license.


# age = input("Input your age: ")
# print(type(age))
# age = int(age)
#
# score = input("Input your score: ")
# print(type(score))
# score = int(score)

# if age > 17 :
#     if score == 9 or score == 10:
#         print("Congratulations! You can get a license.")
# elif score > 10 :
#     print("Invalid score")
# else:
#     print("Sorry.You can't get a licence.")


# Problem 6
# Write a program that takes 2 numbers from the user and prints the smaller one.


# n1 = input("Input the first number: ")
# print(type(n1))
# n1 = int(n1)
#
# n2 = input("Input the second number: ")
# print(type(n2))
# n2 = int(n2)
#
# if n1 > n2:
#     print(n2)
# elif n1 < n2:
#     print(n1)


# Problem 7
# Create a program to check whether a number is negative or positive or equals to 0.



# number = input("Input the number: ")
# print(type(number))
# number = int(number)
#
# if number < 0:
#     print("The number is negative.")
# elif number > 0:
#     print("The number is positive.")
# else:
#     print("The number equals to 0")



#
# Problem 8
# Bob wants to go to university.
# Bob can be accepted if his math exam score is 10 or more and his english exam score is 10 or more.
# Bob can also be accepted if his math score is 15 or more and his english score is 5 or more
#                             or his math score is 5 or more and his english score is 15 or more.
# Bob can also be accepted if one of the scores is 20.
# Bob cannot be accepted if both scores are 0.
# (Exam scores are from 0-20)




# mxs = input("Input your math exam score: ")
# print(type(mxs))
# mxs = int(mxs)
#
# exs = input("Input your english exam score: ")
# print(type(exs))
# exs = int(exs)
#
# if mxs >= 10 and exs >= 10 or mxs >= 15 and exs >= 5 or mxs >= 5 and exs >= 15 or mxs == 20 or exs == 20:
#     print("Congratulations, Bob! You are accepted.")
# elif mxs < 0 or mxs > 20 or exs < 0 or exs > 20:
#     print("Input the right score.")
# else:
#     print("We are sorry to inform you that you are not accepted.")


# english_score = float(input("Input your english score: "))
# math_score = float(input("Input your english score: "))
# if math_score > 20 or english_score > 20 or math_score < 0 or math_score < 0:
#     print("Invalid Score.")
# else:
#     if math_score >= 10 and english_score >= 10:
#         print("Bob is accepted.")
#     elif (math_score >= 15 and english_score >= 5) or (english_score >= 15 and math_score >= 5):
#         print("Bob is accepted.")
#     elif math_score == 20 or english_score == 20:
#         print("Bob is accepted.")
#     elif math_score == 0 and english_score == 0:
#         print("Bob is not accepted")
#     else:
#         print("Bob is not accepted")







