"""Implements various helpers."""

import pprint

from telegrambotapiwrapper import Update


class UpdateWrapper:
    """Обертка вокруг типа Update API телеграмма."""

    def __init__(self, update: Update):
        self._update = update

    def __str__(self):
        return pprint.pformat(self._update)

    def __getattr__(self, name):
        return getattr(self._update, name)

    @property
    def is_start_command(self) -> bool:
        return self._update.message.text == '/start'

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
    def document_id(self) -> str:
        return self._update.message.document.file_id
