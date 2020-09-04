# install requests
# pip install requests

# import package
import requests

def starwars_char():
    number = input("Please choose a random number (1-83) :  ")
    link = 'https://swapi.dev/api/people/' + str(number) + '/'
    swapi_link = requests.get(link)
    starwars_character = swapi_link.json()
    print(starwars_character)
    
starwars_char()