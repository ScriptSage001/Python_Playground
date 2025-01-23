import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            return int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_guess(guess, random_number):
    if guess == random_number:
        return "correct"
    elif guess < random_number:
        return "low"
    else:
        return "high"

def play_game():
    random_number = generate_random_number()
    number_of_guesses = 0

    while True:
        guess = get_user_guess()
        number_of_guesses += 1
        result = check_guess(guess, random_number)

        if result == "correct":
            print(f"You guessed right! Number of guesses: {number_of_guesses}.")
            break
        elif result == "low":
            print("Too low.")
        else:
            print("Too high.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()