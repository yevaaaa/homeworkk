"""
Problem 1
Write a function that will multiply all the list items.
"""

# list_of_numbers_2 = [3, 5, 15, 2, 9, 11, 10]
# multi = 1
# for i in list_of_numbers_2:
#     multi = multi * i
# print(multi)

"""
Problem 2
Write a program that removes duplicates from a list. DO NOT use set().
"""

# list_with_duplicates = ['a', 'b', 'ab', 'a', 'c', 'ab', 'd', 'hh', 'k', 'hh']
#
# list2 = []
# for i in list_with_duplicates:
#     if i not in list2:
#         list2.append(i)
# print(list2)

"""
Problem 3
Write a program that will find the second smallest number of the list.
"""

# ls = [3, 5, 88, -1, 0, -1, 3, -7, -10, 3, 3, -7, 5, -10, 1]
#
# ls2 = []
# for i in ls:
#     if i not in ls2:
#         ls2.append(i)
#         ls2.sort()
# print(ls2)
# print("The second smallest number is", ls2[1])

"""
Problem 4
Write a program that will add the string 'AAA' before every item of the list.
"""
# the_list = ['chrome', 'opera', 'mozilla', 'explorer']
#
# add = "AAA"
# new_list = ["AAA{0}".format(x) for x in the_list]
# print(new_list)

"""
Problem 5
Try to divide a number by 0. Use try, except as a backup. 
"""

# number = 5
#
# try:
#     print( 5 / 0 )
#
# except:
#     print("You cannot divide a number by 0.")

"""
Problem 6
Make a list and then try to access an index that doesn't exist. Use try and except. 
"""

# list3 = ["this", "is", "a", "list"]
#
# try:
#     print(list3[10])
# except:
#     print("This index doesn't exist.")

"""
Problem 7 (OPTIONAL)
1. You have a list of lists. You need to flatten the list. (Make 1 list of all the items in all lists.)
2. Do the same thing with list comprehension.
"""
list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]

#1
# flat_list = []
# for ls in list_of_list:
#     for item in ls:
#         flat_list.append(item)
#
# print(flat_list)

#2
# flat_list1 = [item for ls in list_of_list for item in ls]
# print(flat_list1)