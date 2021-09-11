"""
Problem 1
Create 3 dictionaries for your favourite top 3 cars. Dict should contain information like brand, model, year, and color.
Add all those dicts in one dict and print items.
"""

d1 = {
    "brand": "Mercedes",
    "model": "amg gt",
    "year": "2021",
    "color": "black"
}
d2 = {
    "brand": "porsche",
    "model": "macan",
    "year": "2020",
    "color": "red"
}
d3 = {
    "brand": "volkswagen",
    "model": "beatle",
    "year": "any",
    "color": "white"
}

# dict_keys = ['dict1', 'dict2', 'dict3']
# all_dicts = [d1, d2, d3]
# res = dict(zip(dict_keys, all_dicts))
# print(res)
# print(res.items())

#2
# cars = {}
# cars.update({"d1": d1, "d2": d2, "d3":d3})

"""
Problem 2
You have a list of lists. Each list in the list contains a key and a value. Transform it into a list of dictionaries. 
Use loops.
"""
ls = [['Bob', 45], ['Anna', 4], ['Luiza', 24], ['Martin', 14]]

# dt = {}
# for i in ls:
#     dt.update({i[0]: i[1]})
# print(dt)

"""
Problem 3
Check if value 1000 exists in the dict values. If yes delete all other items except that one.
"""
dt = {'hundred': 100, 'million': 1000000, 'thousand': 1000, 'ten': 10}

print(dt.get("thousand"))

# for i in list(dt.keys()):
#     if i != "thousand":
#         dt.pop(i)
# print(dt)

"""
Problem 4
Change Narine's salary to 10000
"""
sampleDict = {
    'employee1': {'name': 'Marine', 'salary': 7500},
    'employee2': {'name': 'Karine', 'salary': 8000},
    'employee3': {'name': 'Narine', 'salary': 6500}
}

# sampleDict.update({'name': 'Narine', 'salary': 10000})
# print(sampleDict)

"""
Problem 5
Write a function that will get a dict of employees and their salaries. It will return a new dict with 
the same keys (employees) and all values will be the average of their salaries. 
example:  dict1 = {'ann': 3000, 'bob': 4000, 'lily': 5000}
          dict2 = {'ann': 4000, 'bob': 4000, 'lily': 4000}
"""
d = {'ann': 3000, 'bob': 4000, 'lily': 5000, 'molly': 5500, 'some_intern': 500}

# answer = 0
# for i in d:
#     answer = answer + d[i]
#     ans = answer / len(d)
# print(answer)
# print(int(ans))
# d.update((i, int(ans)) for i in d)
# print(d)

"""
Homework 7 Problem 4
Write a program that will add the string 'AAA' as an item before every item of the list.
"""
the_list = ['chrome', 'opera', 'mozilla', 'explorer']

ls1 = []
for i in the_list:
    for j in ["AAA", i]:
        ls1.append(j)
print(ls)


