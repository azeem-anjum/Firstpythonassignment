# Check if a string input is uppercase, lowercase, or a mix.
ch = input("Enter a character: ")
if (ch >='A' and ch <= 'Z'):
    print("Upper case: ")
elif (ch >= 'a' and ch <= 'z'):
    print("Lower case")
else:
    print("Mix case: ")
