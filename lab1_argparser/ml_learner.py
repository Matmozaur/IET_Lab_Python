import argparse

from common_utils.data_read_utils import openable_file, non_negative_int    # jest Pan wewnątrz pakietu, więc import musi być względny (w tym przypadku .. na początku, bo common_utils jest piętro wyżej)

parser = argparse.ArgumentParser()
parser.add_argument("train_data", type=openable_file)
parser.add_argument("test_data", type=openable_file)
parser.add_argument("-o", "--output_file", type=openable_file, default=None)
parser.add_argument("-m", "--model_file", type=openable_file, const='model.txt')    # default, nie const
parser.add_argument("algorithm", choices=['DNN', 'RNN', 'CNN'], help='list DNN, RNN, CNN (default: %(default)s)')   # to działa? argparse sam z siebie wypisuje dopuszczalne opcje
parser.add_argument("samples", type=non_negative_int)
parser.add_argument("n_layers", type=int, choices=[100, 150, 300], help='list 100, 150, 300 (default: %(default)s)')
args = parser.parse_args()
print(parser.parse_args())
