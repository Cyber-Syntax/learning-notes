# Use a web scraping library to extract the product prices from a webpage
prices = scrape_page('http://www.example.com')

# Convert the extracted data into a list using the list() function
price_list = list(prices)

# Use the min() function to find the cheapest price
cheapest_price = min(price_list)

# Display the cheapest price
print("The cheapest price is: " + str(cheapest_price))
