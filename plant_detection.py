# Make request to plant API and return a JSON string with correct information
import requests
from speech import *


# add a newly discovered plant to the list of discovered plants in discovered_plants.txt
def append_new_plant(plant):
    # check plant has not already been discovered
    discovered_plant_file = open("plant_files/discovered_plants.txt", "r")
    for found_plant in discovered_plant_file:
        found_plant = found_plant.replace("\n", "")
        if found_plant == plant:
            return
    discovered_plant_file.close()

    discovered_plant_file = open("plant_files/discovered_plants.txt", "a")
    discovered_plant_file.write("\n" + plant)
    discovered_plant_file.close()

    play("Wow, you discovered a new plant! Well done...")


# identify a plant from a given image file
def identify_plant(plant_image_file):
    # request plant identification from API
    api_url = "https://my-api.plantnet.org/v2/identify/all?nb-results=1&api-key=2b10nwoFz8ran5YoWa2QmvofPe"
    image = open(plant_image_file, 'rb')
    file = [('images', image)]
    response = requests.post(api_url, files=file, data={})
    result = response.json()

    # parse returned JSON
    try:
        species = (result['results'][0]['species']['scientificNameWithoutAuthor'])
        commonName = (result['results'][0]['species']['commonNames'][0])
        family = (result['results'][0]['species']['family']['scientificNameWithoutAuthor'])
        genus = (result['results'][0]['species']['genus']['scientificNameWithoutAuthor'])
    except:
        pass
    else:
        print(commonName)
        append_new_plant(commonName)
        play("You've found a " + commonName + "!")
        play(commonName + "s are part of the, " + family + ", family.")
