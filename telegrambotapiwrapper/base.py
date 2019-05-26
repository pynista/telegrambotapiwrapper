# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

import dataclasses
from typing import List

from telegrambotapiwrapper.annotation import AnnotationWrapper


class Base:
    @classmethod
    def _get_classname(cls):
        return cls.__name__

    @classmethod
    def _get_simple_fields(cls) -> dict:
        return {
            name: tp
            for name, tp in cls._annotations().items()
            if AnnotationWrapper(tp).is_simple_in_opt_and_not_opt
        }

    @classmethod
    def _get_not_simple_fields(cls):
        return {
            name: tp
            for name, tp in cls._annotations().items()
            if not AnnotationWrapper(tp).is_simple_in_opt_and_not_opt
        }

    @classmethod
    def _is_simple_type(cls):
        return all([
            AnnotationWrapper(anno).is_simple_in_opt_and_not_opt
            for anno in cls._used_annotations()
        ])

    @classmethod
    def _fields_names(cls) -> List:
        """Get a list of dataclass fields names."""
        return list(field.name for field in dataclasses.fields(cls))

    @classmethod
    def _annotations(cls) -> dict:
        return {field.name: field.type for field in dataclasses.fields(cls)}

    @classmethod
    def _used_annotations(cls) -> set:
        """Возвращает

        {'int', 'str', 'bool', 'Optional[str]'}
        """
        return set(field.type for field in dataclasses.fields(cls))

    @classmethod
    def _field_type(cls, field_name) -> str:
        for field in dataclasses.fields(cls):
            if field.name == field_name:
                return field.type

    @property
    def _fields_items(self) -> dict:
        """Get a dict of dataclass fields, as name: value pairs.

        Notes:
            Use only for instances.
        """
        return dataclasses.asdict(self)

#     @staticmethod
#     def _serialize(self):
#         return json.dumps(self._fields_items, cls=EnhancedJSONEncoder)
#
#
# class ApiJSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         res = {}
#         for field_name, field_value in o._fields_items():
#             if isinstance(field_value, (int, float, bool, str)):
#                 res[field_name] = field_value
#             else:
#                 res[field_name] = json.dumps(field_value, cls=ApiJSONEncoder)
#         return res
#
#
# class EnhancedJSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if dataclasses.is_dataclass(o):
#             return dataclasses.asdict(o)
#         return super().default(o)
