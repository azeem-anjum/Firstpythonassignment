# Use nested loops to print a pyramid pattern of *.
rows = 6
for i in range(rows):
    for j in range(i):
        print("*", end=" ")
    print(" ")
    