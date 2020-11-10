def greatest_common_denominator(a: int, b: int):
    if a == 0:
        return b
    return greatest_common_denominator(b % a, a)


def positive_int(x: int):
    x = float(x)
    i = int(x)
    if i != x:
        raise TypeError('Wrong type of entities!')
    else:
        if i < 1:
            raise ValueError('Number is not a positive int!')
        return i


def validate_entities(entities, validation, expected_len=None):
    if expected_len is not None:
        if expected_len != len(entities):
            raise ValueError('Wrong number of entities!')
    return [validation(e) for e in entities]


def get_valid_user_input(message, validation, expected_len=None, sep=','):
    return validate_entities(input(message).split(sep), validation, expected_len)


def handle_gcd():
    try:
        a, b = get_valid_user_input("Type numbers separated by comma:\n", positive_int, 2, ',')
        return greatest_common_denominator(a, b)
    except (ValueError, TypeError) as e:
        print(e)
        print('Try again...')
        handle_gcd()


if __name__ == '__main__':
    print(handle_gcd())
