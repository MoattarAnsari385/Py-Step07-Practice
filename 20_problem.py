# Write a program to print a square of numbers where each row contains a user-defined number of integers, incrementing by 1.

n = int(input("Enter a value: "))
i = 1
row = 1
col = 1

while (row <= n):
    while (col <= n):
        print(i, end=" ")
        i += 1
        col += 1
    print()
    row += 1
    col = 1