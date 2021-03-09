"""EX03 - prime functions."""

__author__: str = "730316868"



def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(5))
    print(list_prime(10, 20))
    print(is_prime(6))
    print(list_prime(25, 50))
    # ex. print(is_prime(5)), print(list_primes(10, 20))

def is_prime(x: int) -> bool:
    count: int = 2
    while count < x:
        if x % count == 0:
            return False
        count += 1  
    return True
    
def list_prime(first: int, last: int) -> list[int]:
    finalList: list[int] = []
    while first < last:
        if is_prime(first):
            finalList.append(first)
        first += 1
    return finalList
        




if __name__ == "__main__":
    main()