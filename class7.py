""" File handling """
#
# f = open(r'C:\Users\Asus\Desktop\file.txt', 'r')
# print(f.read())

# fi = open(r'C:\Users\Asus\Desktop\file.txt', 'r')
# word = fi.read()
# print(word.index("Yeva"))
# print(fi.readlines())
# print(fi.readline())

# for x in fi:
#     if x == "Yeva":
#         break
#     print(x)

# file = open(r'C:\Users\Asus\Desktop\file.txt', 'r')
#
# for x in file:
#     print(x)  #loop over the file

""" Closing file"""

# file = open(r'C:\Users\Asus\Desktop\file.txt', 'r')
# print(file.readline())
# file.close()
#
# with open(r'C:\Users\Asus\Desktop\file.txt', 'r') as file:
#     file.read(5)
#
# file = open(r'C:\Users\Asus\Desktop\file.txt', 'a')
# file.write("this is a new text")  we use this when we want to add smth to our file
# file.close()

# """writing in a file"""
# file2 = open(r'C:\Users\Asus\Desktop\file.txt', 'w')
# file2.write("I deleted everything")
# file2.close()  # we use this to delete the text in our file and add the new one

# file1 = open(r'C:\Users\Asus\Desktop\file.txt', 'w')
# list_of_lines = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
#
# file1.write("Hello \n")
# file1.writelines(list_of_lines)
# file1.close()    #esi eli jnjum a meji exac chexacy u nor ban a grum

"""creating a new file"""
# file3 = open(r'C:\Users\Asus\Desktop\file25.txt', 'x')
# file3.write("hello \n")
# file3.close()

# file1 = open(r'C:\Users\Asus\Desktop\file1.txt', 'x')
# file1.close()
# file2 = open(r'C:\Users\Asus\Desktop\file2.txt', 'x')
# file2.close()
# file2 = open(r'C:\Users\Asus\Desktop\file2.txt', 'x')
# file2.close()

# for i in range(1, 4):
#     f = open(fr'C:\Users\Asus\Desktop\file{i}.txt', 'x')
#     f.write(f"write text {i}")

# import os
# os.remove(r'C:\Users\Asus\Desktop\file2.txt', 'x')




