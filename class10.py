"""TUPLES"""

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(type(thistuple))

"""problem 1"""

# tp = ("winter", "summer")
# ls = list(tp)
# # print(ls)
# x = ("fall", "spring")
# ls2 = list(x)
# # print(ls2)
# for i in ls:
#     tp2 = ls + ls2
# # print(tp2)
# result = tuple(tp2)
# print(result)

"""adding tuple to a tuple"""

# tp = ("ani")
# print(type(tp))

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

"""Problem2"""
# tp = ("winter", "summer")
# lst = list(tp)
# # print(lst)
#
# lst.remove("winter")
# lst.remove("summer")
# res = tuple(lst)
# print(res)

# tp = ("winter", "summer")
# ls = list(tp)
# ls.clear()
# print(ls)
# ls = tuple(ls)
# print(ls)

"""unpacking tuples"""
#
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)

"""using asterisk"""

# fruits = ("apple", "banana", "cherry", "straw", "ras")
# (green, yellow, *red) = fruits
# print(red)
# (green, *yellow, red) = fruits
# print(red)
# (*green, yellow, red) = fruits
# print(green)

"""looping through tuple"""
# fruits = ("apple", "banana", "cherry", "straw", "ras")
# for x in fruits:
#     print(x)

# int_tp = (2, 3, True, False, [5,6,7], {1: 'one', 2: [None, None]})
# print(len(int_tp))

"""SETS"""

# thisset = {"apple", "banana", "cherry"}
# print(type(thisset))
#
# sett = {1, 2, 3}
# print(sett)

"""set constructor"""

# thisset = set(("apple", "banana", "cherry"))
# print(thisset)

"""accessing set items"""
# thisset = set(("apple", "banana", "cherry"))
#
# for i in thisset:
#     if i == "banana":
#         print("banana" in thisset)

"""adding items to set"""
# thisset = set(("apple", "banana", "cherry"))
# thisset.add("orange")
# print(thisset)

"""update a set"""
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)
#
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update("tropical")
# print(thisset)
#
# thisset = {"apple", "banana", "cherry"}
# # tropical = {"pineapple", "mango", "papaya"}
# thisset.add('a')
# thisset.update({"tropical"})
# print(thisset)
#
thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# thisset.discard("banana")

# print(thisset.pop())
#
# thisset.clear()
# print(thisset)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
# set3 = set1.union(set2)
# print(set3)

# set3 = set1.intersection_update(set2)
# print(set1)

# set1.intersection_update(set2)
# print(set1)

z = set1.difference(set2)
z1 = set2.difference(set1)
print(z)
print(z1)