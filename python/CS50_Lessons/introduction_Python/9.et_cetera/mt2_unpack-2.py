# Define function 
def total(lion_plate, full_moon_sword, yangs):
    # convert lion_plate and full_moon_sword to yangs and add the number of yangs
    return (lion_plate * 1 + full_moon_sword) + yangs

# create a list of yangs
_yangs: float = [12000,1000000,0] 

# format a number with a comma as a thousand seperator
# use the format() function
# format the full_moon_sword value with a comma as a 
# thousand separator using an f-string
full_moon_sword: float = 1000000
formatted_full_moon_sword = f"{full_moon_sword:,}"

print(total(*_yangs), "Yang_lists")
