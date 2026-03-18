#Prog08. swapcase() reverse the casing of each of the character of the string. Create
#a program that do the same functionality without using swapcase() function.

text = input("Enter string to swap casing: ")
result = ""
for char in text:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char
print(f"Result: {result}")