#Prog02. removeprefix() remove the characters at the beginning of the string that
#matches the function parameter. Create a program that do the same functionality
# without using removeprefix() function.

text = input("Enter the full word: ")
prefix = input("Enter the prefix to remove: ")

if text[:len(prefix)] == prefix:
    print(f"Result: {text[len(prefix):]}")
else:
    print(f"Prefix not found. Result: {text}")