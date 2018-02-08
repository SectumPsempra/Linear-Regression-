from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionClass:

    def __init__(self, file_name):
        """
        :param file_name: Name of the file from where :var will be extracted.
        :var self.JEE_SCORE: JEE_SCORE created from Task.AVG_HRS_STUDIED and Task.PERCENT_IN_12TH_CLASS.
        :var self.PERCENT_IN_12TH_CLASS: Percentage of marks got in class 12th lies between 33-99.
        :var self.linearModel: linear regression model built-in support from sklearn.
        :var self.df: DataFrame created from csv file.
        :var self.model: initialize to self.
        :var self.predictions: initialize to self.
        """
        self.df = pd.read_csv(file_name, sep=',')
        self.JEE_SCORE = self.df['JEE_SCORE']
        self.PERCENT_IN_12TH_CLASS = self.df['PERCENT_IN_12TH_CLASS']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.JEE_SCORE,
                                                                                self.PERCENT_IN_12TH_CLASS,
                                                                                test_size=0.2)
        self.linearModel = linear_model.LinearRegression()
        self.model = self
        self.predictions = self

    def linear_regression(self):
        """
        :var self.model: creates linear regression model from train and test DataSet.
        :var self.predictions: Predict whether the created model gives the correct output as in X_test.
        :return score of accuracy.
        """
        self.X_train = (np.array(self.X_train)).reshape(800, 1)
        self.X_test = (np.array(self.X_test)).reshape(200, 1)

        self.model = self.linearModel.fit(self.X_train, self.y_train)
        self.predictions = self.linearModel.predict(self.X_test)

        return self.model.score(self.X_test, self.y_test), self.predictions


class PlotResult(LinearRegressionClass):

    def __init__(self, parent_instance):
        """
        :param parent_instance: Instance of LinearRegressionClass.
        :var self.predictions: Contains the predicted value from the linear regression model.
        :var self.modelAccuracy: Accuracy of the predicted value to the test data
        """
        self.modelAccuracy, self.predictions = parent_instance.linear_regression()
        self.y_test = parent_instance.y_test
        print(self.predictions, self.y_test)

    def print_score(self):
        """
        :return: prints the value of model's accuracy.
        """
        print "\n\nThe accuracy of the model is : ", self.modelAccuracy

    def plot(self):
        """
        :return: Plots the scatter chart of True value to predicted value, if True value if more
        than predicted value is also more in the chart.
        """
        plt.scatter(self.y_test, self.predictions)
        plt.xlabel("True Values")
        plt.ylabel("Predictions")
        plt.show()


linearRegInit = LinearRegressionClass('data_IIT.csv')
PlotResult(linearRegInit).plot()
PlotResult(linearRegInit).print_score()
