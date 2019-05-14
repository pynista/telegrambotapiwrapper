# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License


def is_str_int_float_bool(value):
    if isinstance(value, (int, str, float)):
        return True
    else:
        return False


def is_ends_with_underscore(value: str):
    if value == "":
        return False
    if value[-1] == '_':
        return True
    else:
        return False