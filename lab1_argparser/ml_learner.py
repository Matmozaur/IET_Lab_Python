import argparse

from common_utils.data_read_utils import openable_file, non_negative_int

parser = argparse.ArgumentParser()
parser.add_argument("train_data", type=openable_file)
parser.add_argument("test_data", type=openable_file)
parser.add_argument("-o", "--output_file", type=openable_file, default=None)
parser.add_argument("-m", "--model_file", type=openable_file, const='model.txt')
parser.add_argument("algorithm", choices=['DNN', 'RNN', 'CNN'], help='list DNN, RNN, CNN (default: %(default)s)')
parser.add_argument("samples", type=non_negative_int)
parser.add_argument("n_layers", type=int, choices=[100, 150, 300], help='list 100, 150, 300 (default: %(default)s)')
args = parser.parse_args()
print(parser.parse_args())
