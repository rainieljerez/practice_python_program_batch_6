#Prog07. center() add space characters at the beginning and at the end of the string to
#print the string at the center. Create a program that do the same functionality without u
#sing center() function.

text = input("Enter string: ")
width = int(input("Enter total width to center within: "))

if len(text) >= width:
    print(text)
else:
    padding = width - len(text)
    left_pad = padding // 2
    right_pad = padding - left_pad
    print(f"Result: '{(' ' * left_pad) + text + (' ' * right_pad)}'")