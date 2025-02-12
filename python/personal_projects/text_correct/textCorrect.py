with open("text.txt", "r") as f:
    text = f.read()
    text = text.replace("\n", " ")

with open("new_text.txt", "w") as f:
    f.write(text)
