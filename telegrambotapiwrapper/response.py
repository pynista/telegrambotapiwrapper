# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

import jsonpickle
from telegrambotapiwrapper.request import json_payload

from telegrambotapiwrapper.errors import RequestResultIsNotOk
from telegrambotapiwrapper.annotation import AnnotationWrapper
from telegrambotapiwrapper.api.types import *
from telegrambotapiwrapper.utils import is_str_int_float_bool


def dataclass_fields_to_jdict(fields: dict) -> dict:
    """Получить из полей dataclass, определяющего тип объекта, json-подобный словарь."""
    jstr = json_payload(fields)
    res = jsonpickle.decode(jstr)
    return res



def to_api_type(obj, tp: AnnotationWrapper):
    """Преобразовать результат запроса к Telegram Bot API в соответствующий тип.

    Notes:
        1)
            В текущей версий Telegram Bot Api (4.2) могут возвращаться следующие значения:
                'Chat',
                'ChatMember',
                'File',
                'List[ChatMember]',
                'List[GameHighScore]',
                'List[Update]',
                'Message',
                'Pool',
                'StickerSet',
                'Union[Message, bool]',
                'User',
                'UserProfilePhotos',
                'WebhookInfo',
                'bool',
                'int',
                'str'
            Для текущей версии Telegram Bot Api (4.2) для создания типов используются следующие `union`- аннотации:
                'Optional[Union[InputFile, str]]'
            Для текущей версии Telegram Bot Api (4.2) для создания типов используются следующие `List`- аннотации:
                    'List[EncryptedPassportElement]',
                    'List[LabeledPrice]',
                    'List[PhotoSize]',
                    'List[PollOption]',
                    'List[Sticker]',
                    'List[str]',
            Для текущей версии Telegram Bot Api (4.2) для создания типов используются следующие `List[List[`- аннотации:
                    'List[List[InlineKeyboardButton]]',
                    'List[List[KeyboardButton]]',
                    'List[List[PhotoSize]]',
            Для текущей версии Telegram Bot Api (4.2) у возвращаемых значений могут быть следующие `union`- аннотации:
                'Union[Message, bool]'
        2)
    """

    def list_to_api_type(obj: list, tp: AnnotationWrapper) -> list:
        inner_part = tp.inner_part_of_list
        api_type = globals()[inner_part]

        res = []
        for item in obj:
            to_type = {}
            for field_name, field_type in api_type._annotations().items():
                try:
                    to_type[field_name] = to_api_type(item[field_name], AnnotationWrapper(field_type))
                except KeyError:
                    continue
            res.append(api_type(**to_type))
        return res

    def list_of_list_to_api_type(obj: list, tp: AnnotationWrapper):
        res = []
        for lst in obj:
            res.append(list_to_api_type(lst, tp.inner_part_of_list))
        return res

    def union_to_api_type(obj, tp: AnnotationWrapper):
        if tp == 'Union[Message, bool]':
            return to_api_type(obj, AnnotationWrapper('Message'))
        elif tp == 'Union[InputFile, str]]':
            return to_api_type(obj, AnnotationWrapper('InputFile'))


    if is_str_int_float_bool(obj):
        return obj

    if tp.is_optional:
        tp = tp.inner_part_of_optional

    if tp.is_list:
        return list_to_api_type(obj, tp)
    elif tp.is_list_of_list:
        return list_of_list_to_api_type(obj, tp)
    elif tp.is_union:
        return union_to_api_type(obj, tp)

    if isinstance(obj, dict):
        to_type = {}
        api_type = globals()[tp]

        for field_name, field_type in api_type._annotations().items():
            try:
                to_type[field_name] = to_api_type(obj[field_name], AnnotationWrapper(field_type))
            except KeyError:
                continue
        return api_type(**to_type)


def get_result(raw_response: str):
    """Извлечь результат из сырого ответа от Bot API телеграмма.

    Args:
        raw_response (str): `сырой` ответ от Bot API телеграмма

    Raises:
        RequestResultIsNotOk: если ответ не содержит результата

    Note:
        если raw_response не содержит поля `ok`, то считаем что это уже извлеченный результат, например
        для целей тестирования
    """
    response = jsonpickle.loads(raw_response)
    try:
        is_ok = response["ok"]
    except KeyError:
        return response
    if is_ok:
        return response['result']

    else:
        raise RequestResultIsNotOk("error_code: {}, description: {}".format(response['error_code'],
                                                                            response['description']))


def handle_response(raw_response: str, method_response_type: AnnotationWrapper):
    """Распарсить строку, являющуюся ответом от Bot API телеграмма.

    Args:
        raw_response (str): ответ от Bot API телеграмма
        method_response_type (AnnotationWrapper): аннотация ожидаемого ответа

    Raises:
        RequestResultIsNotOk: если ответ не содержит результата
    """
    return to_api_type(get_result(raw_response), method_response_type)




if __name__ == '__main__':
    user = User(12243, False, "djshfjksdhfjkhskjd")
    a = InlineQuery(2345345, from_=user, query="asdasdsad", offset="123213213")
    print(dir(a))
    # chat_photo = ChatPhoto(small_file_id='1fdf235643', big_file_id='3454sdfds56546')
    # chat1_with_chat_photo = Chat(
    #     id=123,
    #     type='group',
    #     title='dsdvfvdvxfve',
    #     all_members_are_administrators=True,
    #     photo=chat_photo
    # )
    # to_convert = chat1_with_chat_photo._fields_items
    # to_type = dataclass_fields_to_jdict(to_convert)
    # print(to_type)
    #
    # a = to_api_type(to_type, tp=AnnotationWrapper('Chat'))
    # b = chat1_with_chat_photo
    # print(a)


