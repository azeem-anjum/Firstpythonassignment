# Create a program that simulates a countdown timer starting from a given number down to zero.
import time

# Function to simulate the countdown timer
def countdown_timer(start):
    while start >= 0:
        print(start)
        time.sleep(1)  # Pause for 1 second before printing the next number
        start -= 1  # Decrease the countdown by 1
    print("Countdown finished!")


start_number = 10  
print(f"Starting countdown from {start_number}:")
countdown_timer(start_number)
