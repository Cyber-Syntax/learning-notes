# Define a list of temperature strings
temperatures = ["72.5", "69.1", "70.0", "68.6", "71.6", "72.8"]

# Convert the temperature strings to floating-point numbers
temperatures = [float(temp) for temp in temperatures]

# Calculate the average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Print the average temperature
print("Average temperature:", avg_temp)
