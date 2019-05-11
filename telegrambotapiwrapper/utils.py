def is_str_int_float_bool(value):
    if isinstance(value, (int, str, float)):
        return True
    else:
        return False