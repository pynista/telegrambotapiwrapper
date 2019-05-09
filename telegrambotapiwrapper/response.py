import jsonpickle
from telegrambotapiwrapper.request import json_payload

from telegrambotapiwrapper.errors import RequestResultIsNotOk
from telegrambotapiwrapper.annotation import AnnotationWrapper
from telegrambotapiwrapper.api.types import *


def dataclass_fields_to_d(fields: dict):
    jstr =  json_payload(fields)
    res =  jsonpickle.decode(jstr)
    return res

def to_api_type(obj, tp: Union[AnnotationWrapper, str]):
    """Преобразовать объект, полученный от Bot Api в воответствующий тип.

    Args:
        obj: объект, который требуется преобразовать. Этим объектом является объект извлеченный по ключу 'result'
            из ответа телеграмма
        tp: аннотация получаемого типа
    """

    if isinstance(tp, str):
        tp = AnnotationWrapper(tp)

    if isinstance(obj, (int, float, str, bool)):  # переделать на более красивое
        return obj

    if tp.is_union:
        if tp == 'Union[Message, bool]':
            if isinstance(obj, bool):
                return obj
            else:
                return to_api_type(obj, AnnotationWrapper("Message"))

        else:
            raise NotImplementedError("Bot API 4.2 uses only `Union[Message, bool]`- union")

    if tp.is_list:
        raise Exception

    if tp.is_list_of_list:
        raise Exception

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
    chat_photo = ChatPhoto(small_file_id='1fdf235643', big_file_id='3454sdfds56546')
    chat1_with_chat_photo = Chat(
        id=123,
        type='group',
        title='dsdvfvdvxfve',
        all_members_are_administrators=True,
        photo=chat_photo
    )

    a = dataclass_fields_to_d(chat1_with_chat_photo._fields_items)
    print(a)
    print(to_api_type(a, 'Chat'))

