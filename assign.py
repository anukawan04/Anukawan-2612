# #write a program to add two number
# a = int(input("Enter a number : "))
# b = int(input("enter a number"))
# c = a+b
# print(c)

# #2write a py to find remainder when a number is divide by Z

# a = int(input("enter a num:"))
# b = int(input("enter a number:"))
# c = a%b
# print(c)


#3 check the type of the variable assign using input()function

a = input("tyoe here: ")
print(type(a))


#4write a python to find reminder when a number is divided by 2

sum3= int(input("enter any number"))
reminder = sum % 2
print(reminder)
# 5use the comparision operators to find out whether a variable is greater than b or not

a=34
b=80
result=a>b
print(f"the variable a is greater than b : {result}")

#6write a python program to calculate square a numbers entered by the user

a=int(input("enter the value : "))
total1=a**2
print(f"the square value : {total1}")

#7write a python to display a user centered nmae followed by good afternoon using input()function
name=input("enter your Name")
print(f"Good Afternoon {name}")

from os import replace
#8WAP to fill in a letter template given below with name and date
letter ='''Dear <|Name|>,
          you are selected !
             <|Date|>'''


username=input("Enter you name to see the result :")
Date=input("enter the full date you participated :")

letter=letter.replace("<|Name|>", username)
letter=letter.replace("<|Date|>",Date)

print(letter)
#9wap to detect double space in a string
sentence=input("Enter your sentence")
if " " in sentence :
  print("Please, Aviod double spacing (    )")
else:
  print("No double space found")
# 10Replace the double space from the sentence with a single space

sentence1 = input("Enter your sentence: ")
sentence2 = sentence1.replace("  ", " ")  # Replace double spaces

print("Original sentence:", sentence1)
print("Fixed sentence   :", sentence2) 