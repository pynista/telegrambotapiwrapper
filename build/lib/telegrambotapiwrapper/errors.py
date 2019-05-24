# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

class Error(Exception):
    pass


class ResponseError(Error):
    pass


class RequestError(Error):
    pass


class SendingFileError(Error):
    pass


class RequestResultIsNotOk(ResponseError):
    pass


class KeyboardError(Error):
    pass


class InlineKeyboardMarkupError(KeyboardError):
    pass


class InlineKeyboardButtonError(InlineKeyboardMarkupError):
    pass


class NotExactlyOneOptionalFieldError(InlineKeyboardButtonError):
    pass
