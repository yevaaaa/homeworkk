# Homework 4
"""
Problem 1
You have two strings. Put one in the middle of the other one.
Example: s1 = "Environment", s2 = "Earth", result should be "EnviroEarthnment"
"""
# st1 = "Environment"
# st2 = "Earth"
# new_word = st1[:6] + st2 + st1[6:]
# print(new_word)

"""
Problem 2
You have five strings. Create two strings, 1 containing all the beginning letters of the five strings,
and 1 containing all the ending letter of the 5 strings.
"""

# s1 = "qwerty"
# s2 = "asdfg"
# s3 = "tyu"
# s4 = "1234"
# s5 = "p"
#
# firstl = s1[0] + s2[0] + s3[0] + s4[0] + s5[0]
# lastl = s1[-1] + s2[-1] + s3[-1] + s4[-1] + s5[-1]
# print(firstl)
# print(lastl)

"""
Problem 3
Create a function that gets a name. If the length of the name is odd (կենտ) it returns the name all in upper case.
If the length of the name is even (զույգ) just return it.
"""

# func = input("Input your name: ")
#
# if len(func) % 2 == 0:
#     print(func)
# elif len(func) % 2 != 0:
#     print(func.upper())

"""
Problem 4
You have a CNN article. You want to find out how many time the words 'university', 'vaccine', 
'student' (but not 'students') appear in the text. 
You also want to find out how many numbers from 1 to 5 can be found in the text.
"""
article = """ (CNN)The University of Virginia has disenrolled 238 students for its fall semester on Friday for not 
complying with the university's Covid-19 vaccine mandate, according to a university spokesperson.
UVA requires "all students who live, learn, or work in person at the university" to be fully vaccinated 
for the upcoming 2021-2022 academic year, according to current university Covid-19 policies.
Out of the 238 incoming Fall semester students, only 49 of them were actually enrolled in classes, and the remaining 
189 "may not have been planning to return to the university this fall at all," UVA spokesperson Brian Coy told CNN.
"Disenrolled means you're not eligible to take courses," Coy said. 
He added that students who were enrolled at the university on Wednesday still have a week to update their status 
at which point they can re-enroll."""

# print(article.count("university"))
# print(article.count("vaccine"))
# result = article.split()
# print(result.count("student"))
# print(article.count("1"))
# print(article.count("2"))
# print(article.count("3"))
# print(article.count("4"))
# print(article.count("5"))

"""
Problem 5
Find out if there is '2021-2022' string in the article and slice it. 
"""
if "2021-2022" in article:
    print(article[323:332])

"""
Problem 6 
Create a function that gets a string and returns the same string but the half of it UPPERCASE.
(It's okay if the string has odd number of characters and half is not the exact half)
"""

# word = str(input("Input a 4-letter word: "))
# if len(word) > 4 or len(word) < 4:
#     print("Wrong input")
# else:
#     print(word.upper()[0:2] + word.lower()[2:])


"""
Problem 7
Write a function that takes a name and a (future) profession and returns the sentence
"I am Ani Amirjanyan and I am a backend developer.".
Use .format or f" "
"""

# name = "Yeva Tsughunyan"
# profession = "backend developer"
#
# text = f"I am {name} and I am a future {profession}"
# print(text)

"""
Problem 8
Create a function that takes a 3 digit number (can't take more or less digits) and returns the reverse number.
Example: take "987" return 789. (It is okay if the result starts with 0)
"""
#
# n = int(input('Input a number : '))
# reversed = int(str(n)[::-1])
# if n < 100 or n > 999:
#     print("Input the right number.")
# else:
#     print(reversed)
