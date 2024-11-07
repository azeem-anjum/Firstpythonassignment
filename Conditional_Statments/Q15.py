# Write a program to check if a number is within a specified range.
num = int(input("Enter a number: "))
minrange = int(input("Enter the minrange: "))
maxrange = int(input("Enter the mixrange: "))

if num >= minrange and num <= maxrange:
    print("num is within a spacified range.")
else:
    print("num is not a spacified range.")
