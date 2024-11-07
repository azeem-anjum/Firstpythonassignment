# Print all prime numbers between 1 and 50.
print("Prime numbers in interval",  "and",  "are:")
for num in range(1, 50 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num, end=" ")