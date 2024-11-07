# Write a program to print the first 10 Fibonacci numbers.
length = 10
n1, n2 = 1, 2
count = 0
while count<length:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
     