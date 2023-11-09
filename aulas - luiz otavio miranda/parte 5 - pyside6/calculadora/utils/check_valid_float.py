def is_valid_float(value):
    is_valid = False

    try:
        float(value)
        is_valid = True
    except ValueError:
        pass

    return is_valid
