"""PYTHON DATES"""

# from  datetime import datetime
# print(datetime.now())


import datetime

# x = datetime.datetime.now()
# print(x)

# y = datetime.datetime.today()
# print(y)
# print(y.month)
# print(y.year)
# print(y.day)
# print(y.hour)
# print(y.minute)
# print(y.second)
# print(y.microsecond)


"""strftime() - how to convert a date to a string"""

# x = datetime.datetime(2018, 9, 15, 12, 45, 35, 999999)
# y = datetime.datetime(2018, 9, 15)
# microsecond consist of 6 digits
# print(x)
# print(y)
# print(x.strftime("%b %d %Y %H:%M:%S"))
# print(x.strftime("%A %b %d %Y %H:%M:%S"))

# x = datetime.datetime(2018, 9, 15)
# print(x.strftime(('%d/%m/%Y')))
# print(type(x.strftime(('%d/%m/%Y'))))


# str1 = '9/15/18 12:33:09-----Sep'
# date_object = datetime.datetime.strptime(str1, '%m/%d/%y %H:%M:%S-----%b')
# print(date_object)

"""pr1"""

# str1 = '10-8-03'
# z = datetime.datetime.strptime(str1, '%m-%d-%y')
# n = datetime.datetime.now()
# print(n - z)

"""RANDOM"""

import random
#
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))

# string = "Yeva"
# print(random.choice(string))

# print(random.randrange(20, 50, 5))

# random.shuffle(list1)
# print(list1)

# ls = []
# ls.extend(range(10, 21, 2))
# print(ls)

"""pr2"""

ls = ['mozzilla', 'chrome', 'opera', 'explorer', 'safari', 'brave']


# for i in ls:
#     random.choice(ls)
#     if i == "opera":
#         print("found opera")
#         break
#     else:
#         print("still waiting")

# 2

# while 1 > 0:
#     choice1 = random.choice(ls)
#     if choice1 == 'opera':
#         print('found opera')
#         break
#     else:
#         print(choice1)
#         print('still waiting')

"""lambda"""
#
# def func(x):
#     return x           ========== lambda x: x

# x = lambda  a : a + 10
# print(x(5))
#
# x = lambda a, b : a * b
# print(x(5, 6))

"""lambda func"""

# def myfunc(n):
#     return lambda a: a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(11))
# print(mytripler(5))

# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
# print(squared)

"""PIP - tool(library) for installing """

import camelcase

c = camelcase.CamelCase()
str1 = "hello everyone"
print(c.hump(str1))


