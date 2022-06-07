import random

# THERE IS AN ISSUE WITH THIS CODE WHERE SOMETIMES NOBODY WINS

def player_1_turn(remaining_beans):
    if remaining_beans > 3:
        max_beans = 3
    else:
        max_beans = remaining_beans
    num_taken = random.randint(1, 3)
    remaining_beans -= num_taken
    return remaining_beans


def player_2_turn(remaining_beans):
    if remaining_beans > 3:
        max_beans = 3
    else:
        max_beans = remaining_beans
    num_taken = random.randint(1, 3)
    remaining_beans -= num_taken
    return remaining_beans


def main():
    num_beans = 15

    while num_beans > 0:
        num_beans = player_1_turn(num_beans)

        if num_beans >= 1:
            num_beans = player_2_turn(num_beans)
            if num_beans == 0:
                print("Player 2 wins!")
        else:
            print("Player 1 wins!")



if __name__ == "__main__":
    main()
