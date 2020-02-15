import filetype
import requests


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


def file_path(bot, file_id: str):
    file_obj = bot.get_file(file_id)
    return file_obj.file_path
