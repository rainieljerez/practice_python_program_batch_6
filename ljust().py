#Prog06. ljust() add space characters at the end of the string to complete the number
#of characters specifies in function parameter. Create a program that do the same
#functionality without using ljust() function.
text = input("Enter string: ")
width = int(input("Enter total desired width: "))

padding = width - len(text)
result = text + (" " * padding) if padding > 0 else text
print(f"Result: '{result}'")