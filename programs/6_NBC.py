
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
# Read the data
msg = pd.read_csv('NBC.csv', names=['message', 'label'])
# convert the labels to binary values, 0 = negative and 1 = positive
msg['labelnum'] = msg['label'].map({'pos': 1, 'neg': 0})
# assign the data to X and y
X = msg['message']
y = msg['labelnum']
# split the data into training and testing sets
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)
# create a CountVectorizer object and fit it to the training data to create a vocabulary
count_v = CountVectorizer()
V_Xtrain = count_v.fit_transform(Xtrain)
V_Xtest = count_v.transform(Xtest)
#Feature names
modifieddf = pd.DataFrame(V_Xtrain.toarray(), columns=count_v.get_feature_names_out())
print(modifieddf[0:3])
# create a Multinomial Naive Bayes model and fit it to the training data
model = MultinomialNB()
model.fit(V_Xtrain, ytrain)
pred = model.predict(V_Xtest)
# print the results
for doc, p in zip(Xtest, pred):
        print(doc,"->",'pos' if p  else 'neg')
# print the accuracy metrics
print('Accuracy Metrics: \n', classification_report(ytest, pred))
print('Confusion Matrix: \n', confusion_matrix(ytest, pred))
