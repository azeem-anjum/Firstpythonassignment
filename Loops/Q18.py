# Use a loop to print numbers in reverse order within a given range.
# Function to print numbers in reverse order within a given range
def print_reverse_range(start, end):
    for number in range(end, start - 1, -1):
        print(number)


start = 1
end = 10

print("Numbers from  to  in reverse order:", start, end)
print_reverse_range(start, end)
