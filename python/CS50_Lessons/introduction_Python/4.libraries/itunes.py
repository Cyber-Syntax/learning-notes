import requests, sys, json

# if user didn't give name of the file and name of the band exit.
if len(sys.argv) != 2:
    sys.exit()

# Request itunes api to get band songs. 
# Write which band,singer to learn songs with sys.argv
response = requests.get("https://itunes.apple.com/search?entitiy=song&limit=10&term=" + sys.argv[1])

# Clear to other unnececary informations on the response.json
# It's javascript but json can be available most language like python, c, c++... 
o = response.json()

# response.json'un içindeki sonuçlar'a bak # Look results in response.json
for result in o["results"]:
    # print just track names
    print(result["trackName"])