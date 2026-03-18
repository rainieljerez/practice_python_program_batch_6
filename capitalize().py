#Prog09. capitalize() makes the first letter of the string, capital letter. And all other
#letter in small case. Create a program that do the same functionality without using
#capitalize() function.

text = input("Enter string to capitalize: ")
if not text:
    print("")
else:
    # Handle first char
    first = text[0]
    first = chr(ord(first) - 32) if 'a' <= first <= 'z' else first

    # Handle the rest
    rest = ""
    for char in text[1:]:
        rest += chr(ord(char) + 32) if 'A' <= char <= 'Z' else char

    print(f"Result: {first + rest}")