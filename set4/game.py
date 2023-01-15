import random as rd
import sys


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            continue


def guesser(goal):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess == goal:
                    print("Just right!")
                    sys.exit()
                elif guess > goal:
                    print("Too large!")
                else:
                    print("Too small!")
        except ValueError:
            continue


def main():
    goal = rd.randint(1, get_level())
    guesser(goal)


main()
