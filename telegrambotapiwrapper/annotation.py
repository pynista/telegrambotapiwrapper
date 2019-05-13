# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dzmitry Maliuzhenets; MIT License

from __future__ import annotations
from collections import UserString
import re
from typing import List

# def is_anno_of_simple_type()

class AnnotationWrapper(UserString):
    """Обертка вокруг аннотаций типов."""

    opt_field_re = re.compile(r'^Optional\[')
    list_field_re = re.compile(r'^List\[')
    list_of_list_re = re.compile(r'^List\[List\[')
    union_field_re = re.compile(r'^Union\[')
    inner_part_of_list_of_list_re = re.compile(r'^List\[List\[(.+)\]\]$')
    inner_part_of_opt_re = re.compile(r'^Optional\[(.+)\]$')
    inner_part_of_union_re = re.compile(r'^Union\[(.+)\]$')
    inner_part_of_list_re = re.compile(r'^List\[(.+)\]$')

    @property
    def is_simple(self) -> bool:
        """Является ли тип определяемый аннотацией `простым` типом."""
        if self.data in ('int', 'bool', 'float', 'str'):
            return True
        else:
            return False

    @property
    def is_simple_in_opt(self) -> bool:
        if self.inner_part_of_optional.is_simple:
            return True
        else:
            return False

    @property
    def is_simple_in_opt_and_not_opt(self) -> bool:
        if self.is_optional:
            if self.is_simple_in_opt:
                return True
            else:
                return False
        else:
            if self.is_simple:
                return True
            else:
                return False




    @property
    def is_list_of_list(self) -> bool:
        """Является ли тип определяемый аннотацией тип типом вида List[List[...]]."""
        if AnnotationWrapper.list_of_list_re.match(self.data):
            return True
        else:
            return False

    @property
    def is_optional(self) -> bool:
        """Является ли определяемый аннотацией тип опциональный."""
        if AnnotationWrapper.opt_field_re.match(self.data):
            return True
        else:
            return False

    @property
    def inner_part_of_optional(self) -> AnnotationWrapper:
        """Внутренняя часть опционального поля.

        Optional[User] -> User
        Optional[int] -> int
        """
        return AnnotationWrapper(re.search(AnnotationWrapper.inner_part_of_opt_re, self.data).group(1))

    @property
    def inner_part_of_list_of_list(self) -> AnnotationWrapper:
        """Внутренняя часть union поля.

        Union[User] -> 'User'
        Union[User, bool] -> 'User, bool'
        """
        return AnnotationWrapper(re.search(AnnotationWrapper.inner_part_of_list_of_list_re, self.data).group(1))

    @property
    def inner_part_of_union(self) -> AnnotationWrapper:
        """Внутренняя часть union поля.

        Union[User] -> 'User'
        Union[User, bool] -> 'User, bool'
        """
        return AnnotationWrapper(re.search(AnnotationWrapper.inner_part_of_union_re, self.data).group(1))

    @property
    def inner_part_of_list(self) -> AnnotationWrapper:
        """Внутренняя часть union поля.

        List[User] -> 'User'
        List[User, bool] -> 'User, bool'
        """
        return AnnotationWrapper(re.search(AnnotationWrapper.inner_part_of_list_re, self.data).group(1))



    @property
    def types_in_union(self) -> List[AnnotationWrapper]:
        """
        'Union[Message, bool]' -> ['Message', 'bool']
        """
        return list([AnnotationWrapper(word.strip()) for word in self.inner_part_of_union.split(',')])

    @property
    def sanitized(self) -> AnnotationWrapper:
        res = self.replace('typing.', '').\
            replace('telegrambotapiwrapper.api.types.', '').\
            replace('telegrambotapiwrapper.api.methods.', '').\
            replace("<class '", "").\
            replace("'>", "")
        return AnnotationWrapper(res)


    @property
    def is_list(self) -> bool:
        """Проверить, есть ли атрибут `data` строкой вида 'List[xxx], где xxx не строка вида List[yyy]'.

        'List[ChatMember]' -> True
        'List[List[ChatMember]]' -> False
        """
        if self.is_list_of_list:
            return False
        if AnnotationWrapper.list_field_re.match(self.data):
            return True
        else:
            return False

    @property
    def is_union(self) -> bool:
        """Проверить, есть ли атрибут `data` строкой вида 'Union[xxx]'.

        Union[Message, bool] -> True
        """
        if AnnotationWrapper.union_field_re.match(self.data):
            return True
        else:
            return False







