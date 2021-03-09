"""EX03 - palindromify function."""

__author__: str = "730316868"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("red", True))
    

def palindromify(x: str, y: bool) -> str:
    palindrome: str = str(x)
    if y == True:
        count: int = -1
        while count >= (-len(x)):
            palindrome += x[count]
            count -= 1
        return palindrome
    if y == False:
        count: int = -2
        while count >= (-len(x)):
            palindrome += x[count]
            count -= 1
    return palindrome


if __name__ == "__main__":
    main()