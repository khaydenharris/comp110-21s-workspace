"""EX03 - palindromify function."""

__author__: str = "730316868"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("red", True))
    

def palindromify(x: str, y: bool) -> str:
    """Palindrome Function."""
    palindrome: str = str(x)
    if y is True:
        count: int = len(x) - 1
        while count >= 0:
            palindrome += x[count]
            count -= 1
        return palindrome
    if y is False:
        count: int = len(x) - 2
        while count >= 0:
            palindrome += x[count]
            count -= 1
    return palindrome


if __name__ == "__main__":
    main()