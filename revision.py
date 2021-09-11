"""
Problem 1
You get a list. Delete each items last character and return the list.
"""
ls = ['bobb', 'annaa', 'martinn']

# ls2 = []
# for i in ls:
#      s = i[:-1]
#      ls2.append(s)
# print(ls2)

"""
Problem 2
Write a function that gets list (length longer than 3) divides the list into three parts and returns three lists.
"""
list = ["pamidor", "varung", "badrjan", "gazar", "sox", "chgitem"]



# l = []
# for i in list:
#     l.append(list[0:2])
#     l.append(list[2:4])
#     l.append(list[4:6])
#     break
# print(l)

#2
# n=2
# newlist=[list[i:i + n]
#          for i in range(0, len(list), n)]
# print(newlist)

"""
Problem 3
You get a dictionary. The values are names but there might be commas(,) and dots(.) in the names that need to be removed
Return the dictionary with valid values.
"""
d = {
    'name1': 'ma,.rt.in',
    'name2': 'A.,nna',
    'name3': 'Lui,.z.a',
    'name4': 'an,ahi.,t',
    'name5': 'b,ob',
    'name6': 'Ar,m.en',
    'name7': ',,,,a,rt,ak'
}

v = []
for x in d.values():
    x = x.replace(",", "").replace(".", "")
    v.append(x)
print(v)






"""
Problem 4
You have two tuples. The lengths are equal. Write a program that multiplies the numbers from two tuples with the same 
index.
Example: (4, 5, 0) and (1, 3, 4) --> (4, 15, 0)
"""

# t1 = (4, 5, 0)
# t2 = (1, 3, 4)
#
# for i in range(0, 3):
#     print(t1[i] * t2[i])

"""
Problem 5
You have a list. Pick 2 random ranges. Given the ranges of the list (for example [2:5]) tell the user how many 
characters are in the item under 2, 3, 4 indices altogether. 
"""
lst = ["Jon", "Kelly", "Jessa", "Jodi", "Eric", "Garry", "Scott"]
# z = 0
# for i in lst[2:5]:
#     z += len(i)
# print(z)




