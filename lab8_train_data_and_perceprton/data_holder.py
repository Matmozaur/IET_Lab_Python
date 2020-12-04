import csv
from functools import wraps
import numpy as np


class DataHolder:

    def __init__(self, x=None, y=None):
        self.X = x
        self.Y = y

    def read_data(self, path, y_col=-1, delimiter=';'):
        with open(path) as csvfile:
            data = csv.reader(csvfile, delimiter=delimiter)
            data = [d for d in data]
        data = np.asarray(data, dtype=float)
        if y_col is not None:
            self.Y = data[:, y_col]
            self.X = np.delete(data, y_col, 1)
        else:
            self.X = data

    def get_number_of_columns(self):
        return self.X.shape[1]

    def check_none(self):
        if self.X is None:
            raise ValueError('Data must be pulled first!')

    def center_rows(self):
        self.check_none()
        for i in range(self.X.shape[1]):
            self.X[:, i] -= self.X.min(1)
            max_val = self.X.max(1)
            if max_val != 0:
                self.X[:, i] /= max_val

    def center_column(self, col_num):
        self.check_none()
        self.X[:, col_num] -= self.X[:, col_num].min()
        max_val = self.X[:, col_num].max()
        if max_val != 0:
            self.X[:, col_num] /= max_val

    def normalize_rows(self):
        self.check_none()
        for i in range(self.X.shape[1]):
            self.X[:, i] -= self.X.mean(1)
            std = self.X.std(1)
            if std != 0:
                self.X[:, i] /= std

    def normalize_column(self, col_num):
        self.check_none()
        self.X[:, col_num] -= self.X[:, col_num].mean()
        std = self.X[:, col_num].std()
        if std != 0:
            self.X[:, col_num] /= std

    def train_test_split(self, train_ratio=0.8):
        self.check_none()
        n_train = int(self.X.shape[0] * train_ratio)
        x_train, x_test = self.X[:n_train], self.X[n_train:]
        if self.Y is not None:
            y_train, y_test = self.Y[:n_train], self.Y[n_train:]
        else:
            y_train = y_test = None
        return DataHolder(x_train, y_train), DataHolder(x_test, y_test)
