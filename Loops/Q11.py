# Print the reverse of a given number.
print("Enter a number: ")
n = int(input())
rev = 0
while n>0:
    rem = n%10
    rev =(rev*10)+rem
    n = n//10
print("Reverse is ", rev)
