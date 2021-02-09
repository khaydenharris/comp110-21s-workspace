"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730316868"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint



print("Your fortune cookie says...")

fortune = randint(1,4)

if (fortune == 1):
        print("God loves you")
else:
    if (fortune == 2):
        print("You is smart, you is Kind, and you is important.")
    else:
        if (fortune == 3):
            print("Trust the process.")
        else:
            print("Have a blessed day.")

print("Now, go spread positive vibes!")




     
    
