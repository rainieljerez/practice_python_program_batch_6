#Prog04. isupper() check if all characters of the string is on upper case.
#Create a program that do the same functionality without using isupper() function.

text = input("Enter a string to check if it is all uppercase: ")
is_up = any(c.isalpha() for c in text) # Ensure there's at least one letter

for char in text:
    if 'a' <= char <= 'z':
        is_up = False
        break
print(f"Is uppercase? {is_up}")