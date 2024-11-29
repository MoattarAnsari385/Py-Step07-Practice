    # Write a program to print the following star pattern 

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if (i == 1 or i == n):
        print("*" * n, end="")  # Top or bottom line
    else:
        print("*", end="")  # Left edge
        print(" " * (n - 2), end="")  # Spaces in the middle
        print("*", end="")  # Right edge
    print("")
