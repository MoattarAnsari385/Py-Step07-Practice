# Write a program that sums all the even numbers between 1 and a user-input value n using a while loop.

n = int(input("Enter a value: "))

sum = 0  # Initial sum should be 0
i = 1

while(i <= n): # The loop should go till n (inclusive)
    if( i % 2  == 0):
        sum += i
    i += 1

print("Sum of even numbers between 1 and", n, "is:", sum)