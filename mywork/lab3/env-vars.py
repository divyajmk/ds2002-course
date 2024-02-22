#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

# Prompt User for Input
# Store in 4 Variables 
FAV_SPORT = input('What is your favorite sport? ')
UVA_YEAR = input('What is your UVA year standing? ')
FAV_FOOD = input('What is your favorite food? ' )
FAV_GENRE = input('What is your favorite genre of music? ')

# Set the Environment Variables 
os.environ["FAV_SPORT"] = FAV_SPORT
os.environ["UVA_YEAR"] = UVA_YEAR
os.environ["FAV_FOOD"] = FAV_FOOD
os.environ["FAV_GENRE"] = FAV_GENRE 

# Fetch and Print the Envrionment Variables 
print(os.getenv("FAV_SPORT"))
print(os.getenv("UVA_YEAR"))
print(os.getenv("FAV_FOOD"))
print(os.getenv("FAV_GENRE"))
