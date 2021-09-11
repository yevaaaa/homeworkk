"""
Problem 1
Write a function that gets a set and an item. It returns the set without the item if it was present in the set.
"""
set1 = {"item"}
# ls = list(set1)
# for i in ls:
#     if i in ls:
#         ls.remove(i)
#         tp = tuple(ls)
#         print(tp)

#chisht dzevy
# def check(set1, item):
#     if item in set1:
#         set1.discard(item)
#         return set1
#     else:
#         return set1
#
# print(check({'a','b','c','d'}, 'c'))

"""
Problem 2
Write a program that gets two sets. If they have the same items it deletes those items from both sets 
and prints them.
"""

s1 = {"apple"}
s2 = {"apple", "banana"}

# l1 = list(s1)
# l2 = list(s2)
#
# for i in l1:
#     for j in l2:
#         if i == j:
#             l1.remove(i)
#             l2.remove(j)
#             t1 = tuple(l1)
#             t2 = tuple(l2)
#             print(t1)
#             print(t2)
#         else:
#             print("The items are not the same")

# items = s1.intersection_update(s2)
# s2 = s2.difference(items)
# print(s2)

"""
Problem 3
You have a list of tuples. Remove the tuples that have length 1.
"""

test_list = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]


# for i in test_list:
#     if len(i) == 1:
#         test_list.remove(i)
# print(test_list)

"""
Problem 4
You have two tuples.
Create tuples of all combinations of those tuple elements and store them in a list.
"""
# tuple1 = (1, 5)
# tuple2 = (7, 2)
#
# t = []
# for x in tuple1:
#     for y in tuple2:
#         t.append((x, y))
#         t.append((y, x))
# print(t)

"""
Problem 5
Convert a tuple to a float data type.
Example: (9, 56) - 9.56
"""
tp_ex = (77, 31)
print(float(str(tp_ex[0]) + '.' + str(tp_ex[1])))

"""
Problem 6 
Write a program that will sort tuples by their maximum element.
"""
list1 = [(4, 5, 20, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# w = []
#
# for i in list1:
#     list1 = list(sorted(i, reverse= True))
#     w.append(list1)
# print(w)


def get_max(sub):
    return max(sub)

list1.sort(key= get_max)
print(list1)

