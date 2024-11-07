# Write a program that continues to ask for a number until the correct number is guessed.

def guess_the_number():
    # Let's assume the correct number is 42
    correct_number = 42
    
    while True:
        # Ask the user to enter a number
        user_guess = input("Guess the number: ")
        
       
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_guess == correct_number:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            print("Incorrect guess. Try again.")


guess_the_number()
