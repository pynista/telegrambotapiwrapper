import inspect


def outer_args(skip_self=True) -> dict:
    """Получить аргументы функции, внутри которой вызвана данная функция."""
    currframe = inspect.currentframe()
    outerframe = inspect.getouterframes(currframe, 2)
    args, _, _, values = inspect.getargvalues(outerframe[1][0])
    if skip_self:
        return {
            key: value
            for key, value in values.items()
            if (key in args) and (key != 'self')
        }
    else:
        return {key: value for key, value in values.items() if key in args}


def outer2_args(skip_self=True):
    """Получить аргументы функции, которая есть внешняя функцией для функции внутри которой вызвана данная функция ."""
    currframe = inspect.currentframe()
    outerouterframe = inspect.getouterframes(currframe, 1)
    args, _, _, values = inspect.getargvalues(outerouterframe[2][0])

    if skip_self:
        return {
            key: value
            for key, value in values.items()
            if (key in args) and (key != 'self')
        }
    else:
        return {key: value for key, value in values.items() if key in args}


def outer3_args(skip_self=True):
    currframe = inspect.currentframe()
    outer3frame = inspect.getouterframes(currframe)[3].frame
    args, _, _, values = inspect.getargvalues(outer3frame)

    if skip_self:
        return {
            key: value
            for key, value in values.items()
            if (key in args) and (key != 'self')
        }
    else:
        return {key: value for key, value in values.items() if key in args}


def outer_return_type() -> str:
    return inspect.stack()[0]


def outer2_return_type():
    pass


def outer3_return_type():
    pass


def outer_name():
    outer_name = inspect.stack()[1][3]
    return outer_name


def outer2_name():
    return inspect.stack()[2][3]


def outer3_name():
    return inspect.stack()[3][3]
