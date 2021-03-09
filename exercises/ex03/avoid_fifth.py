"""EX03 - avoid_fifth function."""

__author__: str = "730316868"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Campbell's chicken noodle soup is delicious"))


def avoid_fifth(letters: str) -> str:
    no_e_string: str = ""
    for item in letters:
        if item == "e" or item == "E":
            pass
        else: 
            no_e_string += item
    return no_e_string
            




if __name__ == "__main__":
    main()