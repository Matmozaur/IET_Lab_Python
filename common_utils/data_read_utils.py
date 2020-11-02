import argparse


def non_negative_int(x):
    i = int(x)
    if i < 0:
        raise ValueError('Negative values are not allowed')
    return i


def openable_file(path):
    try:
        f = open(path, "r+")
        f.close()
        return path
    except IOError as e:
        print("Could not open file! ")
        raise e
