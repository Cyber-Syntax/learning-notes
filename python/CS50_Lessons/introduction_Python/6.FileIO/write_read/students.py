with open("names.csv") as file:
    for line in file:
        # row = satır, column = sütun 
        #row = line.rstrip().split(",")       
        #print(f"{row[0]}, is in {row[1]}")
         name, house = line.rstrip().split(",")  
         print(f"{name}, is in {house}")