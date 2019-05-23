# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License


def replace_from__word(d: dict):
    """Заменить рекурсивно ключи в объекте from_ на from."""
    res = {}
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [replace_from__word(v) for v in d]

    for key, value in d.items():
        if key == 'from_':
            res['from'] = replace_from__word(d['from_'])
        else:
            res[key] = replace_from__word(d[key])
    return res


def replace_from_word(d: dict):
    """Заменить рекурсивно ключи в объекте from на from_."""
    res = {}
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [replace_from_word(v) for v in d]

    for key, value in d.items():
        if key == 'from':
            res['from_'] = replace_from_word(d['from'])
        else:
            res[key] = replace_from_word(d[key])

    return res


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
