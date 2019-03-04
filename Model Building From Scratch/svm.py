import matplotlib.pyplot as plt
import numpy as np
import scipy
import cvxpy as cp
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd


def preprocess():
    data = pd.read_csv('weatherAUS.csv')

    # Drop certain features any any data with null values
    data = data.drop(['Sunshine', 'Evaporation', 'Cloud3pm', 'Cloud9am', 
                      'Location', 'RISK_MM','Date'], axis=1)
    data = data.dropna(how='any')

    # Change labels
    data['RainToday'].replace({'No': 0, 'Yes': 1}, inplace = True)
    data['RainTomorrow'].replace({'No': -1, 'Yes': 1}, inplace = True)

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


class LinearSVM(object):
    """A support vector machine with linear kernel that trains using
       the primal convex minimization problem"""

    def __init__(self, C=1.0):
        self.C = C
        self.w = None
        self.b = None

    def train(self, X, y):
        """Use training arrays to set the values of self.w and self.b"""
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.DataFrame): 
            y = y.values
        y = np.array([-1 if x == 0 else 1 for x in y])
        nrows, ncols = np.shape(X)
        ζ = cp.Variable(nrows)
        # insert the correct length for w
        w = cp.Variable(ncols)
        b = cp.Variable()
        # use cp.sum_squares and cp.sum to form the objective function
        objective = cp.Minimize(0.5 * cp.sum_squares(w) + self.C * cp.sum(ζ))
        # apply the optimization constraints (hint: cp.multiply)
        constraints = [cp.multiply(y, X * w + b) >= 1 - ζ,
                       ζ >= 0]
        prob = cp.Problem(objective, constraints)
        prob.solve()
        self.w = w.value
        self.b = b.value

    def predict(self, X_test):
        """Return a numpy array of prediction labels"""
        if isinstance(X_test, pd.DataFrame):
            X_test = X_test.values
        predict = np.dot(X_test, self.w) + self.b
        predict = [1 if x >= 0 else 0 for x in predict]
        return np.array(predict)


def linear_kernel(a, b):
    """Return the data converted by linear kernel"""
    return np.dot(a, b.T)


def polynomial_kernel(a, b):
    """Return the data converted by polynomial kernel"""
    return (np.dot(a, b.T) + 1) ** 2


def rbf_kernel(a, b):
    """Return the data converted by RBF kernel"""
    return np.exp(-(np.dot(a, a.T) + np.dot(b, b.T) - 2 * np.dot(a, b.T)))


class SVM(object):
    def __init__(self, kernel=rbf_kernel, C=1.0):
        self.kernel = kernel
        self.C = C
        self.X = None
        self.y = None
        self.α = None
        self.b = None

    def train(self, X, y):
        """Use training arrays X and y to set the values of 
        self.α and self.b"""
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.DataFrame):
            y = y.values
        y = np.array([-1 if x == 0 else 1 for x in y])
        nrows, ncols = np.shape(X)
        α = cp.Variable(nrows)
        w = cp.Variable(ncols)
        # form a kernel matrix (as a numpy array)
        K = self.kernel(X, X)
        objective = cp.Minimize(1/2 * cp.quad_form(cp.multiply(α, y), K)
                                    - cp.sum(α))
        # list the constraints for the optimization problem
        constraints = [α >= 0,
                       α <= self.C,
                       α * y == 0]
        prob = cp.Problem(objective, constraints)
        prob.solve()
        self.X = X
        self.y = y
        # fill in the value of α
        self.α = α.value
        # fill in the value of b
        self.b = np.mean(y - np.dot(X, np.dot(X.T, self.α * self.y)))

    def predict(self, X_test):
        """Return a numpy array of prediction labels"""
        if isinstance(X_test, pd.DataFrame):
            X_test = X_test.values
        predict = np.dot(rbf_kernel(X_test, X_test), self.α * self.y) + self.b
        predict = [1 if x >= 0 else 0 for x in predict]
        return np.array(predict)
