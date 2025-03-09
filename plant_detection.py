# Make request to plant API and return a JSON string with correct information
import requests
from speech import *


# add a newly discovered plant to the list of discovered plants in discovered_plants.txt
def append_new_plant(plant):
    # check plant has not already been discovered
    discovered_plants_file = open("plant_files/discovered_plants.txt", "r")
    for found_plant in discovered_plants_file:
        found_plant = found_plant.replace("\n", "")
        if found_plant == plant:
            return 0
    discovered_plants_file.close()

    # append new plants to the list of discovered ones
    discovered_plants_file = open("plant_files/discovered_plants.txt", "a")
    discovered_plants_file.write("\n" + plant)
    discovered_plants_file.close()

   # chime()
    play("Wow, you discovered a new plant Well done")
    return 1


# check if a newly discovered plant is rare
def check_plant_rarity(plant):
    rare_plants_file = open("plant_files/rare_plants.txt", "r")
    for rare_plant in rare_plants_file:
        rare_plant = rare_plant.replace("\n", "")
        rare_plant = rare_plant.split(", ")

        if rare_plant[0] == plant:
            rare_chime()
            play("You have found a rare plant")
            play("The " + plant + " " + rare_plant[1])
    rare_plants_file.close()

# identify a plant from a given image file
def identify_plant(plant_image_file):
    # request plant identification from API
    api_url = "https://my-api.plantnet.org/v2/identify/all?nb-results=1&api-key=2b10nwoFz8ran5YoWa2QmvofPe"
    image = open(plant_image_file, 'rb')
    file = [('images', image)]
    print("send query")
    response = requests.post(api_url, files=file, data={})
    result = response.json()
    print("got response")

    # parse returned JSON
    try:
        species = (result['results'][0]['species']['scientificNameWithoutAuthor'])
        commonName = (result['results'][0]['species']['commonNames'][0])
        family = (result['results'][0]['species']['family']['scientificNameWithoutAuthor'])
        genus = (result['results'][0]['species']['genus']['scientificNameWithoutAuthor'])
    except Exception as e:
        print("exception occurred")
        print(e.getMessage())
    else:
        print(commonName)
        new_plant = append_new_plant(commonName)
        play("You've found a " + commonName)
        play(commonName + "s are part of the " + family + " family.")

        if new_plant:
            check_plant_rarity(commonName)
