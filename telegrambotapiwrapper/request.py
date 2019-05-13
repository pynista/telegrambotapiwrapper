# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

import jsonpickle
from telegrambotapiwrapper.api.types import *


def json_payload(args: dict) -> str:
    """Получить строку, содержащую объект для отправки к Telegram Bot Api.

    Args:
        args(dict): словарь с данными для отправки
    Returns:
        (строка): json-строка, содержащая объект который будет отправлен к Telegram Bot Api.
    """
    def remove_none_values(d: dict):
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
    jstr = jsonpickle.dumps(py_obj)
    return jstr

if __name__ == '__main__':
    btn1 = InlineKeyboardButton(text='add', url='http://lenta.ru')
    btn2 = InlineKeyboardButton(text='sub', url='http://topwar.ru')
    btn3 = InlineKeyboardButton(text='mul', url='http://waralbum.ru')
    btn4 = InlineKeyboardButton(text='div', url='http://antio.ru')
    inline_kb = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4]])

    payload = json_payload({'chat_id':-1912345677, 'text':'test',  'reply_markup':inline_kb})
    print(payload)

