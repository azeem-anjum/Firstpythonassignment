# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
def check_temperature(temp):
    # Check if the temperature is freezing, moderate, or hot
    if temp <= 0:
        return "Freezing"
    elif 1 <= temp <= 25:
        return "Moderate"
    else:
        return "Hot"

# Get user input for temperature in Celsius
temperature = float(input("Enter the temperature in Celsius: "))

# Check the temperature category
category = check_temperature(temperature)

# Display the result
print(f"The temperature is {category}.")
