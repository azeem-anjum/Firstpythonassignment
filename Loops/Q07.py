# Find the factorial of a number using a while loop.
num = int(input("Enter a factorial: "))
fact = 1
while (num>0):
    fact = fact*num
    num = num - 1

print("factorial number is ", fact)

