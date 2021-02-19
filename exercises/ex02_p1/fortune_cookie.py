"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730316868"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Function that produces random fortunes."""
    fortune = randint(1, 4)
    if (fortune == 1):
        return("God loves you.")
    else:
        if (fortune == 2):
            return("You is smart, you is Kind, and you is important.")
        else:
            if (fortune == 3):
                return("Trust the process.")
            else:
                return("Have a blessed day.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()