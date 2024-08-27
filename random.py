import random

def guess_number_game():
    
    number_to_guess = random.randint(1, 100)
    
    
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    
    while True:
        
        attempts += 1
        
        
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
            break


guess_number_game()
