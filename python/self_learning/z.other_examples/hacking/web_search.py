import requests
from bs4 import BeautifulSoup

# Burada web bağlantıları teker teker taranır ve her bağlantı ekrana yazdırılır.
url = "http://www.example.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link.get("href"))
