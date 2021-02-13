"""Tar Heels exercise redux as a structured program."""

__author__ = "730316868"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    ripXXI: int = int(input("Enter an int: "))
    print(tar_heels(ripXXI))


def tar_heels(ripXXI: int) -> str:
    """Tarheel divisibility function."""
    if (ripXXI % 2 == 0 and ripXXI % 7 == 0):
        return("TAR HEELS")
    else:
        if (ripXXI % 2 == 0):
            return("TAR")
        else:
            if(ripXXI % 7 == 0):
                return("HEELS")
            else:
                return("CAROLINA")



if __name__ == "__main__":
    main()
