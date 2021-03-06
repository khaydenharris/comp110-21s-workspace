"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730316868"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    Population: int = int(input("Population: "))
    Doses_administered: int = int(input("Doses administered: "))
    Doses_per_day: int = int(input("Doses per day: "))
    Target_percent: int = int(input("Target percent vaccinated: "))
    N_of_days: int = days_to_target(Population, Doses_administered, Doses_per_day, Target_percent)
    future: str = future_date(N_of_days)
    print("We will reach " + str(Target_percent) + "% vaccination in " + str(N_of_days) + " days, which falls on " + str(future))


def days_to_target(Population: int, Doses_administered: int, Doses_per_day: int, Target_percent: int) -> int:
    """A Function that calculates the number of days gone by at target percent vaccination."""
    Doses_needed: int = round(int(Population) * float(0.01) * int(2) * int(Target_percent))
    New_doses_needed: int = round(int(Doses_needed) - int(Doses_administered))
    N_of_days: int = round(int(New_doses_needed) / int(Doses_per_day)) 
    return N_of_days


def future_date(N_of_days: int) -> str:
    """A function that calculates future date at target percent vaccination."""
    today: datetime = datetime.today()
    future_date: timedelta = timedelta(int(N_of_days))
    future: datetime = today + future_date
    return future.strftime("%B %d, %Y")
 

if __name__ == "__main__":
    main()
