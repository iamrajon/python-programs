import random


def number_guessing_game():
    print("Number Guessing Game:")

    min_range = 1
    max_range = 100
    is_playing = True

    while is_playing:
        number = random.randint(min_range, max_range)
        guess = 0
        guesses = 0

        while guess != number:
            try:
                guess = int(input(f"Guess a number between {min_range} and {max_range}: "))
                if min_range <= guess <= max_range:
                    if guess > number:
                        print(f"{guess} is too high.")
                    elif guess < number:
                        print(f"{guess} is too low.")
                    guesses += 1
                else:
                    print(f"Please enter a number between {min_range} and {max_range}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("Congratulations! You guessed the number.")
        print(f"Number is: {number}")
        print(f"Total guesses: {guesses}")

        play_again = input("Would you like to play again? (y/n): ").lower()
        is_playing = play_again == 'y'

    print("Thanks for playing the game!")


if __name__ == "__main__":
    number_guessing_game()
