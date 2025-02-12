characters = [
    {"class": "Warrior", "skill": "Berserk", "weapon": "Sword" },
    {"class": "Ninja", "skill": "Ambush", "weapon":("Dagger","Bow")},
    {"class": "Sura", "skill": "Flame Spirit", "weapon": "Sword"},
    {"class": "Shaman", "skill": "Dragon's Roar", "weapon": "Bell, Fan"}
]
# TODO, write this again
# create an empty dictionary to store the character weapons
character_weapons = {}

# iterate over the characters
for character in characters:
    # get the character name
    name = character["class"]
    # if character weapon is a string, split it and add the resulting list to the dictionary
    if isinstance(character["weapon"], str):
        character_weapons[name] = character["weapon"].split(", ")
    # if character weapon is a tuple or list, add it to the dictionary
    elif isinstance(character["weapon"], (tuple, list)):
        character_weapons[name] = character["weapon"]
# if character weapon is neither a string nor a tuple/list, add it to the dictionary as a single-item list
    else:
        character_weapons[name] = [character["weapon"]]

# print the character weapons
for name, weapons in character_weapons.items():
    print(f"{name}: {', '.join(weapons)}")

