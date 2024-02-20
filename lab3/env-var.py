#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

os.environ["FAV_SPORT"] = "Soccer"
os.environ["UVA_YEAR"] = "Third"
os.environ["FAV_FOOD"] = "Pasta"

FAV_SPORT = input('What is your favorite sport? ')
UVA_YEAR = input('What is your UVA year standing? ')
FAV_FOOD = input('What is your favorite food? ' )

# Fetch the variables 
SPORT_ENV = os.getenv("FAV_SPORT")
UVA_YEAR = os.getenv("UVA_YEAR")
FAV_FOOD = os.getenv("FAV_FOOD")

# Print the Variables 
print(SPORT_ENV)
print(UVA_YEAR)
print(FAV_FOOD)