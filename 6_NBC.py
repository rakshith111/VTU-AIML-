
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import pandas as pd

msg = pd.read_csv('NBC.csv', names=['message', 'label'])
msg['labelnum'] = msg['label'].map({'pos': 1, 'neg': 0})

X = msg['message']
y = msg['labelnum']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

count_v = CountVectorizer()
Xtrain_v = count_v.fit_transform(Xtrain)
Xtest_v = count_v.transform(Xtest)

df = pd.DataFrame(Xtrain_v.toarray(), columns=count_v.get_feature_names_out())
print(df[0:3])

model = MultinomialNB()
model.fit(Xtrain_v, ytrain)
pred = model.predict(Xtest_v)

for doc, p in zip(Xtrain, pred):
        print(doc,"->",'pos' if p  else 'neg')

print('Accuracy Metrics: ')
print('Accuracy: ', accuracy_score(ytest, pred))
print('Recall: ', recall_score(ytest, pred))
print('Precision: ', precision_score(ytest, pred))
print('Confusion Matrix: \n', confusion_matrix(ytest, pred))
