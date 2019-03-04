import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


def preprocess():
    """Return the preprocessed data set"""
    data = pd.read_csv('weatherAUS.csv')

    # Drop certain features any any data with null values
    data = data.drop(['Sunshine', 'Evaporation', 'Cloud3pm',
                      'Cloud9am', 'Location', 'RISK_MM', 'Date'], axis=1)
    data = data.dropna(how='any')

    # Change labels
    data['RainToday'].replace({'No': 0, 'Yes': 1}, inplace=True)
    data['RainTomorrow'].replace({'No': 0, 'Yes': 1}, inplace=True)

    # Change categorical data to integers
    categorical_columns = ['WindGustDir', 'WindDir3pm', 'WindDir9am']
    data = pd.get_dummies(data, columns=categorical_columns)

    # standardize data set
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(data)
    data = pd.DataFrame(scaler.transform(data),
                        index=data.index, columns=data.columns)

    y = data.pop('RainTomorrow')
    X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2)
    return X_train, X_test, y_train, y_test


class LogisticRegression(object):
    def __init__(self):
        self.X_train, X_test, self.y_train, y_test = preprocess()

    # activation function
    def sigmoid(self, x):
        """Return the output of sigmoid fuction"""
        return 1 / (1 + np.exp(-x))

    # fit part
    def fit(self, X, y, learning_rate=0.01, epochs=32,
            batch_size=1, num_iter=100000):
        """Train the model using SGD"""
        # add intercept
        intercept = np.ones((X.shape[0], 1))
        X = np.concatenate((intercept, X), axis=1)
        y = np.array(y)
        # initialize weights
        self.beta = np.zeros(X.shape[1])
        # Utilizing SGD to do weight tuning
        for i in range(epochs):
            for j in range(num_iter):
                index = np.random.randint(0, len(X) - 1)
                z = np.dot(X[index], self.beta)
                r = self.sigmoid(z)
                gradient = (r - y[index]) * X[index]
                self.beta -= learning_rate * gradient

    # Prediction part
    def predict(self, X):
        """Return the prediction list"""
        # add intercept
        intercept = np.ones((X.shape[0], 1))
        X = np.concatenate((intercept, X), axis=1)
        predict_value = self.sigmoid(np.dot(X, self.beta))
        predict_value = np.array(list(map(lambda x: 1 if x > 0.5 else 0,
                                          predict_value)))
        return predict_value

    # Evaluate part
    def evaluate(self, X_test, y_test):
        """Returns a numpy array of prediction labels"""
        self.fit(self.X_train, self.y_train)
        predict_value = self.predict(X_test)
        return predict_value
    
    
    
    
    
    
