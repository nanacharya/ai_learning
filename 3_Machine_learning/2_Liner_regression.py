import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


#Generating Synthetic Data
print("Generating Synthetic Data")

np.random.seed(42)
x= np.random.rand(100, 1) *100
print("x \n ", x)
y = 3 * x + np.random.randn(100, 1) *2
print( "y \n " , y)

#Split Data
print("Split Data")
print("Split Data")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("x_train \n" , x_train.shape)
print(("x_test \n" , x_test.shape))



#Fit Liner regression
model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

#Preditiction

print("Slope : " , model.coef_[0][0])
print("Intercept : " , model.intercept_[0])

plt.scatter(x_test, y_test, color="blue", label = "Actual")
plt.plot(x_test, y_pred, color="red", label="Predicted")

plt.title("Linear Regression Model")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


##Performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE : " , mse)
print("R-Squared :" , r2)
