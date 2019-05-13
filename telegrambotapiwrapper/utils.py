# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

def is_str_int_float_bool(value):
    if isinstance(value, (int, str, float)):
        return True
    else:
        return False