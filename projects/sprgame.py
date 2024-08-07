import random


def play():
    user = input("Enter 's' for scissor, 'p' for paper, 'r' for rock and 'e' for exit the game: ")
    computer = random.choice(['s', 'p', 'r'])

    # exit the program
    if user == 'e':
        return 'exit'

    # choice of user
    if user == 's':
        print("You choose: scissor")
    elif user == 'p':
        print("You choose: paper")
    else:
        print("You choose: rock")

    # choice of computer
    if computer == 's':
        print("computer choose: scissor")
    elif computer == 'p':
        print("computer choose: paper")
    else:
        print("computer choose: rock")

    # logic for game
    if user == computer:
        return 'tie..'

    if is_winner(user, computer):
        return 'You won!'

    return 'You lost!'


# rule: r > s, s > p, p > r
def is_winner(player, opponent):
    # rule: r > s, s > p, p > r
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


while True:
    check = input("Welcome ot spr game, Do you wan play? (y/n): ")
    if check.lower() == 'y':
        result = play()
        print(result)
        if result == 'exit':
            break
    elif check.lower() == 'n':
        print("Good Bye!")
        break
    else:
        print("Invalid Input! please enter valid inputs")

