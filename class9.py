"""DICTIONARIES
dict format"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_in_store": True,
    "colors": ["red", 'blue']
}

# print(type(thisdict))
# print(thisdict["brand"])
# print(thisdict.get("model"))
# print(thisdict.get("ll"))
# print(list(thisdict.keys()))
# print(list(thisdict.values()))
# print(list(thisdict.items()))

# if "year" in thisdict:
#     print("that key exists")

"""problem1"""

mydict = {
    "name": "Yeva",
    "surname": "Tsughunyan",
    "age": "17",
    "email": "yeva.tsughunyan@gmail.com"
}
# print(mydict.keys())
#
# if "age" in mydict:
#     print(True)

"""updating the dict and adding irems"""

# thisdict.update({"year": "2020",
#                  "owned": True,
#                   "Year": 123,
#                  })
# print(thisdict)
# thisdict["year"] = 1900
# print(thisdict)

"""removing items"""
# key1 = "model"
# value1 = thisdict.pop(key1)
# thisdict.update({key1: value1})
# print(thisdict)

# thisdict.popitem()
# thisdict.popitem() #verji itemy jnjum a
# del thisdict["model"]
# del thisdict
# thisdict.clear()
# print(thisdict)

"""problem 2"""

key = ['phone number', 'country']
value = ['+37491414614', 'Armenia']

# for i in range(len(key)):
#     mydict.update({key[i]: value[i]})
#     print(mydict)

#
# mydict.update({key[0] : value[0], key[1] : value[1]} )
# print(mydict)

"""looping through dicts"""
for x in mydict:
    print(x) #keys
    print(mydict[x]) #values
#
# for x in mydict.items():
#     print(x)

# for x, y in mydict.items():
#     print(x, y)

"""copy a dict"""

# copyofthisdict = mydict.copy()
# copyofthisdict.clear()
# print(copyofthisdict)
# print(mydict)

"""problem 3"""

# def func(mydict):
#     copy = mydict.copy()
#     copy.clear()
#     item = {'state': 'empty'}
#     copy.update(item)
#     return copy
#
#
# print(func(mydict))

myfamily = {
    "child1": {
        "name": "Bob",
        "year": 2000
    },
    "child2": {
        "name": "Anna",
        "year": 2002
    }
}

listofdicts = [{"name": "Bob", "year": 2000}, {"name": "Anna", "year": 2002}]
d