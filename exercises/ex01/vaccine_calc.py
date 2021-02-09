"""A vaccination calculator."""

__author__ = "730316868"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


Population: int = input("Population:")
Doses_administered: int = input("Doses administered:")
Doses_per_day: int = input("Doses per day:")
Target_percent_vaccinated: int = input("Target percent vaccinated:")



Doses_needed: int = round(int(Population) * float(0.01) * int(2) * int(Target_percent_vaccinated))
New_doses_needed: int = round(int(Doses_needed) - int(Doses_administered))
Number_of_days: int = round(int(New_doses_needed) / int(Doses_per_day)) 






today: datetime = datetime.today()
future_date: timedelta = timedelta(int(Number_of_days))
future: datetime = today + future_date



print("We will reach " + str(Target_percent_vaccinated) + "% vaccination in " + str(Number_of_days) + " days, which falls on " + str(future.strftime("%B %d, %Y")))










