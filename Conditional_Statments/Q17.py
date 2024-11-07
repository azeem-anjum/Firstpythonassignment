# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
num = int(input("Enter a number: "))
if (num%2 == 0):
    print("Yes is divisible: ")
elif (num % 3 == 0):
    print("Yes is divisible: ")
else:
    print("This is not divisible: ")
    