numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break


# Another example 

import requests
from bs4 import BeautifulSoup

url = "http://www.example.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

iterator = iter(links)

while True:
    try:
        link = next(iterator)
        print(link.get("href"))
    except StopIteration:
        break
