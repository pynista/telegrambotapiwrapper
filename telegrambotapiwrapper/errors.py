# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

class Error(Exception): pass


class ResponseError(Error): pass


class RequestResultIsNotOk(ResponseError): pass


class KeyboardError(Error): pass


class InlineKeyboardMarkup(KeyboardError): pass


class InlineKeyboardButtonError(InlineKeyboardMarkup): pass


class NotExactlyOneOptionalFieldError(InlineKeyboardButtonError): pass
