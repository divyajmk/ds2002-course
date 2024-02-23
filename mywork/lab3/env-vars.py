#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

# Prompt User for Input
# Store in 3 Variables 
FAV_SPORT = input('What is your favorite sport? ')
FAV_FOOD = input('What is your favorite food? ' )
FAV_GENRE = input('What is your favorite genre of music? ')

# Set the Environment Variables 
os.environ["FAV_SPORT"] = FAV_SPORT
os.environ["FAV_FOOD"] = FAV_FOOD
os.environ["FAV_GENRE"] = FAV_GENRE 

# Fetch and Print the Envrionment Variables 
print(os.getenv("FAV_SPORT"))
print(os.getenv("FAV_FOOD"))
print(os.getenv("FAV_GENRE"))
