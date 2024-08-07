import random


# Number Guessing Game in Python


def generate_random_number():
    number = random.randint(1, 100)

    return number


if __name__ == "__main__":
    random_number = generate_random_number()
    guesses = 0
    isPlaying = True

    while isPlaying:
        guessed_number = 0

        while guessed_number != random_number:
            try:
                guessed_number = int(input("Guess a number between 1 and 100: ").lower())

                if guessed_number > random_number:
                    print(f"{guessed_number} is too high")
                    guesses += 1
                elif guessed_number < random_number:
                    print(f"{guessed_number} is too low")
                    guesses += 1
                else:
                    guesses += 1
                    break
            except ValueError as e:
                print(f"Invalid Input! {e}")

        print("You win!")
        print(f"Number is {random_number}")
        print(f"Your guess is: {guessed_number}")
        print(f"Total guesses: {guesses}")
        response = input("Would you like to play again? (y/n) ")
        if response == "y":
            guesses += 1
            isPlaying = True
        else:
            isPlaying = False

    print("Thanks for playing the game. Good Bye!")
