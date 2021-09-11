# #STRINGS
#
# fruit = 'banana'
# letter = fruit[1]
# print(letter)
#
# letter1 = fruit[2]
# print(letter1)
#
# print(len(fruit))
#
# long_text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
# industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
# type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into
# electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker
# including versions of Lorem Ipsum"""
# print(long_text[-7])
# print(len(long_text))
#
# print('i\'m Yeva')
#
# print(long_text[6:12])
# print(long_text[:10])
#
# var = "Yeva Tsughunyan"
# print(var[:4])
# print(var[5:])

#IMMUTABLE BARY HISHEL

# txt = "Karine"
# new_txt = "M" + txt[1:]
# print(new_txt)
#
# sentence = "Ani is a backend developer"
# print(sentence.find("developer"))
# print(sentence[17:])
# print(sentence.find(" "))
# print(sentence.count(" "))   #hashvec qani hat prabel ka
# #ASCII masin kardal
# print(sentence.count("a"))


# txt = " The weather is sunny "

# if "sun" in txt:
#     print("rain is NOT in text")
#
# txt = "The weather is sunny, rainy"
# if "rain" not in txt:
#     print("rain is NOT in text")

# print(txt.upper())
# print(txt.lower())
# print(txt.strip()) # demi u hetevi probely hecha anum
# txt.replace("n", "q")
# print(txt.split(" "))


# txt = "I am a back-end developer."
# if txt.find("back-end"):
#     print(txt.split("-"))


# txt = "I am a back-end developer"
# if "back-end" in txt:
#     print(txt.split("-"))
#
# age = 30
# txt = "she turns {} next year".format(age)
# print(txt)

# age1 = 14
# age2 = 34
# txt = "she turns {1} next yr, and her bro turns {0}".format(age1, age2)
# print(txt)
#
# txt1 = f"she turns {age2} next yr, and her bro {age1}"
# print(txt1)  #this way of sol is better
#
#
#
# name = "Bob Bobyan"
# workplace = "Google"
# text = f"Hi I am {name[0:3]} and i work in {workplace.upper()} "