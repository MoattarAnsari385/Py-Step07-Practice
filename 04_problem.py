# Write a program to find whether a given number is prime or not.

user_inupt = int(input("Enter a number: "))

for i in range(2, user_inupt):
    if(user_inupt % i) == 0:
        print(user_inupt, "is not a prime number")
        break
else:
    print(user_inupt, "is a prime number")