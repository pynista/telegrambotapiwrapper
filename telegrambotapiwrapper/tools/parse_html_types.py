# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

"""Модуль для парсинга Telegram Bot Api с сайта."""
from __future__ import annotations

import keyword
import os
import textwrap
from dataclasses import dataclass
from operator import attrgetter
from typing import List, Optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from bs4 import BeautifulSoup

# ALL_TYPES_FILES = (
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/avaliable/types.html',
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/games/types.html',
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/getting_updates/types.html',
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/inline_mode/types.html',
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/passport/types.html',
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/payments/types.html',
#     '/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/stickers/types.html',
# )
#
# HTML_FILE = "/home/dzmitry/PycharmProjects/bots/tgbotapi/for_parser/avaliable/types.html"


@dataclass
class ApiType:
    name: str
    description: str
    fields: List[TypeField]


@dataclass
class TypeField:
    ESPECIAL_ANNOTATIONS = {
        'Array of Array of InlineKeyboardButton': 'List[List[InlineKeyboardButton]]',
        'Array of Array of KeyboardButton': 'List[List[KeyboardButton]]',
        'Array of Array of PhotoSize': 'List[List[PhotoSize]]',
        'Array of MessageEntity': 'List[MessageEntity]',
        'Array of PhotoSize': 'List[PhotoSize]',
        'Array of User': 'List[User]',
        'Boolean': 'bool',
        'InputFile or String': 'Union[InputFile, str]',
        'Integer': 'int',
        'String': 'str',
        'Float': 'float',
        'Float number': 'float',
        'Array of PassportFile': 'List[PassportFile]',
        'True': 'bool_True',
        'Array of String': 'List[str]',
        'Array of Sticker': 'List[Sticker]',
        'Array of EncryptedPassportElement': 'List[EncryptedPassportElement]',
        'Array of LabeledPrice': 'List[LabeledPrice]',
        'Array of PollOption': 'List[PollOption]'

    }

    name: str
    type: str
    description: str
    parent_api_type: Optional[ApiType] = None

    @property
    def is_optional(self):
        if self.description.split()[0] == 'Optional.':
            return True
        else:
            return False

    @property
    def field_type_rec(self):

        if self.type == 'True':
            return """    {field_name}: {field_type} = {default_value}\n""".format(
                field_name=self.name,
                field_type=self.type_annotation,
                default_value=self.default_value,
            )

        if self.is_optional:
            return """    {field_name}: {field_type} = {default_value}\n""".format(
                field_name=self.name,
                field_type=self.type_annotation,
                default_value=self.default_value,
            )
        else:
            return """    {field_name}: {field_type}\n""".format(
                field_name=self.name,
                field_type=self.type_annotation,
            )

    @property
    def type_annotation(self):

        if self.type in TypeField.ESPECIAL_ANNOTATIONS:
            py_type = TypeField.ESPECIAL_ANNOTATIONS[self.type]
        elif self.type == "True":
            py_type = "bool"
        else:
            py_type = self.type

        if self.type == 'True':
            if self.parent_api_type.name == 'Message':
                return "Optional[bool]"
            else:
                return "bool"
        elif self.is_optional:
            return "Optional[{}]".format(py_type)
        else:
            return py_type

    @property
    def default_value(self) -> Optional[bool]:
        if self.parent_api_type.name in ('ReplyKeyboardRemove', 'ForceReply'):
            if self.type == "True":
                return True
            else:
                return None
        else:
            return None


def parse_available_types(html_file):
    res = []
    with open(html_file) as file:
        html = file.read()
        if not is_html_file_corrrect(html_file):
            raise Exception("File Not Correct")
        soup = BeautifulSoup(html, 'html.parser')
        available_types = soup.find_all("h4")
        for available_type in available_types:
            type_name = available_type.contents[1].strip()
            type_descr = available_type.next_sibling.next_sibling.get_text()

            table = available_type.next_sibling.next_sibling.next_sibling.next_sibling
            table_rows = table.find_all('tr')
            type_fields = []
            for tr in table_rows:
                tds_in_tr = tr.find_all("td")
                if tds_in_tr:
                    try:
                        field_name, field_type, description = [
                            td.text for td in tds_in_tr
                        ]
                    except ValueError as e:
                        print(table)
                        raise
                    if keyword.iskeyword(field_name):
                        field_name += '_'
                    if field_name:
                        field = TypeField(name=field_name,
                                          type=field_type,
                                          description=description
                                          )
                        type_fields.append(field)
            new_api_type = ApiType(type_name,
                                   type_descr,
                                   type_fields)
            res.append(new_api_type)

    return res



