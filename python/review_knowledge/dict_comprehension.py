from pathlib import Path
from unittest.mock import MagicMock

names = ["config", "log"]

dict_return = {name: MagicMock(spec=Path) for name in names}

print(dict_return)
# OUTPUT
# {
#     'config': <MagicMock spec='Path' id='140276321371536'>,
#     'log': <MagicMock spec='Path' id='140276321371872'>
# }

horses = ["yıldırım", "beyazıt"]
ages = ["5", "10"]
# wrong logic I made up
# horse_return = {horse: ages for horse in horses}
# print(horse_return)
# OUTPUT
# # {'yıldırım': ['5', '10'], 'beyazıt': ['5', '10']}

horse_return = {horse: age for horse, age in zip(horses, ages)}
print(horse_return)
# OUTPUT
# {'yıldırım': '5', 'beyazıt': '10'}

horse_return2 = dict(zip(horses, ages))
print(horse_return2)
# OUTPUT
# {'yıldırım': '5', 'beyazıt': '10'}

# same logic written with for loop
horse_return3 = {}

for horse, age in zip(horses, ages):
    horse_return3[horse] = age  # assign key: value

print(horse_return3)
# OUTPUT
# {'yıldırım': '5', 'beyazıt': '10'}
