def weird_number(x):
    if not isinstance(x, (float, int, str)):
        raise TypeError("this function only accepts integers, floats and strings.")

    try:
        x = float(x)
    except ValueError:
        x = 0
    else:
        x = x ** 3
    finally:
        x = x + 1

    return x
