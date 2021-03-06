

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection._validation import cross_val_score
from sklearn.model_selection._split import LeaveOneOut
from sklearn.model_selection import validation_curve

class KNN:
    def __init__(self, dataset, neighbors, x1 = None, x2 = None, y1 = None, y2 = None, cross_validation = True, folds = 0):
        self.data = dataset
        self.x = dataset.data
        self.y = dataset.target
        self.is_cross_validation = cross_validation
        if cross_validation is not True:
            self.split_data()
        else:
            self.folds = folds
        self.neighbors = neighbors if neighbors is not None else 1
        self.model = KNeighborsClassifier(n_neighbors = self.neighbors)
        
    def split_data(self):
        self.x1, self.x2, self.y1, self.y2 = train_test_split(self.x, self.y, random_state = 0, train_size = 0.5)

    def train(self, x = None, y = None):
        self.model.fit(x, y)

    def predict(self, target):
        self.y_model = self.model.predict(target)
        return self.y_model

    def score(self, target):
        return accuracy_score(target, self.y_model)

    def holdout_validation(self):
        self.train(self.x1, self.y1)
        self.y2_model = self.model.predict(self.x2)
        return accuracy_score(self.y2, self.y2_model)

    def cross_validation(self, folds = None):
        if folds is None:
            y2_model = self.model.fit(self.x1, self.y1).predict(self.x2)
            y1_model = self.model.fit(self.x2, self.y2).predict(self.x1)
            return [accuracy_score(self.y1, y1_model), accuracy_score(self.y2, y2_model)]
        else:
            return cross_val_score(self.model, self.x, self.y, cv = folds)

    def cross_validation_leave_one(self):
        return cross_val_score(self.model, self.x, self.y, cv = LeaveOneOut())

    def validate(self):
        neighbors = np.arange(1, 10)
        train_score, val_score = validation_curve(self.model, self.x, self.y, 'n_neighbors', neighbors, cv = 5)
        plt.plot(neighbors, np.median(train_score, 1), color = 'blue', label = 'training score')
        plt.plot(neighbors, np.median(val_score, 1), color = 'red', label = 'validation score')
        plt.ylim(0, 1)
        plt.xlabel('neighbors')
        plt.ylabel('score')
        plt.legend(loc = 'best')
        plt.show()
        return True
