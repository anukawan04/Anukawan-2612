#write a program to detect double space in a string
#replace the dounle spaces from problem 3 with single spaces
#write a program to format the following letter using escape sequence characters.



letter = "Dear Students, This python course is going well. Thanks!"


text="Dear Student,  This python course is going well. Thanks"
if " " in text:
    print("double space is detected")

else:
    print("no double space")




#replace the double space from problem 3 with problem 3 with single space

replaced=text.replace("  "," ")
print(replaced)

# write a program to format the following letter using escape sequences character
letter = "Dear students,\n\tThis Python course is going well.\nThanks!"
print(letter)