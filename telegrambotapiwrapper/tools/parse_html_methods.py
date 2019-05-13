# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

"""Парсер для методов из API телеграмма.

Парсер работает с файлом html, содержащим данные о методах в следующем формате:

<h4><a class="anchor" name="getme" href="#getme"><i class="anchor-icon"></i></a>getMe</h4>
<p>A simple method for testing your bot&#39;s auth token. Requires no parameters. Returns basic information about the bot in form of a <a href="#user">User</a> object.</p>
<table class="table">
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>werf</td>
<td>wer</td>
<td>wer</td>
<td>wef</td>
</tr>
</tbody>
</table>
...
<h4>...</h4>
<p>...</p>
<table>...</table>
...
"""
import os
import textwrap
from dataclasses import dataclass
from operator import attrgetter
from typing import List, Optional
import subprocess

from bs4 import BeautifulSoup

HTML_FILE = "/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/avaliable/methods.html"

ALL_METHODS_FILES = (
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/avaliable/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/games/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/getting_updates/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/inline_mode/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/passport/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/payments/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/stickers/methods.html',
    '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/updating_messages/methods.html'
)

RETURNED_VALUES = {
    ' Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future':
    'Optional[Message]',
    ' Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future':
    'Optional[Message]',
    ' Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future':
    'Optional[Message]',
    ' Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future':
    'Optional[Message]',
    ' Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future':
    'Optional[Message]',
    ' If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned':
    'Optional[List[ChatMember]]',
    ' On success, True is returned':
    'Optional[bool]',
    ' On success, an array of the sent Messages is returned':
    'Optional[List[Message]]',
    ' On success, if the edited message was sent by the bot, the edited Message is returned, otherwise True is returned':
    'Optional[Union[Message, bool]]',
    ' On success, if the message was sent by the bot, the sent Message is returned, otherwise True is returned':
    'Optional[Union[Message, bool]]',
    ' On success, the sent Message is returned':
    'Optional[Message]',
    ' Returns Int on success':
    'Optional[int]',
    ' Returns True on success':
    'Optional[bool]',
    ' Returns a Chat object on success':
    'Optional[Chat]',
    ' Returns a ChatMember object on success':
    'Optional[ChatMember]',
    ' Returns a UserProfilePhotos object':
    'UserProfilePhotos',
    ' Returns basic information about the bot in form of a User object':
    'User',
    ' Returns the new invite link as String on success':
    'Optional[str]',
    ' When the link expires, a new one can be requested by calling getFile again':
    'Optional[File]',
    ' An Array of Update objects is returned':
    'List[Update]',
    'Array of String':
    'List[str]',
}

import os

