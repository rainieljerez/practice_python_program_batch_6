#rog10. title() makes all first letter of each word in the string, capital letter. And all
#other letter in small case. Create a program that do the same functionality without using
#title() function.
text = input("Enter a sentence for title case: ")
result = ""
new_word = True

for char in text:
    if not char.isalpha():
        result += char
        new_word = True
    elif new_word:
        result += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        new_word = False
    else:
        result += chr(ord(char) + 32) if 'A' <= char <= 'Z' else char
print(f"Result: {result}")