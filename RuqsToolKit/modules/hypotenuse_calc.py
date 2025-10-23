#this script is for python exercise 1

#this is a piece of code that calculates the square of the hypotenuse for a given triangle - if a = 10 and b = 12 then what is the square of the hypotenuse?

def hypotenuse_calc (a, b):
    return a**2 + b**2

a = 10
b = 12

result = hypotenuse_calc(a, b)

print("The square of the hypotenuse is:", result)
