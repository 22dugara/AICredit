from django.templatetags.static import static
from django.db import models
import pandas as pd
import numpy as np
import keras
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
import os
import h5py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
dataset = pd.read_excel('static/json/LoanStats3a.xlsx').iloc[:400, 0:19].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
dataset[:, 12] = labelencoder.fit_transform(dataset[:, 12])

onehotencoder = OneHotEncoder(categorical_features = [1])
amountofdeleted = 0
for x in range(223):
    if dataset[x][12] == 1:
        if amountofdeleted < 200:
            dataset = np.delete(dataset, (x), axis=0)

yvar = dataset[:, 12]
f = yvar
f = np.array(f, dtype=np.float32)
print(f)
independentone = dataset[:, 0:6]
independenttwo = dataset[:, 9:12]
independentthree = dataset[:, 13:19]
X = dataset[:, 0:15]
for x in range(224):
    for y in range(6):
        X[x][y] = independentone[x][y]
    for y in range(3):
        X[x][y + 6] = independenttwo[x][y]
    for y in range(6):
        X[x][y + 9] = independentthree[x][y]

print("X")
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
print("X")
X[:, 3] = labelencoder_X_1.fit_transform(X[:, 3])
print("X")
X[:, 6] = labelencoder_X_1.fit_transform(X[:, 6])
print("X")
X[:, 8] = labelencoder_X_1.fit_transform(X[:, 8])
print("X")

onehotencoder = OneHotEncoder(categorical_features = [1])
print("X")
X = X[:, 0:9]
print(X[0][0])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 97:105]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, f, test_size = 0.2, random_state = 0)

import keras
from keras.models import Sequential
from keras.layers import Dense
classifier = Sequential()
classifier.add(Dense(units=5, activation="relu", input_dim=8, kernel_initializer="uniform"))
classifier.add(Dense(units=1, activation="sigmoid", kernel_initializer="uniform"))
classifier.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
classifier.fit(X_train,y_train,batch_size=10, epochs=2)
print(classifier.predict(np.matrix([10000, 79, 1 , 78, 1, 1, 1, 1]))[0][0])
def machinelearn(amountofmoney, term, interestrate, installment, homeowenership, income):

	amountofmoney = float(amountofmoney)
	interestrate = float(interestrate)
	installment = float(installment)
	income = float(income)
	if classifier.predict(np.matrix([amountofmoney, amountofmoney, 1 , interestrate, installment, 1, income, 1]))[0][0] > 1:
		response = 100
	if classifier.predict(np.matrix([amountofmoney, amountofmoney, 1 , interestrate, installment, 1, income, 1]))[0][0] < 1:
		response = classifier.predict(np.matrix([amountofmoney, amountofmoney, 1 , interestrate, installment, 1, income, 1]))[0][0] * 75
	return response

   

# evaluate loaded model on test data
