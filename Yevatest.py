"""
Quiz 1
Name: Yeva
"""
import random

"""
Problem 1   (2 points)
Let the user input two numbers. Then print all the numbers between those inputted numbers.
"""

# n1 = int(input("Input a number: "))
# n2 = int(input("Input a number: "))
#
# rng = range(n1 , n2 + 1)
# nlst = list(rng)
#
# for y in nlst:
#     print(y)


"""
Problem 2   (3 points)

You have a long string of words. Write a program that will only print the words (from that string)
that have more than 5 characters.
"""
text = """This makes texting a quick and easy way to communicate with friends, family and colleagues, including in
       contexts where a call would be impolite or inappropriate."""

# w = text.split()
# for i in w:
#     if len(i) > 5:
#         print(i)


"""
Problem 3   (3 points)

Write a function that gets a list of sets. 
It loops over it and adds a random number from 1-100 to the sets that have odd length.
It converts all the sets into tuples. 
The returned result should be a list of tuples that have even length.
"""

sets = [{4, 2, 8}, {'a', 'b'}, {1000, 10, 1, 100, 10}, {1, 23, 456, 7}, {6, 6, 6, 6}, {3, 'three'}]

# for i in sets:
#     if len(i) % 2 != 0:
#         i.add(random.randrange(1, 100))
#         i = tuple(i)
#
#
# def func(ls):
#     for i in range(len(ls)):
#         if len(ls[i]) % 2 != 0:
#             rand_num = random.randrange(1, 100)
#             ls[i].add(rand_num)
#         ls[i] = tuple(ls[i])
#     return ls
#
#
# print(func(sets))
"""
Problem 4   (3 points)

You have a list of items of different types. Loop over it and try to convert every item to integer and print it. 
If it is impossible, print '{item} cannot be converted to an integer'.
"""
ls = [True, 9, '98.2', 'bob', '0', ' ', 4.5555, False]

# for i in ls:
#     try:
#         print(int(i))
#     except:
#         print(f"{i} cannot be converted to integer")

"""
Problem 5   (3 points)

You have information that needs to be made into a nested dictionary.
Bob's surname is Jackson. He is 40 years old. He has 2 emails [j.b@gmail.com, b.j@mail.ru]
Bob has 2 addresses, address1 = 123 Jacksonville, Ohio
                     address2 = 567 Bobville, Florida

Anna's surname is Brown. She is 30 years old. She has 3 emails [an@gmail.com, ann@mail.ru, ann6@mail.ru]
Anna has 2 addresses, address1 = 123 Annaville, Ohio
                      address2 = 567 Brownville, Florida

Build a dictionary that has two values with Bob's and Anna's info.
Dict should be nested.
"""
# bob = {
#     "name": "Bob",
#     "surname": "Jackson",
#     "age": 40,
#     "email": ["j.b@gmail.com, b.j@mail.ru"],
#     "adress1": "address1 = 123 Jacksonville, Ohio",
#     "adress2": "address2 = 567 Bobville, Florida",
# }
#
# anna = {
#     "name": "Anna",
#     "surname": "Brown",
#     "age": 30,
#     "email": ["an@gmail.com, ann@mail.ru, ann6@mail.ru"],
#     "adress1": "aaddress1 = 123 Annaville, Ohio",
#     "adress2": "address2 = 567 Brownville, Florida",
# }
#
# result = {
#     'n1': bob,
#     'n2': anna
# }
# print(result)


"""
Problem 6 (3 points)
You have a dictionary. Loop over it, if the value doesn't start with uppercase letter, make it uppercase.
"""
d = {
    'name1': 'martin',
    'name2': 'Anna',
    'name3': 'Luiza',
    'name4': 'anahit',
    'name5': 'bob',
    'name6': 'Armen',
    'name7': 'artak'
}

# for i in d.values():
#     if i != i[0].upper():
#         print(i[0].upper() + i[1:])

"""Problem 7 (3 points) You have a list of tuples (of length two). Write a function that will return a list of items 
where each item is the sum of the numbers in tuple. 

Example [(2, 3), (4, 5)] --> [5, 9] 
"""
lst = [(2, 3), (4, 5), (16, 98), (8, 99), (23, 456)]

# tup = []
# for i in lst:
#     tup.append(i[0] + i[1])
# print(tup)
