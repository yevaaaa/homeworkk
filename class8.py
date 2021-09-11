'''error handling'''
#
# try:
#     print(x)
# except:
#     print("An exception occurred")
# finally:
#     print('code reached finally')

# x = 10
# try:
#     print(x)
# except NameError :
#     print("please define variable name for x")
# except:
#     print("smth else has happened")
# else:
#     print("Nothing went wrong")

# f = open(r'C:\Users\Asus\Downloads\pr3.txt')  #try y charec vorovhetev "w" cheinq grel verjum
# try:
#     f.write("Lorem ipsum")
# except:
#     print("smth went wrong when writing to the file")
# finally:
#     f.close()

"""Problem 1"""

# try:
#     print(10 + "this is ten")
# except:
#     print("You can't add a number to an int")

"""raising an error"""
# try:
#     4 + "f"
# except:
#     raise  TypeError("cant add int to str")

"""List- data type"""
"""changing list items"""
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
#
# thislist[1:4] = ["blackcurrant", "watermelon", "cherry"]
# print(thislist)

"""inserting values"""
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelomn")
# print(thislist)

"""append method"""
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = [ "mabgo", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# ls = [] myus dzevy
# ls = thislist + tropical
# print(ls)

# thislist.extend('ani')
# print(thislist)

# try:
#     thislist.extend('mari')
# except:
#     print("im expecting just one list to add to the other one")

"""problem 2"""

list = []
list.append("sleeping")
list.append("movies")
list.append("tennis")
print(list)

# for i in list:
#     list.remove(i)
# print(list)

"""removing list items"""
# while len(list) != 0:
#     list.remove(list[0])
# print(list)

# for i in range(len(list)):
#     list.remove(list[-1])
# print(list)

# for i in list[::]:  # :: y amen inch vercnum a
#     list.remove(i)
# print(list)

# for j in list:  #en while i texy senc el a linum
#     list.remove(j)
#     print(list)


"""remove list items"""
thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

"""pop- jnjum a u veradarcnum a en valuen vory jnjel a"""
# print(thislist.pop(1))
# print(thislist.pop())

# del thislist[0]
# print(thislist)


# thislist.clear()
# print(thislist)

"""sorting"""
# list1 = [100, 50, 65, 83]
# list1.sort(reverse=True)
# print(list1)

"""list comprehension"""
# thislist = ["apple", "banana", "cherry"]
# newlist = [ x for  x in thislist if "a" in  x]
# print(newlist)