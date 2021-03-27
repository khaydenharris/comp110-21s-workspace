"""EX03 - prime functions."""

__author__: str = "730316868"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(5))
    print(list_primes(10, 20))
    print(is_prime(6))
    print(list_primes(25, 50))
   

def is_prime(x: int) -> bool:
    """Function that determines prime numbers."""
    count: int = 2
    while count < x:
        if x % count == 0:
            return False
        count += 1  
    return True

    
def list_primes(first: int, last: int) -> list[int]:
    """Function that determines a list of prime numbers."""
    finalList: list[int] = []
    while first < last:
        if is_prime(first):
            finalList.append(first)
        first += 1
    return finalList
        

if __name__ == "__main__":
    main()