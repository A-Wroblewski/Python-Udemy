def is_number_or_dot(string):
    is_num_or_dot = False

    if string in '0123456789.':
        is_num_or_dot = True

    return is_num_or_dot
