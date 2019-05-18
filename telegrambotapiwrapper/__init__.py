# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

import inspect
from pprint import pprint

import requests

from telegrambotapiwrapper.annotation import AnnotationWrapper
from telegrambotapiwrapper.api.types import *
from telegrambotapiwrapper.errors import *
from telegrambotapiwrapper.request import json_payload
from telegrambotapiwrapper.response import to_api_type, handle_response


class ApiBase:
    def __init__(self, token: str):
        self.token = token

    def _get_caller_method_name(self):
        """Получить имя метода, внутри которой была вызван данный метод."""
        caller_method_name = inspect.stack()[1][3]
        return caller_method_name

    @staticmethod
    def _get_tg_api_method_name(py_style_method_name):
        """Get Telegram API method name from python method name."""
        res = py_style_method_name.replace("_", " ").title().replace(" ", "")
        res = res[0].lower() + res[1:]
        return res

    def _get_tg_api_method_url(self, api_method_name: str):
        """Get method url."""
        return "https://api.telegram.org/bot{}/{}".format(
            self.token, api_method_name)

    @classmethod
    def _get_caller_func_return_type(cls):
        """Получить возврашаемого значения функции из которой была вызвана данная функция."""
        caller_method_name = inspect.stack()[1][3]
        return inspect.signature(getattr(cls,
                                         caller_method_name)).return_annotation

    def _get_caller_of_caller_func_args(self) -> dict:
        """Получить аргументы функции, внутри которой была вызвана данная функция."""
        currframe = inspect.currentframe()
        callercallerframe = inspect.getouterframes(currframe, 1)
        args, _, _, values = inspect.getargvalues(callercallerframe[2][0])

        res = {}
        for par in args:
            if par == "self":
                continue
            else:
                res[par] = values[par]
        return res

    @staticmethod
    def _get_caller_func_args() -> dict:
        """Получить аргументы функции, внутри которой была вызвана данная функция."""
        currframe = inspect.currentframe()
        callerframe = inspect.getouterframes(currframe, 2)
        args, _, _, values = inspect.getargvalues(callerframe[1][0])
        res = {}
        for par in args:
            if par == "self":
                continue
            # TODO: перевроверить ао ли проверяить
            else:
                res[par] = values[par]
        return res

    @classmethod
    def _get_caller_method_return_type(cls):
        caller_method_name = inspect.stack()[1][3]
        return inspect.signature(getattr(cls,
                                         caller_method_name)).return_annotation

    def _get_caller_caller_func_return_type(self) -> AnnotationWrapper:
        """Получить аннотацию возврашаемого значения функции из которой была вызвана данная функция."""
        caller_caller_name = (inspect.stack()[2][3])
        signature = inspect.signature(getattr(self, caller_caller_name))
        annotation = signature.return_annotation
        anno_wrapper = AnnotationWrapper(annotation)
        return anno_wrapper.sanitized

    def _get_caller_caller_func_name(self):
        return inspect.stack()[2][3]

    def _make_request(self):
        result_type = self._get_caller_caller_func_return_type()
        caller_caller_args = self._get_caller_of_caller_func_args()
        payload = json_payload(caller_caller_args)
        caller_caller_name = self._get_caller_caller_func_name()
        tg_method_name = self._get_tg_api_method_name(caller_caller_name)
        url = self._get_tg_api_method_url(tg_method_name)
        r = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
        return handle_response(r.content.decode('utf-8'), result_type)



class Api(ApiBase):
    def __init__(self, token: str):
        super().__init__(token=token)

    def send_message(
            self,
            chat_id: Union[int, str],
            text: str,
            parse_mode: Optional[str] = None,
            disable_web_page_preview: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup,
                      ReplyKeyboardRemove, ForceReply]] = None) -> Message:
        return self._make_request()

    # def send_message(self,
    #                  chat_id: Union[int, str],
    #                  text: str,
    #                  parse_mode: Optional[str] = None,
    #                  disable_web_page_preview: Optional[bool] = None,
    #                  disable_notification: Optional[bool] = None,
    #                  reply_to_message_id: Optional[int] = None,
    #                  reply_markup: Optional[
    #                      Union[InlineKeyboardMarkup, ReplyKeyboardMarkup,
    #                            ReplyKeyboardRemove, ForceReply]] = None) -> Message:
    #     payload = json_payload(self._get_caller_func_args())
    #     url = self._get_tg_api_method_url(self._get_tg_api_method_name())
    #     r = requests.post(
    #         url, data=payload, headers={'Content-Type': 'application/json'})
    #     return handle_response(
    #         r.content.decode('utf-8'),
    #         AnnotationWrapper(
    #             str(
    #                 typing.get_type_hints(getattr(Api, self._get_caller_method_name()))['return'])).sanitized)


if __name__ == '__main__':
    bot_api = Api(token="432916128:AAG-rZvzYDzZCUr2psOlBrYeJa0_is7LR9o")
    btn1 = InlineKeyboardButton(text='add', url='http://lenta.ru')
    btn2 = InlineKeyboardButton(text='sub', url='http://topwar.ru')
    btn3 = InlineKeyboardButton(text='mul', url='http://waralbum.ru')
    btn4 = InlineKeyboardButton(text='div', url='http://antio.ru')
    inline_kb = InlineKeyboardMarkup([[btn1, btn2], [btn3, btn4]])
    res = bot_api.send_message(
        -1001373939377, "werfew", reply_markup=inline_kb)
    # print(res)
    # bot_api.send_message()
