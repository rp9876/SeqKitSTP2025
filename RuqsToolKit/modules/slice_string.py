#this code is for python exercise 1 - to slice some string


#define new function stringslicer, which needs the following parameters: a piece of string (text), a start position (s1) and an end position (e1) or more
#the function slices the text into 2 depending on the input integers and returns the 2 slices separated by a space
def stringslicer (text, s1, e1, s2, e2):
    slice1 = text[s1:e1]
    slice2 = text[s2:e2]
    return slice1 + " " + slice2

#the text is give, the result variable is defined using the function and inputs and is finally printed
text = "TheUniversityOfManchester"
result = stringslicer(text, 3, 12, 15, 25)
print(result)

#OR

text = input("enter your text ")
s1 = input("enter your start position ")
e1 = input("enter your end position ")

s2 = input("enter your start position ")
e2 = input("enter your end position ")

result = stringslicer(text, 3, 12, 15, 25)
print("Your sliced string is: ", result)