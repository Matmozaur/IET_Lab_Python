def non_negative_int(x):
    i = int(x)
    if i < 0:
        raise ValueError('Negative values are not allowed')
    return i


def openable_file(path):
    try:
        file = open(path, "r+") # odradzam przesłanianie nazw wbudowanych (tutaj: file - proszę popatrzeć co robi kolorowanie składni)
        return path
    except IOError as e:    # jeśli Pan obsłuży wyjątek, to skąd będzie Pan wiedział, że plik jest niepoprawny?
        print("Could not open file! ")
        print(e)
