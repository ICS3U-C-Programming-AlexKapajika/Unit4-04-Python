#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 11, 2023
# This program guess the user number and generate until you the user guess correctly

import random


def main():
    # Setting a correct guess variable
    correct_guess = random.randint(0, 9)
    # Process to get and ask user for a random a number between 0 to 9 and the correct guess will tell you if is right or wrong
    while True:
        user_guess = input("Guess a number between 0 to 9 : ")

        try:
            user_guess = int(user_guess)

        except ValueError:
            print("Invalid input")

        # Output process
        else:
            if user_guess >= 0:
                if user_guess <= 9:
                    if user_guess == correct_guess:
                        print("The correct guess is {}".format(correct_guess))
                        break
                    else:
                        print("You guessed wrong, try again.")

                else:
                    print("Your number cannot be higher than 9")
            else:
                print("negative numbers are not a valid guess")


if __name__ == "__main__":
    main()
