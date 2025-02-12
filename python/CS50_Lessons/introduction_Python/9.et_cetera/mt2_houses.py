# characters, skills, name,
characters = [
    {"class": "Warrior", "skill": "Berserk", "weapon": "Sword" },
    {"class": "Ninja", "skill": "Ambush", "weapon":("Dagger","Bow")},
    {"class": "Sura", "skill": "Flame Spirit", "weapon": "Sword"},
    {"class": "Shaman", "skill": "Dragon's Roar", "weapon": ("Bell", "Fan")}
]
# create empty set to store characters
weapons = set()

# itarate over the characters
for character in characters:
    # if character weapon not in the weapons, add it on the set
    if not character["weapon"] in weapons:
        weapons.add(character["weapon"])
# TODO, solve dict printing problem.
# sort the weapons set and print the values
#for weapon in sorted(weapons):
  #  print(*weapons, "\n")

print("\n", weapons)