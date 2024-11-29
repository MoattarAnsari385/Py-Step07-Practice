# Write a program to print the following star pattern 

user_input = int(input("Enter the number: "))

for i in range(1, user_input + 1) :
    print(" " * (user_input - i), end="")
    print("*" * (2 * i -1), end="")
    print("")

