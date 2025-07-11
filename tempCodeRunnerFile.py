numbers=[]
print("enter a number")
for i in range(4):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

total = sum(numbers)