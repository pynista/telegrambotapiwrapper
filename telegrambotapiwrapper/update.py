from telegrambotapiwrapper.typelib import Update
from telegrambotapiwrapper.utils import get_file, is_bytes_img
from telegrambotapiwrapper.wrapper import Api


class UpdateWrapper:
    """Обертка вокруг типа Update API телеграмма."""

    def __init__(self, update: Update):
        self._update = update

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


    def is_image(self, token) -> bool:
        """Проверить, является ли обновление изображением, переданным как
        document или photo."""
        if self.has_msg_photo_field:
            return True
        elif self.is_file:
            bot = Api(token=token)
            file_obj = bot.get_file(self._update.message.document.file_id)

            file_path = file_obj.file_path
            f_bytes = get_file(token, file_path)
            if is_bytes_img(f_bytes):
                return True
            else:
                return False
        else:
            return False

    @property
    def chat_id(self) -> int:
        return self._update.message.chat.id

    @property
    def poll_id(self) -> str:
        return self._update.message.poll.id





