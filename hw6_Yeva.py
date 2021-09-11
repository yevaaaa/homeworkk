"""
Problem 1
Create a file manually with some text in it like "My favourite fruits are:".
Then write a program to append the file with the fruits that you love.
"""
# file.write("banana, watermelon")
# file.close()

"""
Problem 2
Create a file that has 5 or more lines of text.
Write a program to store each line in a variable.
"""

# f = open(r'C:\Users\Asus\Desktop\hw6_Yeva_files\lorem.txt', 'r')
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# line5 = f.readline()
# f.close()
# print(line1, line2, line3, line4, line5, end = '\r')

"""
Problem 3
Find the longest word in the file pr3.txt.
"""

# file3 = open(r'C:\Users\Asus\Desktop\hw6_Yeva_files\pr3.txt', 'r')
# f = file3.read().replace(',', '').replace('.', '')
# word_list = f.split()
# longest_word = ''
# for word in word_list:
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)


"""
Problem 4
Create a list of names of all our group members.
Loop over the list and create files (filename = name).
Each file should contain the name of a person repeated as many times as the characters of the name.
for example: file -> Ani.txt
              text - > Ani
                       Ani
                       Ani
Ani is repeated 3 times as it has 3 characters.
"""

list = ["Yeva", "Hayarpi", "Mary", "Marc", "Hovhannes", "Abraham", "Alik", "Aren", "Armen", "Arsen", "Artur",
"Ashot", "David", "Nerses", "Vardan"]

for i in list:
    file5 = open(fr'C:\Users\Asus\Desktop\{i}.txt','w')
    x = len(i)
    for a in range(x):
        file5.writelines(i)
        file5.writelines('\n')

    file5.close()

for i in list:
    file5 = open(fr'C:\Users\Asus\Desktop\{i}.txt', 'w')
    file5.write(f"{i} \n" * len(i))


"""
Problem 5

After writing Problem 4 write a function that gets this list and checks if files with these names exist. 
If a file exists return True, otherwise False.
"""
# new_names = ['Ani', 'Armen', 'Aren', 'Argishti', 'Arsen', 'Alik', 'Anahit', 'Anna']
#
# for x in  new_names:
#
#     try:
#         f = open(fr'C:\Users\Asus\Desktop\{x}.txt', 'r')
#         print("True")
#     except:
#         print("False")

"""
Problem 6
Write a function that gets a file path and calculates how many upper case letters are in the text.
Hint: use isupper() method.
"""
#
# def upper():
#     file6 = open(r'C:\Users\Asus\Desktop\hw6_Yeva_files\upper.txt', 'r')
#     words = file6.read()
#     n = 0
#     for i in words:
#         if i.isupper():
#             n +=1
#     print(n)
#     file6.close()
#
# upper()
