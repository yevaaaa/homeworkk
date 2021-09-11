import math

"""
Problem 1
Write a function that gets a name and a salary and prints 'Employee named --- earns ---.'
If no salary is passed to the function, print the default salary which is 100.000.
"""

# def salary(name, salary=100000):
#     print("Employee named " + name + ' earns ' + str(salary))
#
#
# n = input("input your name ")
# s = input("input your salary ")
#
# salary(n, int(s))
# salary(n)


"""
Problem 2
Create a function that gets 3 numbers then checks if the first number falls between the 2nd and 3rd numbers.
"""


def number(n1, n2, n3):
    if n2 <= n1 <= n3 or n3 <= n1 <= n2 or n2 >= n3 >= n1:
        print(str(n1) + ' falls between ' + str(n2) + ' and ' + str(n3))

    else:
        print(str(n1) + ' doesn`t fall between ' + str(n2) + ' and ' + str(n3))


number(5, 4, 6)


"""
Problem 3
Create a function that gets 3 numbers and returns the biggest of them.
Hint: You can use a function inside a function. 
"""


def num(a, b, c):
    if a > b > c:
        print(a)
    elif b > a > c:
        print(b)
    elif c > a > b:
        print(c)


num(506, 7899, 20)

# I tried to use a function inside a function but it didn't work

"""
Problem 4
Write a function that will return the volume (ծավալ) of a cylinder (գլան). 
You can pass the radius and the height to the function. 
Google how to calculate the volume of the cylinder.
You are going to need sqrt(square root, արմատ) and pi (I show those below)
"""


# V=pi * r ** 2 * h

def volume(r, h):
    pi = math.pi

    def high():
        return r ** 2

    result = pi * h * high()
    return result


print(volume(50, 120))

"""
Problem 5 (Calculator)
Write a function that accepts 3 variables -> number1, number2, operation.
operation can be +, -, *, /
The function should return the result of the operation with the two number.
Example: calculator(9, 3, '+') -> result is 12
In case of division, if the second number is 0, say that the operation cannot be completed.
"""


def calculator(number1, number2, operation):
    if operation == '/':
        if number2 == 0:
            return 'Cant divide on 0'
        else:
            return number1 / number2
    elif operation == '+':
        solution = number1 + number2
    elif operation == '-':
        solution = number1 - number2
    elif operation == '*':
        solution = number1 * number2

    return solution



print(calculator(9, 3, '/'))

# et 0 i pahy vonc porceci chstacvec :(

