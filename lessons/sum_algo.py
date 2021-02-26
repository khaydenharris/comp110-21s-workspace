"""Examples of List and loop algorithm."""

def sum_algo(xs: list[int]) -> int:
    """Summation of inout list is returned."""
    #1. Initialize totla and index i to 0
    total: int = 0
    i: int = 0
    #2. While i is valid, meaning i < len(xs)
    while i < len(xs):
        #   2. True) Take xs[i] and add to total
        total += xs[i]
        #   2. True) Increase i by 1, moving it to the next index
        i += 1

    #2.Fakse) Result is stored in total variable
    return total