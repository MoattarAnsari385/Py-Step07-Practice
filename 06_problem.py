# Write a program to calculate the factorial of a given number using for loop
# 5! = 1 x 2 x 3 x 4 x 5

user_input = int(input("Enter a number: "))
product = 1

for i in range(1, user_input + 1):
    product *= i

print(f"The factorial of {user_input} is {product}")