import numpy as np
from data_holder import DataHolder


class Perceptron:

    def __init__(self, number_of_columns):
        self.weights = np.random.rand(number_of_columns, 1)
        self.threshold = 0

    def predict(self, x):
        pred = np.matmul(self.weights.T, x)[0] + self.threshold
        y_pred = int(pred > 0)
        return y_pred

    @staticmethod
    def check_data(data):
        if data.X is None or data.Y is None:
            raise ValueError('Missing data!')
        n_samples = len(data.Y)
        if n_samples != len(data.X):
            raise ValueError('Different dimensions in the data!')

    def train(self, train_data, max_iter=100, learning_rate=0.1):
        self.check_data(train_data)
        n_samples = len(data.Y)
        for i in range(max_iter):
            error = 0
            for x, y in zip(train_data.X, train_data.Y):
                y_pred = self.predict(x)
                err = y - y_pred
                if err != 0:
                    error += abs(err)
                    for n, v in enumerate(self.weights):
                        self.weights[n] = v + learning_rate*x[n]*err
            err_rate = error / n_samples
            print('Iteration {}:\n\terror rate: {} \n\taccuracy: {}'.format(i, err_rate, 1-err_rate))

    def test(self, test_data):
        n_samples = len(data.Y)
        self.check_data(test_data)
        error = 0
        for x, y in zip(test_data.X, test_data.Y):
            y_pred = self.predict(x)
            error += abs(y - y_pred)
        err_rate = error / n_samples
        return {'error rate': err_rate,
                'accuracy': 1-err_rate}


if __name__ == '__main__':
    print('sample1')
    data = DataHolder()
    data.read_data('sample1.csv')
    train, test = data.train_test_split()
    clf = Perceptron(train.get_number_of_columns())
    clf.train(train, learning_rate=0.01)
    print()
    print('Test results\n', clf.test(test))
    print('\n\n')
    print('sample2')
    data = DataHolder()
    data.read_data('sample2.csv')
    train, test = data.train_test_split()
    clf = Perceptron(train.get_number_of_columns())
    clf.train(train, learning_rate=0.01)
    print()
    print('Test results\n', clf.test(test))
    print('\n\n')
    print('sample3')
    data = DataHolder()
    data.read_data('sample3.csv')
    train, test = data.train_test_split()
    clf = Perceptron(train.get_number_of_columns())
    clf.train(train, learning_rate=0.01)
    print()
    print('Test results\n', clf.test(test))
