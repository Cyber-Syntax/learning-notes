import csv

name = input("name: ")
home = input("home: ")

with open("hogwart.csv", "a") as file:
    #writer = csv.writer(file)
    #writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
