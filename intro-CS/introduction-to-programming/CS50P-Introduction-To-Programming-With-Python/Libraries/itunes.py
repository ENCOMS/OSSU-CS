#Twelve example: using get function from the requests library to get a json response.
'''
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())
'''

#Thirtieth example: using python own library json, to prettier our json response
'''
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json(), indent= 2))
'''

# Fourteenth example: using the result, and only taking what we want from the dictionary inside the response.

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# we change the limit to 50
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
