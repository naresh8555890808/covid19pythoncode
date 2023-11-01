import pandas as pd

# Sample COVID-19 dataset (replace with your data)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Cases': [100, 150, 200, 250],
    'Deaths': [5, 10, 15, 20],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("COVID-19 Data:")
print(df)

# Calculate total cases and deaths
total_cases = df['Cases'].sum()
total_deaths = df['Deaths'].sum()

# Print the total cases and deaths
print("\nTotal Cases:", total_cases)
print("Total Deaths:", total_deaths)
