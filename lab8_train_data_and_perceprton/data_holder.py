import csv
import numpy as np


def read_data(path, y_col=-1, delimiter=';'):
    with open(path) as csvfile:
        data = csv.reader(csvfile, delimiter=delimiter)
        data = [d for d in data]
    data = np.asarray(data, dtype=float)
    Y = data[:, y_col]
    X = np.delete(data, y_col, 1)
    return DataHolder(X, Y)


class DataHolder:

    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.center_params = dict()
        self.normalize_params = dict()

    def get_number_of_columns(self):
        return self.X.shape[1]

    def center_rows(self):
        result = np.copy(self.X)
        r_min = result.min(1)
        for i in range(result.shape[1]):
            result[:, i] -= r_min
        r_max = result.max(1)
        r_max[r_max == 0] = 1
        for i in range(result.shape[1]):
            result[:, i] /= r_max
        return result

    def normalize_rows(self):
        result = np.copy(self.X)
        r_mean = result.mean(1)
        r_std = result.std(1)
        r_std[r_std == 0] = 1
        for i in range(result.shape[1]):
            result[:, i] -= r_mean
            result[:, i] /= r_std
        return result

    def fit_column_center(self, col_num):
        self.center_params[col_num] = dict()
        self.center_params[col_num]['min'] = self.X[:, col_num].min()
        self.center_params[col_num]['max'] = self.X[:, col_num].max()

    def fit_column_normalizer(self, col_num):
        self.normalize_params[col_num] = dict()
        self.normalize_params[col_num]['mean'] = self.X[:, col_num].mean()
        self.normalize_params[col_num]['std'] = self.X[:, col_num].std()

    def fit_all_column_centers(self):
        for i in range(self.X.shape[1]):
            self.fit_column_center(i)

    def fit_all_column_normalizers(self):
        print(self.X.shape[1])
        for i in range(self.X.shape[1]):
            print(i)
            self.fit_column_normalizer(i)

    def center_column(self, data=None, col_num=0):
        try:
            if data is None:
                data = self.X
            result = np.copy(data)
            result[:, col_num] -= self.center_params[col_num]['min']
            if self.center_params[col_num]['max'] != 0:
                result[:, col_num] /= self.center_params[col_num]['max']
        except KeyError as e:
            raise AttributeError('center for column not fitted yet!')
        return result

    def normalize_column(self, data=None, col_num=0):
        try:
            if data is None:
                data = self.X
            result = np.copy(data)
            result[:, col_num] -= self.normalize_params[col_num]['mean']
            if self.normalize_params[col_num]['std'] != 0:
                result[:, col_num] /= self.normalize_params[col_num]['std']
        except KeyError as e:
            raise AttributeError('normalizer for column not fitted yet!')
        return result

    def center_all_columns(self, data=None):
        if data is None:
            data = self.X
        result = np.copy(data)
        for i in range(data.shape[1]):
            result = self.center_column(result, i)
        return result

    def normalize_all_columns(self, data=None):
        if data is None:
            data = self.X
        result = np.copy(data)
        for i in range(data.shape[1]):
            result = self.normalize_column(result, i)
        return result

    def train_test_split(self, train_ratio=0.8):
        n_train = int(self.X.shape[0] * train_ratio)
        x_train, x_test = self.X[:n_train], self.X[n_train:]
        if self.Y is not None:
            y_train, y_test = self.Y[:n_train], self.Y[n_train:]
        else:
            y_train = y_test = None
        return DataHolder(x_train, y_train), DataHolder(x_test, y_test)
