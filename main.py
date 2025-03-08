# Make request to plant API and return a JSON string with correct information
import requests
from speech import *

# request plant identification from API
api_url = "https://my-api.plantnet.org/v2/identify/all?nb-results=1&api-key=2b10nwoFz8ran5YoWa2QmvofPe"
image = open("assets/daffy.jpg", 'rb')
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
    play("You've found a " + commonName + "!")
    play(commonName + "'s are part of the " + family + " family and " + genus + "genus, and are known scientifically "
                                                                                "as " + species + ".")
