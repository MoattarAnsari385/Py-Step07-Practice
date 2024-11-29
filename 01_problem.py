# Write a program to print multiplication table of a given number using for loop.

user_inupt = int(input("Enter a number: "))

for i in range (1, 11):
    print(f"{user_inupt} X {i} = {user_inupt * i}")
