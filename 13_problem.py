# Write a program to print a right-angled triangle of stars where the number of stars in each row is equal to the row number (e.g., 1 star in the first row, 2 in the second, and so on).
user_input = int(input("Enter number: "))

for i in range(1, user_input + 1):
    print("*" * i)