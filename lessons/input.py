"""A program to demonstrate user input and variables."""
from random import randint

Random_roll = str(randint(1, 2))
def main() -> None:
    die()

def die() -> None:
    global Random_roll
    Random_roll = str(randint(1, 2))




    if __name__ == "__main__":
        main()
