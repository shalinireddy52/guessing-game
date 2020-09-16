# guessing-game/game.py
import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congrats! You've guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_game()
