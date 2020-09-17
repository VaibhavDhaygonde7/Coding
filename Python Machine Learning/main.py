import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
#this will load the data of the diabetes which is already present in the module
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename']
# print(diabetes.keys())
#this will print what is present in the dataset diabetes
# print(diabetes.DESCR)   #this will print the description of the data

diabetes_x = diabetes.data
#this will return an array of array using numpy module
# print(diabetes_x)

#declaring the features
diabetes_x_train = diabetes_x[:-30]
#this will slice and take the last 30 features of the diabetes data
diabetes_x_test = diabetes_x[-20:]
#this will slice and take the first 20 features of the diabetes data

#declaring the labels
diabetes_y_train = diabetes.target[:-30]
#remember to take the labels as per the features declared because they are corresponding to each other
diabetes_y_test = diabetes.target[-20:]


#making our linear model
model = linear_model.LinearRegression()
#we are doing here linear regression

model.fit(diabetes_x_train, diabetes_y_train)
#this function is learning the data which is passed to it

diabetes_y_predicted = model.predict(diabetes_x_test)
#here we are testing our machine learning

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))
#mean_squared_error() first argument is the test values and the second argument is the predicted value

print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)

#plotting our values using matplotlib
# plt.scatter(diabetes_x_test, diabetes_y_test)
# plt.plot(diabetes_x_test, diabetes_y_predicted)
# plt.show()

# Mean squared error is:  2561.3204277283867
# Weights:  [941.43097333]
# Intercept:  153.39713623331698