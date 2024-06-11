import random

def welcome_message():
    print("Welcome to Guess a Number game.")
    print("Please type 'exit' to exit the program.")

def get_user_guess():
    while True:
        user_input = input("Guess an integer number between 0 and 100: ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            return None
        if user_input.isdigit() and 0 <= int(user_input) <= 100:
            return int(user_input)
        else:
            print("Please enter a valid integer between 0 and 100.")

def play_game():
    welcome_message()
    
    while True:
        number_to_guess = random.randint(0, 100)
        
        while True:
            guess = get_user_guess()
            if guess is None:
                return
            
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print("Your guess is correct.")
                break
        
        play_again = input("Press Enter to play again, or type 'exit' to exit the program: ")
        if play_again.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            return

if __name__ == "__main__":
    play_game()
