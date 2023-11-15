def weird_number(x):
    """Multiple operations with a value.

    This function performs multiple operations with a given value. First, tries
    to cast the value to a float. If it does not work, sets the value to `0`.
    If it works, sets the value its cube (power). After, adds one to the value.
    Finally, returns the value.

    Args:_
        x: the original value.

    Returns_
        x: the final value.

    """
    if not isinstance(x, (float, int, str)):
        raise TypeError(
            "this function only accepts integers, floats and strings."
        )

    try:
        x = float(x)
    except ValueError:
        x = 0
    else:
        x = x ** 3
    finally:
        x = x + 1

    return x
