# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License
import jsonpickle

from telegrambotapiwrapper import utils


def json_payload(args: dict) -> str:
    """Получить строку, содержащую объект для отправки к Telegram Bot Api.

    Args:
        args(dict): словарь с данными для отправки
    Returns:
        (строка): json-строка, содержащая объект который будет отправлен к Telegram Bot Api.
    """

    def remove_none_values(d):
        """Delete None values,"""
        if not isinstance(d, (dict, list)):
            return d
        if isinstance(d, list):
            return [remove_none_values(v) for v in d]
        return {
            k: remove_none_values(v)
            for k, v in d.items() if v is not None
        }

    jstr = jsonpickle.encode(args, unpicklable=False)
    py_obj = jsonpickle.decode(jstr)
    py_obj = remove_none_values(py_obj)
    py_obj = utils.replace_from__word(py_obj)
    jstr = jsonpickle.dumps(py_obj)
    return jstr
