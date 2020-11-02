def non_negative_int(x):
    i = int(x)
    if i < 0:
        raise ValueError('Negative values are not allowed')
    return i


def openable_file(path):
    try:
        open(path, "r+")
        return path
    except IOError as e:
        print("Could not open file! ")
        print(e)
        raise
