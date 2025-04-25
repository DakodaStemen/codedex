number = int(input("Enter number: "))
total = 0

for i in range(number + 1):
    square = i ** 2
    total = total + square

print(f"The sum of squares from 0 to {number} is {total}.")