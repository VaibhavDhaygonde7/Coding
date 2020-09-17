from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

features = iris.data     #these are the features of the program
labels = iris.target     #these are the labels of the program
# print(iris.DESCR)
print(features[0], labels[0])

# Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[1, 1, 1, 1]])
print(preds)