ESPECIAL_ANNOTATIONS = {
    'Array of Array of InlineKeyboardButton':
    'List[List[InlineKeyboardButton]]',
    'Array of Array of KeyboardButton':
    'List[List[KeyboardButton]]',
    'Array of Array of PhotoSize':
    'List[List[PhotoSize]]',
    'Array of MessageEntity':
    'List[MessageEntity]',
    'Array of PhotoSize':
    'List[PhotoSize]',
    'Array of User':
    'List[User]',
    'Array of String':
    'List[str]',
    'Boolean':
    'bool',
    'InputFile or String':
    'Union[InputFile, str]',
    'Integer':
    'int',
    'String':
    'str',
    'Array of InlineQueryResult':
    'List[InlineQueryResult]',
    'Array of PassportElementError':
    'List[PassportElementError]',
    'Array of LabeledPrice':
    'List[LabeledPrice]',
    'Array of ShippingOption':
    'List[LabeledPrice]',
    'InputFile':
    'InputFile',
    'MaskPosition':
    'MaskPosition',
    'Float':
    'float',
    'Array of InputMediaPhoto and InputMediaVideo':
    'List[Union[InputMediaPhoto, InputMediaVideo]]',
    'Array of InputMediaPhoto and InputMediaVideo\n':
    'List[Union[InputMediaPhoto, InputMediaVideo]]',
    'Float number':
    'float',
    'InlineKeyboardMarkup':
    'InlineKeyboardMarkup',
    'InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply':
    'Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]',
    'InlineKeyboardMarkup or ReplyKeyboardMarkup\n            or ReplyKeyboardRemove or ForceReply':
    'Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]',
    'ForceReply':
    'ForceReply',
    'Integer or String':
    'Union[int, str]',
    'InputMedia':
    'InputMedia',
    'PassportElementError':
    "PassportElementError",
    'InlineQueryResult':
    'InlineQueryResult',
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def importanize_in_dir_rec():
    lib_dir = os.path.join(BASE_DIR, 'api')
    for dirpath, _, filenames in list(os.walk(lib_dir))[1:]:
        if 'methods.py' in filenames:
            methods_file_path = os.path.join(dirpath, 'methods.py')
            print(methods_file_path)
            subprocess.run(["importanize", "{}".format(methods_file_path)])
        if 'types.py' in filenames:
            methods_file_path = os.path.join(dirpath, 'types.py')
            print(methods_file_path)
            subprocess.run(["importanize", "{}".format(methods_file_path)])


@dataclass
class MethodParameter:
    name: str
    type: str
    required: str
    description: str

    @property
    def is_required(self):
        if self.required.strip() == 'Yes':
            return True
        elif self.required.strip() == 'Optional':
            return False
        else:
            raise NotImplementedError


@dataclass
class Method:
    name: str
    description: str
    parameters: Optional[List[MethodParameter]]

    @property
    def returns(self):
        return RETURNED_VALUES[self.description.split('.')[-2]]


def parse_available_methods(html_file: str):
    res = []
    with open(html_file) as file:
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')
        if not is_html_file_correct(html_file):
            raise Exception("File Not Correct")

        available_methods = soup.find_all("h4")
        for available_method in available_methods:
            method_name = available_method.contents[1].strip()
            method_descr = available_method.next_sibling.next_sibling.get_text(
            )

            table = available_method.next_sibling.next_sibling.next_sibling.next_sibling
            table_rows = table.find_all('tr')

            method_parameters = []
            for tr in table_rows:
                tds_in_tr = tr.find_all("td")
                if tds_in_tr:
                    name, type, required, description = [
                        td.text for td in tds_in_tr
                    ]
                    new_par = MethodParameter(
                        name=name,
                        type=type,
                        required=required,
                        description=description)
                    if name:
                        method_parameters.append(new_par)
                    else:
                        pass
            new_method = Method(
                method_name, method_descr, parameters=method_parameters)
            res.append(new_method)

    return res


def generate_file_text(methods: List[Method], add_base_class=True) -> str:
    """Сгенерировать py файл."""
    imports = \
"""\n"""
    res = ''
    res += imports

    # if add_base_class:
    #     res += """class Base: pass\n\n"""

    def method_class_py_code(method: Method):
        def get_class_header():
            if add_base_class:
                header = """@dataclass\nclass {}(Base):""".format(
                    method.name[0].capitalize() + method.name[1:])
            else:
                header = """@dataclass\nclass {}:""".format(
                    method.name[0].capitalize() + method.name[1:])
            return header

        def generate_docstring():
            def generate_class_description():
                wrapper_for_first_line = textwrap.TextWrapper(width=69)
                first_line = wrapper_for_first_line.wrap(method.description)[0]
                text_without_first_line = method.description.replace(
                    first_line, ' ').strip()

                wrapper_for_other_lines = textwrap.TextWrapper(width=72)
                other_lines = wrapper_for_other_lines.wrap(
                    text_without_first_line)
                text_result = "\n".join(other_lines)
                text_result = textwrap.indent(text_result, '       ')

                docstring_header = '''    """{}"""\n'''.format(
                    first_line + '\n' + text_result)
                return docstring_header

            return generate_class_description()

        def generate_body_dataclass():
            res = ''
            for par in sorted(
                    method.parameters, key=attrgetter('is_required'),
                    reverse=True):
                if par.required == 'Yes':
                    res += """    {field_name}: {field_type}\n""".format(
                        field_name=par.name,
                        field_type=ESPECIAL_ANNOTATIONS[par.type],
                    )
                elif par.required == 'Optional':
                    field_type = 'Optional[{}]'.format(
                        ESPECIAL_ANNOTATIONS[par.type])
                    res += """    {field_name}: {field_type} = {default_value}\n""".format(
                        field_name=par.name,
                        field_type=field_type,
                        default_value=None,
                    )
                else:
                    res += "ERROR1"
            # res += '    returns: {}\n'.format(method.returns)
            return res

        return get_class_header() + '\n' + generate_docstring(
        ) + '\n' + generate_body_dataclass()

    for method in methods:
        res += method_class_py_code(method)
        res += '\n\n'

    return res


def is_html_file_correct(html_file: str) -> bool:
    """Проверить вляется ли html- файл корректным."""
    errors = False
    with open(html_file) as file:
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("h4")
        for item in items:
            if item.next_sibling.next_sibling.name != 'p':
                print(
                    'Файл {}\nСлед тэг после <h4> не <p>, а <{}>. ({})\n***************'
                    .format(
                        html_file,
                        item.next_sibling.next_sibling.next_sibling.
                        next_sibling.name,
                        item.next_sibling.next_sibling.next_sibling.
                        next_sibling,
                    ))
                errors = True
            if item.next_sibling.next_sibling.next_sibling.next_sibling.name != 'table':
                print(
                    'Файл {}\nСлед тэг после <p> не <table>, а <{}>. ({})\n***************'
                    .format(
                        html_file,
                        item.next_sibling.next_sibling.next_sibling.
                        next_sibling.name,
                        item.next_sibling.next_sibling.next_sibling.
                        next_sibling,
                    ))
                errors = True
    if not errors:
        print('OK: {}'.format(html_file))
        return True
    else:
        return False


def run():

    dest_file = os.path.join(BASE_DIR, 'api', 'methods.py')
    os.remove(dest_file)

    methods_html_files =  (
        os.path.join(BASE_DIR, 'tools', 'htmls', 'available', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'games', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'getting_updates', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'inline_mode', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'passport', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'payments', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'stickers', 'methods.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'updating_messages', 'methods.html'),
    )

    file_header = """from __future__ import annotations

from dataclasses import dataclass
from typing import Union, Optional, List

from telegrambotapiwrapper.api.base import Base
from telegrambotapiwrapper.api.types import (PassportElementErrorDataField,
                                          PassportElementErrorFrontSide,
                                          PassportElementErrorReverseSide,
                                          PassportElementErrorSelfie,
                                          PassportElementErrorFile,
                                          PassportElementErrorFiles,
                                          PassportElementErrorTranslationFile,
                                          PassportElementErrorUnspecified,
                                          PassportElementErrorTranslationFiles,
                                          InputMediaAnimation,
                                          InputMediaDocument,
                                          InputMediaAudio,
                                          InputMediaPhoto,
                                          InputMediaVideo,
                                          InlineQueryResultCachedAudio,
                                          InlineQueryResultCachedDocument,
                                          InlineQueryResultCachedGif,
                                          InlineQueryResultCachedMpeg4Gif,
                                          InlineQueryResultCachedPhoto,
                                          InlineQueryResultCachedSticker,
                                          InlineQueryResultCachedVideo,
                                          InlineQueryResultCachedVoice,
                                          InlineQueryResultArticle,
                                          InlineQueryResultAudio,
                                          InlineQueryResultContact,
                                          InlineQueryResultGame,
                                          InlineQueryResultDocument,
                                          InlineQueryResultGif,
                                          InlineQueryResultMpeg4Gif,
                                          InlineQueryResultPhoto,
                                          InlineQueryResultVenue,
                                          InlineQueryResultVideo,
                                          InlineQueryResultVoice,
                                          InlineKeyboardMarkup,
                                          ReplyKeyboardMarkup,
                                          ReplyKeyboardRemove,
                                          ForceReply,
                                          InlineQueryResultLocation,
                                          InputFile,
                                          MaskPosition,
                                          LabeledPrice)

PassportElementError = Union[
    PassportElementErrorDataField,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified
]

InputMedia = Union[
    InputMediaAnimation,
    InputMediaDocument,
    InputMediaAudio,
    InputMediaPhoto,
    InputMediaVideo
]

InlineQueryResult = Union[
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultGame,
    InlineQueryResultDocument,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
]"""
    with open(dest_file, 'a+') as f:
        f.write(file_header)

    for html_file_path in methods_html_files:
        file_text = generate_file_text(parse_available_methods(html_file_path))
        with open(dest_file, 'a+') as f:
            f.write(file_text)
    importanize_in_dir_rec()


if __name__ == '__main__':
    run()
