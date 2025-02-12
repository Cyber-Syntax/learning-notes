# Count the number of occurrences(oluşumlar) of a specific character in a string

string = "Hello World!"

# Count the number of occurrences of the letter "o" in the string
count = string.count("o")

# Print the result
print(count)  # outputs 2

# cybersecurity example


# Analyze network traffic logs to identify potential security threats

# List of network traffic logs
logs = [
    "192.168.1.1 - - [10/Oct/2020:19:00:00 +0000] GET /index.html",
    "192.168.1.1 - - [10/Oct/2020:19:00:01 +0000] POST /login.php",
    "192.168.1.2 - - [10/Oct/2020:19:00:00 +0000] GET /index.html",
    "192.168.1.2 - - [10/Oct/2020:19:00:02 +0000] POST /login.php",
    "192.168.1.3 - - [10/Oct/2020:19:00:00 +0000] GET /index.html",
    "192.168.1.3 - - [10/Oct/2020:19:00:03 +0000] POST /login.php",
    "192.168.1.4 - - [10/Oct/2020:19:00:00 +0000] GET /index.html",
    "192.168.1.4 - - [10/Oct/2020:19:00:04 +0000] POST /login.php",
]

# Count the number of occurrences of each IP address in the logs
ip_counts = {}
for log in logs:
    ip = log.split()[0]
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

# Print the number of occurrences for each IP address
print(ip_counts)
