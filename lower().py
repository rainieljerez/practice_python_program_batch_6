#Prog03. lower() converts all characters of the string into lower case.
#Create a program that do the same functionality without using lower() function.
text = input("Enter a string to lowercase: ")
result = ""
for char in text:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
print(f"Result: {result}")
