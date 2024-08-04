def analyze_temperatures(temperature_readings):
    if not temperature_readings:
        return "No temperature readings provided"
    
    total_temp = 0
    highest_temp = temperature_readings[0]
    lowest_temp = temperature_readings[0]
    
    for temp in temperature_readings:
        total_temp += temp
        if temp > highest_temp:
            highest_temp = temp
        if temp < lowest_temp:
            lowest_temp = temp
    
    average_temp = total_temp / len(temperature_readings)
    
    return average_temp, highest_temp, lowest_temp

temperature_readings = list(map(int, input("Enter temperature readings separated by space: ").split()))

average_temperature, highest_temperature, lowest_temperature = analyze_temperatures(temperature_readings)

print(f"Average Temperature: {average_temperature:.1f}")
print(f"Highest Temperature: {highest_temperature}")
print(f"Lowest Temperature: {lowest_temperature}")
