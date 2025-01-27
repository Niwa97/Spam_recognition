import numpy
import pandas
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier 
from sklearn.metrics import accuracy_score, balanced_accuracy_score, recall_score, confusion_matrix, ConfusionMatrixDisplay

########## PassiveAggressive ##########

dataframe = pandas.read_csv('drive/MyDrive/news.csv') #Reading the data
labels = dataframe.label
text = dataframe.text

x_train,x_test,y_train,y_test = train_test_split(text, labels, test_size = 0.12, random_state = 42, stratify = labels) #splitting train and test 

vectorizer = TfidfVectorizer(analyzer = 'word',  stop_words = 'english', max_df = 0.60) #converting documents to a of TF-IDF (Term Frequency — Inverse Data Frequency”.) matrix, using english stopwords list
train = vectorizer.fit_transform(x_train.values.astype('U')) #learning vocabulary, returning document-term matrix
test = vectorizer.transform(x_test.values.astype('U')) #transforming documents to document-term matrix

classifier = PassiveAggressiveClassifier(max_iter = 70, early_stopping = True)
classifier.fit(train, y_train.values.astype('U'))

y_pred = classifier.predict(test)

score = accuracy_score(y_test.values.astype('U'), y_pred)
score2 = balanced_accuracy_score(y_test.values.astype('U'), y_pred) 
score3 = recall_score(y_test.values.astype('U'), y_pred, average = 'macro', labels = ['FAKE','REAL'])  

print(f'Accuracy PAA: {round(score*100,4)}%')
print(f'Ballanced Accuracy PAA: {round(score2*100,4)}%')
print(f'Recall PAA: {round(score3*100,4)}%')

cm1 = confusion_matrix(y_test, y_pred, labels = ['FAKE','REAL'])

print(cm1)

print(f'\n')

########## Stochastic Gradient Descent ##########

dataframe2 = pandas.read_csv('drive/MyDrive/news.csv') #Reading the data
labels2 = dataframe2.label
text2 = dataframe2.text

x_train_2,x_test_2,y_train_2,y_test_2 = train_test_split(text2, labels2, test_size = 0.12, random_state = 42, stratify = labels2)

vectorizer2 = CountVectorizer(analyzer = 'word', stop_words = 'english', max_df = 0.60)
train2 = vectorizer2.fit_transform(x_train_2.values.astype('U')) #learning vocabulary, returning document-term matrix
test2 = vectorizer2.transform(x_test_2.values.astype('U')) #transforming documents to document-term matrix
classifier2 = SGDClassifier(alpha = 0.001, max_iter = 60, early_stopping = True) #stochastic gradient descent classifier with stronger regularisation term constant
classifier2.fit(train2, y_train_2)

y_pred_2 = classifier2.predict(test2)

score4 = accuracy_score(y_test_2, y_pred_2)
score5 = balanced_accuracy_score(y_test_2, y_pred_2) 
score6 = recall_score(y_test_2, y_pred_2, average = 'macro', labels = ['FAKE','REAL'])  

print(f'Accuracy SCD: {round(score4*100,4)}%')
print(f'Ballanced Accuracy SCD: {round(score5*100,4)}%')
print(f'Recall SCD: {round(score6*100,4)}%')

cm2 = confusion_matrix(y_test_2,y_pred_2, labels = ['FAKE','REAL'])

print(cm2)

print(f'\n')
