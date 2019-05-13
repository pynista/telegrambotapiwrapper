# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

import inspect
import pprint
from telegrambotapiwrapper.static import METHODS_RETURN_TYPES

import telegrambotapiwrapper.api.methods as methods_module
import re
import telegrambotapiwrapper.api.types as types_module

CLASS_FROM_TYPES_REGEXP = re.compile(r"^<class '(.+)'>$")

def get_all_used_types():
    res = []
    for name, obj in inspect.getmembers(types_module):
        if inspect.isclass(obj):
            if 'types.Base' not in str(obj):
                mo = re.search(CLASS_FROM_TYPES_REGEXP, str(obj))
                res.append(mo.group(1))

    res = set(tp.split('.')[-1] for tp in res)

    return res

def get_all_used_methods():
    res = []
    for name, obj in inspect.getmembers(methods_module):
        if inspect.isclass(obj):
            if 'methods.Base' not in str(obj):
                mo = re.search(CLASS_FROM_TYPES_REGEXP, str(obj))
                res.append(mo.group(1))

    res = set(tp.split('.')[-1] for tp in res)

    return res



def union_anotations_in_methods_module():
    res = set()
    res.update(methods_annos())
    res = [anno for anno in res if 'Union' in anno]
    return sorted(set(res))


def types_annos():
    """Получить все используемые аннотации для типов."""
    res = set()
    for tp in get_all_used_types():
        if tp == "Base":
            continue
        type_ = getattr(types_module, tp)
        res.update(type_._used_annotations())
    return sorted(res)

def methods_annos():
    """Получить все используемые аннотации для методов."""
    res = set()
    for tp in get_all_used_methods():
        if tp == "Base":
            continue
        type_ = getattr(methods_module, tp)
        res.update(type_._used_annotations())
    return res

def get_all_used_annotations():
    """Получить абсолютно все используемые аннотации."""
    res = set()
    res.update(types_annos())
    res.update(methods_annos())
    res.update(get_annotations_of_returned_values_all_methods())
    return res


def get_annotations_of_returned_values_all_methods():
    """Получить аннотации возвращаемых значений методами."""
    res = set(METHODS_RETURN_TYPES.values())
    return res



def lower_first_letter(word: str):
    return  word[0].lower() + word[1:]

if __name__ == '__main__':
    print('{')
    for anno in union_anotations_in_methods_module():
        print("'" + anno + "'" + ',')
    print('}')
