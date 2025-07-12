even_number = []
for i in range(5):
    num = int(input(f"Enter a number {i+1}: "))
    if num % 2 == 0:
        even_number.append(num)


print(even_number)