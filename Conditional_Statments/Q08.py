# Create a program that checks if a given string is a palindrome.
value = input("Enter a value: ")
reversed_value = value[::-1]

if value == reversed_value:
    print("The number is Palindrome: ")
else:
    print("The number is not Palindrome: ")
