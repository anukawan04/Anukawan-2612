l1 = [1,8,7,2,21,15]

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3,8)
print(l1)

l1.append(5)
print(l1)

l1.pop(5)
print(l1)

l1 = [1,8,7,2,21,15]
l1.append(8)
last_item = l1.pop()
print(last_item)
print(l1)

l1.remove(7)
print(l1) 

#write a program to store seven fruits in a list by the user
# Program to store seven fruits entered by the user

fruits = []

print("Enter the names of 7 fruits:")
for i in range(7):
    fruit = input(f" fruits {i+1} ")
    fruits.append(fruit)


print(fruits)
#write a program to accept marks of 6 students and display them in sorted manner
marks = []
print("enter the marks")
for i in range(6):
    mark = int(input(f" marks {i+1}"))
    marks.append(mark)
    print(marks)
    marks.sort()


# write a program to sum a list with 4 numbers.
numbers=[]
print("enter a number")
for i in range(4):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
print("\nThe numbers you entered:", numbers)
print("Sum of the numbers:", total)







