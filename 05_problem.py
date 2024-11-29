# Write a program to find the sum of first n natural numbers using while loop.

user_input = int(input("Enter a integer: ")) # 4

i = 1
sum = 0

while (i <= user_input):
    sum += i
    i += 1

print("The sum of first", user_input, "natural numbers is:", sum)

"""
Output:
The sum of first 4 natural numbers is: 10 - 1+2+3+4 = 10
"""