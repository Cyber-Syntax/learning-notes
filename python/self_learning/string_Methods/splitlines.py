addresses = '123 Main Street\nSuite 200\nAnytown, USA 12345\n\n456 Maple Street\nSuite 100\nAnytown, USA 12345\n'

address_lines = addresses.splitlines()  # split the string into a list of lines

for line in address_lines:
    # parse the line and process the address data
    if 'Suite' in line:
        # this line represents the suite number of the address
        suite = line.split()[-1]  # extract the suite number from the line
    elif ',' in line:
        # this line represents the city, state, and zip code of the address
        city, state_zip = line.split(',')
        state, zip_code = state_zip.strip().split()
    else:
        # this line represents the street address
        street_address = line

# print the extracted address data
print('Suite:', suite)
print('Street Address:', street_address)
print('City:', city)
print('State:', state)
print('Zip Code:', zip_code)

