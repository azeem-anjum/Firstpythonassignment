# Check if a year input by the user is a century year.
inputyear = input("Enter year: ")
if(inputyear%100==0):
    print("This is century year: ")
else:
    print("This is not century year: ")
