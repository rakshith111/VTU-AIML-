
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.20)
targets=iris.target_names

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
# OPTIONAL: print the predicted and actual values
for i in range(len(y_pred)):
    if targets[y_test[i]]== targets[y_pred[i]]:
        print('Lable is {} and prediction is {} and they are same'.format(targets[y_test[i]], targets[y_pred[i]]))
    else:
        print('Lable is {} and prediction is {} and they are different'.format(targets[y_test[i]], targets[y_pred[i]]))

print('Confusion matrix is as follows')
print(confusion_matrix(y_test, y_pred))
print('Accuracy Metrics')
print(classification_report(y_test, y_pred))
