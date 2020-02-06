# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License
"""The module contains various utilities."""
import pprint

import filetype
import requests

from telegrambotapiwrapper.typelib import Update


def replace_from__word(d: dict):
    """Replace recursive keys in the object from_ to from."""
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


def replace_from_word(d: dict) -> dict:
    """Replace recursive keys in the object from to from_."""
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
    """Is value str, int, float, bool."""
    return isinstance(value, (int, str, float))


def is_ends_with_underscore(value: str):
    """Does value end with underscore."""
    if value == "":
        return False
    else:
        return value[-1] == '_'


def file_path(bot, file_id: str):
    file_obj = bot.get_file(file_id)
    return file_obj.file_path


def is_bytes_img(obj: bytes):
    """Check whether bytes define an image."""
    try:
        return 'image/' in filetype.guess(obj).MIME
    except AttributeError:
        return False


def download_file(bot, file_path) -> bytes:
    """Get file."""
    url = "https://api.telegram.org/file/bot{}/{}".format(
        bot.token,
        file_path
    )
    u = requests.get(url)
    return u.content


class UpdateWrapper:
    """Обертка вокруг типа Update API телеграмма."""
    def __init__(self, update: Update):
        self._update = update

    def __str__(self):
        return pprint.pformat(self._update)

    def __getattr__(self, name):
        return getattr(self._update, name)

    def is_start_command(self):
        return self._update.message.text == '/start'

    @property
    def has_msg_photo_field(self) -> bool:
        """Check whether the update has a Photo field."""
        return self._update.message.photo is not None

    @property
    def has_msg_document_field(self) -> bool:
        return self._update.message.document is not None

    @property
    def is_file(self) -> bool:
        """Проверить, представляет ли собой обновловление document.

        Notes:
            document может быть и изображением
        """
        return self._update.message.document is not None

    def is_img(self, bot) -> bool:
        """Проверить, является ли обновление изображениям, переданным как
        document или photo."""
        if self.has_msg_photo_field:
            return True
        elif self.is_file:
            fp = file_path(bot, self.document_id)
            f_bytes = download_file(bot, fp)
            return is_bytes_img(f_bytes)
        else:
            return False

    @property
    def chat_id(self) -> int:
        return self._update.message.chat.id

    @property
    def poll_id(self) -> str:
        return self._update.message.poll.id

    @property
    def msg_text(self) -> str:
        return self._update.message.text

    @property
    def is_text(self) -> bool:

        """Представляет ли собой update текст."""
        return self._update.message.text is not None \
               and not self.has_msg_document_field \
               and not self.has_msg_photo_field

    def is_number(self) -> bool:
        """Представляет ли собой update текст, являющимся числом """
        if self.is_text:
            txt = self.msg_text.replace('.', '', 1)
            txt = txt.replace(',', '', 1)
            return txt.isdigit()
        else:
            return False

    def number(self) -> float:
        if self.is_number:
            return float(self.msg_text)
        else:
            raise TypeError(
                "update не представляет собой текст являющимся числом")

    @property
    def document_id(self) -> str:
        return self._update.message.document.file_id

    @property
    def img_id(self) -> str:
        return self._update.message.photo[0].file_id

    def download_img(self, bot) -> bytes:
        fp = file_path(bot, self.img_id)
        return download_file(bot, fp)

def is_right_type_message_entity(message_entity_type: str):
    """Проверить, правильный ли тип message entity

    Notes:
        https://core.telegram.org/bots/api#messageentity
    """
    right_types = (
        'mention',
        'hashtag',
        'cashtag',
        'bot_command',
        'url',
        'email',
        'phone_number',
        'bold',
        'italic',
        'underline',
        'strikethrough',
        'code',
        'pre',
        'text_link',
        'text_mention',
    )

    return message_entity_type in right_types