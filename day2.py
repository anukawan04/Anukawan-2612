#slicing
name = "anu"
print(name[0:1])

name = "purnima"
print(name[3:6])

name = "purnima"
print(name[3: ])

name = "purnima"
print(name[0:len(name)-2 ])

#LENGTH
print(len(name))

#find and replace

name = "sangit"
print(name.find("g"))
replaced = name.replace("g","p")
print(replaced)

#escspe sequence character
text = "my name is Anu \n\ and\n i am 20 years"  #t-tab
print(text)

text = "my name is Anu \n\t and\n\t i am 20 years"  #t-tab
print(text)

text = "my name is Anu \n\'here\' and\n\t i am 20 years"  #t-tab
print(text)