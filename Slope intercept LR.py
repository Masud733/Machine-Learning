import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = {
    'year': [2015, 2016, 2017, 2018, 2019, 2020],
    'per_capita_income': [10000, 11000, 12000, 13000, 14000, 15000]
}
df = pd.DataFrame(data)
# Extracting 'year' and 'per_capita_income' columns
x = df['year']
y = df['per_capita_income']

# Performing Linear Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

# Predicting per capita income for the year 2024
year_2024 = 2024
predicted_per_capita_2024 = slope * year_2024 + intercept
print(f"Predicted per capita income for 2024: {predicted_per_capita_2024}")

# Plotting the data and the regression line
plt.scatter(x, y, label='Data points')
plt.plot(x, slope*x + intercept, color='red', label='Regression line')
plt.scatter([year_2024], [predicted_per_capita_2024], color='green', label='Prediction for 2024')
plt.xlabel('Year')
plt.ylabel('Per Capita Income')
plt.title('Linear Regression of Year vs. Per Capita Income')
plt.legend()
plt.show()



