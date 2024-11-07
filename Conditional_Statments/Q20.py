# Create a program that evaluates if an inputted number is prime.
def operation(x):
    if x>1:
        for i in range(2, x):
            if (x%i)==0:
                print(x, "is not prime number: ")
                break
        else:
            print(x, "is a prime number: ")
