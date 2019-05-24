import inspect
import re
import textwrap

import telegrambotapiwrapper.api.methods as methods_module
from telegrambotapiwrapper import AnnotationWrapper
from telegrambotapiwrapper.static import METHODS_RETURN_TYPES

CLASS_FROM_TYPES_REGEXP = re.compile(r"^<class '(.+)'>$")


def run():
    gen = generator_methods()
    result = ""
    for method in gen:
        result += get_method_code_text(method)
        result += "\n"
    return result


def generator_methods():
    res = []
    for name, obj in inspect.getmembers(methods_module):
        if inspect.isclass(obj):
            if ".methods." in str(obj):
                if 'methods.Base' not in str(obj):
                    mo = re.search(CLASS_FROM_TYPES_REGEXP, str(obj))
                    res.append(mo.group(1))
    res = sorted([tp.split('.')[-1] for tp in res])
    yield from (getattr(methods_module, item) for item in res)


def generate_docstring(docstring):
    wrapper_for_first_line = textwrap.TextWrapper(width=69)
    first_line = wrapper_for_first_line.wrap(docstring)[0]
    text_without_first_line = docstring.replace(
        first_line, ' ').strip()

    wrapper_for_other_lines = textwrap.TextWrapper(width=72)
    other_lines = wrapper_for_other_lines.wrap(
        text_without_first_line)
    text_result = "\n".join(other_lines)
    text_result = textwrap.indent(text_result, '           ')

    docstring_header = '''        """{}"""\n'''.format(
        first_line + '\n' + text_result)
    return docstring_header


def get_method_code_text(method_info):
    result = """{}""".format(gen_method_first_line(method_info))
    result += (" " * 12 + "self,\n")
    result += get_args_code_text(method_info)
    result += (" " * 4 + ") -> {}:\n".format(get_method_return_type(method_info)))
    # result += (" " * 8 + '"""{}\n"""'.format(method_info.__doc__))
    result += ('{}\n'.format(generate_docstring(method_info.__doc__)))
    result += (" " * 8 + "return self._make_request()\n")
    return result


def get_args_code_text(method_info):
    fields_names = method_info._fields_names()
    fields_annos = method_info._annotations()
    res = """"""
    for name in fields_names:
        if AnnotationWrapper(fields_annos[name]).is_optional:
            res += (" " * 12 + "{}: {}=None,\n".format(name, fields_annos[name].strip()))
        else:
            res += (" " * 12 + "{}: {},\n".format(name, fields_annos[name]))
    return res


def get_method_return_type(method_info) -> str:
    mt = method_info.__name__[0].lower() + method_info.__name__[1:]
    return METHODS_RETURN_TYPES[mt]


def gen_method_first_line(method_info):
    result = """\
    def {}(
""".format(py_api_method_name_from_method_info(method_info))
    return result


def py_api_method_name_from_method_info(method_info):
    mt = method_info.__name__
    upper_words = re.findall('[A-Z][^A-Z]*', mt)

    return "_".join([word.lower() for word in upper_words])


if __name__ == '__main__':
    # for m in generator_methods():
    #     print(m)
    print(run())
