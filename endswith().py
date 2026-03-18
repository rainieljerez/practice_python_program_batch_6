#Prog05. endswith() check if the string end part matches the function parameter.
#Create a program that do the same functionality without using endswith() function.

text = input("Enter the string: ")
suffix = input("Enter the suffix to check: ")

if len(suffix) <= len(text) and text[-len(suffix):] == suffix:
    print(True)
else:
    print(False)