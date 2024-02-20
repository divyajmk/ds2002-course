#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

FAV_SPORT = input('What is your favorite sport? ')
UVA_YEAR = input('What is your UVA year standing? ')
FAV_FOOD = input('What is your favorite food? ' )

# Fetch the variables 
os.environ["FAV_SPORT"] = FAV_SPORT
os.environ["UVA_YEAR"] = UVA_YEAR
os.environ["FAV_FOOD"] = FAV_FOOD

# Print the Variables 
print(FAV_SPORT)
print(UVA_YEAR)
print(FAV_FOOD)

