import numpy as np
from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error

house_area = np.array([[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]])
house_area.reshape(-1, 1)
house_area_train = house_area

house_price = np.array([[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]])
house_price.reshape(-1, 1)
house_price_train = house_price

model = linear_model.LinearRegression()

model.fit(house_area_train, house_price_train)

area = int(input("Enter the area of the house: "))
area_predict = np.array([[area]])
predicted_price = model.predict(area_predict)

# print("Mean squared error is: ", mean_squared_error(house_price_train, predicted_price))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)

print("The predicted price by the machine is ", predicted_price)