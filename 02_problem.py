# Write a program to greet all the person names stores in the list 'l' and which start with S.
l = ["Ali", "Sara", "Zain", "Samir", "Nadia", "Sadiq", "Farhan", "Sana", "Ayesha", "Shayan"]

for name in l:
    if (name.startswith('S')):
        print(f"Hello, {name}!")