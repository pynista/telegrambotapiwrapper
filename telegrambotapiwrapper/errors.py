class Error(Exception): pass


class ResponseError(Error): pass


class RequestResultIsNotOk(ResponseError): pass


class KeyboardError(Error): pass


class InlineKeyboardMarkup(KeyboardError): pass


class InlineKeyboardButtonError(InlineKeyboardMarkup): pass


class NotExactlyOneOptionalFieldError(InlineKeyboardButtonError): pass
