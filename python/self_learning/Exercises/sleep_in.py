def sleep_in(weekday, vacation):
    weekday = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
    vacation = {7: "Sunday"}
    workday = {6: "Saturday"}
    if not weekday or vacation:
        print("Sleep in")
    elif workday:
        print("Don't sleep in")
    else:
        print("Error")

if __name__ == "__main__":
    sleep_in(1, 6)
    