#  Use a loop to count the number of digits in an integer.
num = 65674654
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits: " + str(count))

