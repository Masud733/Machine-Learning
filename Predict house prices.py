# A linear regression model to predict house prices based on features such as the number of bedrooms and the square footage.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#example data
np.random.seed(42)
num_sample = 100
X = 2* np.random.rand(num_sample, 1)
Y = 4+3*X + np.random.randn(num_sample, 1)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.2, random_state = 42)

#linear regression model
model = LinearRegression()
#Train the model on the training data
model.fit(X_train, y_train)

#Make prediction
y_pred = model.predict(X_test)

#Evaluating the model
ml = mean_squared_error(y_test,y_pred)
print(f"Mean square error: {ml}")

#plot the data
plt.scatter(X_test, y_test, color ='blue')
plt.plot(X_test, y_pred, color='red', linewidth=4)
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.title('Linear Regression Model')
plt.show()







