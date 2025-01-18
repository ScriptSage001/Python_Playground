import random

input_to_value = {'s': -1, 'w': 0, 'g': 1}
value_to_name = {-1: 'Snake', 0: 'Water', 1: 'Gun'}
ascii_art = { -1: "Snake 🐍", 0: "Water 💧", 1: "Gun 🔫" }
winning_pairs = [(-1, 0), (0, 1), (1, -1)]


def get_user_choice():
    while True:
        choice = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
        if choice in input_to_value:
            return input_to_value[choice]
        print("Invalid choice! Try again.")


def play_round(user_score, computer_score):
    user_choice = get_user_choice()
    computer_choice = random.choice(list(value_to_name.keys()))
    print(f"Your choice: {ascii_art[user_choice]} | Computer's choice: {ascii_art[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
        return user_score, computer_score
    elif (user_choice, computer_choice) in winning_pairs:
        print("You win!")
        return user_score + 1, computer_score
    else:
        print("You lose!")
        return user_score, computer_score + 1


def main():
    user_score = 0
    computer_score = 0

    print('~~~ Welcome to the Snake-Water-Gun Game! ~~~')
    print('____________________________________________')

    while True:
        user_score, computer_score = play_round(user_score, computer_score)
        print(f"Scores: You - {user_score}, Computer - {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

    print("\nGame Summary:")
    print(f"You won: {user_score} times")
    print(f"Computer won: {computer_score} times")
    print(f"Draws: {user_score + computer_score - (user_score + computer_score)}")


if __name__ == "__main__":
    main()