def generate_file_text(types: List[ApiType], add_base_class=True):
    """Сгенерировать py файл."""
    imports = \
"""\n
"""
    res = ''
    res += imports
    # if add_base_class:
    #     res += """class Base: pass\n\n"""

    def type_class_py_code(type: ApiType):

        def get_class_header():
            if add_base_class:
                header = """@dataclass\nclass {}(Base):""".format(type.name[0].capitalize() + type.name[1:])
            else:
                header = """@dataclass\nclass {}:""".format(type.name[0].capitalize() + type.name[1:])
            return header

        def generate_docstring():
            def generate_class_description():
                wrapper_for_first_line = textwrap.TextWrapper(width=69)
                first_line = wrapper_for_first_line.wrap(type.description)[0]
                text_without_first_line = type.description.replace(first_line, ' ').strip()

                wrapper_for_other_lines = textwrap.TextWrapper(width=72)
                other_lines = wrapper_for_other_lines.wrap(text_without_first_line)
                text_result = "\n".join(other_lines)
                text_result = textwrap.indent(text_result, '       ')
                if text_result:
                    docstring_header = '''    """{}"""\n'''.format(first_line + '\n' + text_result)
                else:
                    docstring_header = '''    """{}"""\n'''.format(first_line)
                return docstring_header

            return generate_class_description()

        def generate_body_dataclass():
            res = ''
            for par in sorted(type.fields, key=attrgetter('is_optional')):
                par.parent_api_type = type
                res += par.field_type_rec
            return res

        return get_class_header() + '\n' + generate_docstring() + '\n' + generate_body_dataclass()

    for type in types:
        res += type_class_py_code(type)
        res += '\n\n'

    return res


def is_html_file_corrrect(html_file: str) -> bool:
    """Проверить вляется ли html- файл корректным."""
    errors = False
    with open(html_file) as file:
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("h4")
        for item in items:
            if item.next_sibling.next_sibling.name != 'p':
                print('Файл {}\nСлед тэг после <h4> не <p>, а <{}>. ({})\n***************'.format(
                    html_file,
                    item.next_sibling.next_sibling.next_sibling.next_sibling.name,
                    item.next_sibling.next_sibling.next_sibling.next_sibling,
                ))
                errors = True
            if item.next_sibling.next_sibling.next_sibling.next_sibling.name != 'table':
                print('Файл {}\nСлед тэг после <p> не <table>, а <{}>. ({})\n***************'.format(
                    html_file,
                    item.next_sibling.next_sibling.next_sibling.next_sibling.name,
                    item.next_sibling.next_sibling.next_sibling.next_sibling,
                ))
                errors = True
    if not errors:
        print('OK: {}'.format(html_file))
        return True
    else:
        return False


def run():

    dest_file = os.path.join(BASE_DIR, 'api', 'types.py')
    os.remove(dest_file)

    types_html_files = (
        os.path.join(BASE_DIR, 'tools', 'htmls', 'available', 'types.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'games', 'types.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'getting_updates', 'types.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'inline_mode', 'types.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'passport', 'types.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'payments', 'types.html'),
        os.path.join(BASE_DIR, 'tools', 'htmls', 'stickers', 'types.html'),
    )

    file_header = """from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, Union

from telegrambotapiwrapper.api.base import Base
"""
    with open(dest_file, 'a+') as f:
        f.write(file_header)

    for html_file_path in types_html_files:
        file_text = generate_file_text(parse_available_types(html_file_path))
        with open(dest_file, 'a+') as f:
            f.write(file_text)


if __name__ == '__main__':
    run()
