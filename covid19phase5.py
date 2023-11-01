import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data from a CSV file (replace 'covid_data.csv' with your data file)
data = pd.read_csv('covid_data.csv')


date_column = 'date'
cases_column = 'total_cases'
data[date_column] = pd.to_datetime(data[date_column])


data = data.sort_values(by=date_column)


data['new_cases'] = data[cases_column].diff()

data['7_day_avg_new_cases'] = data['new_cases'].rolling(window=7).mean()


plt.figure(figsize=(12, 6))
plt.plot(data[date_column], data['new_cases'], label='Daily New Cases')
plt.plot(data[date_column], data['7_day_avg_new_cases'], label='7-Day Avg New Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Daily New Cases and 7-Day Average')
plt.legend()
plt.grid(True)
plt.show()
