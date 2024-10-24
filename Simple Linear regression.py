# import matplotlib.pyplot as plt
#
# # Data
# X = [5, 1, 2, 1]
# Y = [25, 5, 7, 8]
#
# # Linear regression equation
# m = 4.72
# b = 0.63
# Y_pred = [m * x + b for x in X]
#
# # Plotting
# plt.scatter(X, Y, color='blue', label='Data points')
# plt.plot(X, Y_pred, color='red', label='Regression line')
# plt.xlabel('Salary')
# plt.ylabel('Expenditure')
# plt.legend()
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Week (X) and Sales (Y) data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([1.2, 1.5, 2.6, 3.2, 3.6])

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, Y)

# Predict the sales value for the 7th week
week_7 = np.array([[7]])
predicted_sales_week_7 = model.predict(week_7)
print(f"Predicted sales value for the 7th week: {predicted_sales_week_7[0]}")

# Plot the data and the regression line
plt.scatter(X, Y, color='blue', label='Actual Sales')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(week_7, predicted_sales_week_7, color='green', label='Predicted Sales (Week 7)')
plt.xlabel('Week')
plt.ylabel('Sales')
plt.legend()
plt.title('Linear Regression for Sales Prediction')
plt.show()
