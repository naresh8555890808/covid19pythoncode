import random
import time

# Simulate IoT data collection
def collect_covid_data():
    # Simulate data from IoT sensors
    cases = random.randint(1, 100)
    deaths = random.randint(0, 10)
    return cases, deaths

# Initialize variables to store total data
total_cases = 0
total_deaths = 0

# Simulate data collection for 7 days
for day in range(1, 8):
    cases, deaths = collect_covid_data()
    
    # Display daily data
    print(f"Day {day}: Cases: {cases}, Deaths: {deaths}")
    
    # Accumulate total data
    total_cases += cases
    total_deaths += deaths
    
    # Simulate data collection delay
    time.sleep(1)

# Display total data
print("\nTotal Cases: ", total_cases)
print("Total Deaths: ", total_deaths)
