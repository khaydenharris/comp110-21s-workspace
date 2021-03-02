"""Coin Toss Comp 110 Project."""

from random import randint

_author_ = "730316868"


player: str
pet_points = 0
pet_questions = str(randint(1,3))
pet_needs = str("1, 2, 3")
pet_name: str
correct_rolls = 0
Random_roll = (randint(1, 6))
player_guess = int(randint(1, 6))
BIG_EYES: str = "\U0001F440"
points: int(correct_rolls + pet_points)


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    player_decision = input("doggy daycare, die, end game:")
    if player_decision == "doggy daycare":
        doggy_daycare()
    else:
        if player_decision == "die":
            die()
        else:
            ending()
    
    
def greet() -> None:
    """Function that greets the participant."""
    global player
    player = input("Enter Name:")
    print(f"What's up {player}, would you like to play doggy daycare, die, or end the program?")
    


def doggy_daycare() -> None:
    """Entrypoint to Interactive pet game."""
    global player
    print(f"What's up {player}, you picked my favorite game doggy daycare! Earn points by taking care of your dogs needs.")
    global pet_points
    pet_points = 0
    global pet_name
    pet_name = input("Enter Pet Name:")
    print(f"{pet_name} \U0001F436 needs a lot of TLC, I hope you're ready for this big responsibility.")
    pet_questions = str(randint(1, 3))
    if pet_questions == "1":
        print("I'm thirsty") 
    else:
        if pet_questions == "2":
            print("Lets go on a walk!")
        else:
            if pet_questions == "3":
                print("Can I have a treat?")
    player_response = str(input(f"Give {pet_name} water, treat, walk:"))
    if player_response == "water":
        global pet_needs
        pet_needs = "1"
    else:
        if player_response == "walk":
            pet_needs = "2"
        else:
            if player_response == "treat":
                pet_needs = "3"
    while pet_questions == pet_needs:
        pet_points += 1
        print(f"{pet_name} loves you \U0001F60A , so far you got {pet_points} pet points!")
        pet_questions = str(randint(1, 3))
        if pet_questions == "1":
            print("I'm thirsty") 
        else:
            if pet_questions == "2":
                print("Lets go on a walk!")
            else:
                if pet_questions == "3":
                    print("Can I have a treat?")
        player_response = str(input(f"Give {pet_name} water, treat, walk:"))
        if player_response == "water":
            pet_needs = "1"
        else:
            if player_response == "walk":
                pet_needs = "2"
            else:
                if player_response == "treat":
                    pet_needs = "3"
    print(f"{pet_name} is so sad \U0001F625 , but you accumulated a total of {pet_points} pet points.")
    print("Would you like to play again, play die or end the program?")
    player_decision = input("doggy daycare, die, end game:")
    if player_decision == "doggy daycare":
        doggy_daycare()
    else:
        if player_decision == "die":
            die()
        else:
            ending()


def die() -> None:
    """Entrypoint to the die guessing game."""
    global player
    print(f"What's up {player}, you picked the die game! All you gotta do is guess the correct roll.")
    global correct_rolls 
    correct_rolls = 0
    Random_roll = randint(1, 6)
    global player_guess
    player_guess = int(input("Enter numerical value 1-6:"))
    while Random_roll == player_guess:
        correct_rolls += 1
        print(f"I see you {BIG_EYES}!, you have {correct_rolls} so far.")
        Random_roll = int(randint(1, 6))
        player_guess = int(input("Enter numerical value 1-6:"))
    print(f"tough luck you rolled {correct_rolls} correctly.")
    print("Would you like to try again, play doggy daycare or end the program?")
    player_decision = input("doggyday care, die, end game:")
    if player_decision == "doggy daycare":
        doggy_daycare()
    else:
        if player_decision == "die":
            die()
        else:
            ending()


def ending() -> None:
    """An ending function that ends the program."""
    global player
    global pet_points
    global correct_rolls
    global points
    points = int(correct_rolls + pet_points)
    print(f"Congrats {player}! You finished with {points} total points!")
    print(f"Hate to see you go {player}. Have a great day!")


if __name__ == "__main__":
    main()