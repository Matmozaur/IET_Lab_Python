import csv
from functools import wraps # nigdzie Pan nie używa, a można by
import numpy as np


class DataHolder:

    def __init__(self, x=None, y=None):
        self.X = x
        self.Y = y
        self.center_params = dict()
        self.normalize_params = dict()

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

    def check_none(self):   # _check_none
        if self.X is None:
            raise ValueError('Data must be pulled first!')  # to czemu konstruktor tego nie robi?

    def center_rows(self):
        self.check_none()
        result = np.copy(self.X)
        for i in range(result.shape[0]):
            result -= result.min(1)
            max_val = result.max(1)
            if max_val != 0:
                result[:, i] /= max_val # to rows, czy columns?
        return result

    def normalize_rows(self):
        self.check_none()
        result = np.copy(self.X)
        for i in range(result.shape[0]):
            result[:, i] -= result.mean(1)
            std = result.std(1)
            if std != 0:
                result[:, i] /= std
        return result

    def fit_column_center(self, col_num):
        self.check_none()
        self.center_params[col_num] = {'min': self.X[:, col_num].min()}
        self.center_params[col_num]['max'] = self.X[:, col_num].max()

    def fit_column_normalizer(self, col_num):
        self.check_none()
        self.normalize_params[col_num] = {'mean': self.X[:, col_num].mean()}
        self.normalize_params[col_num]['std'] = self.X[:, col_num].std()

    def fit_all_column_centers(self):
        for i in range(self.X.shape[1]):
            self.fit_column_center(i)

    def fit_all_column_normalizers(self):
        print(self.X.shape[1])
        for i in range(self.X.shape[1]):
            print(i)
            self.fit_column_normalizer(i)

    def center_column(self, data, col_num): # można jako wartość domyślną data przyjmować self.X
        result = np.copy(data)
        result[:, col_num] -= self.center_params[col_num]['min']    # a jeśli 'min' nie jest ustawione?
        if self.center_params[col_num]['max'] != 0:
            result[:, col_num] /= self.center_params['max']
        return result

    def normalize_column(self, data, col_num):
        result = np.copy(data)
        result[:, col_num] -= self.normalize_params[col_num]['mean']
        if self.normalize_params[col_num]['std'] != 0:
            result[:, col_num] /= self.normalize_params[col_num]['std']
        return result

    def center_all_columns(self, data):
        result = np.copy(data)
        for i in range(data.shape[1]):
            result = self.center_column(result, i)
        return result

    def normalize_all_columns(self, data):
        result = np.copy(data)
        for i in range(data.shape[1]):
            result = self.normalize_column(result, i)
        return result

    def train_test_split(self, train_ratio=0.8):
        self.check_none()
        n_train = int(self.X.shape[0] * train_ratio)
        x_train, x_test = self.X[:n_train], self.X[n_train:]
        if self.Y is not None:
            y_train, y_test = self.Y[:n_train], self.Y[n_train:]
        else:
            y_train = y_test = None
        return DataHolder(x_train, y_train), DataHolder(x_test, y_test)

# nie udało mi się nic zrobić z wczytanymi danymi, żeby nie poleciał wyjątek
