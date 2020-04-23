import builtins
import re

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class BuiltinMeta(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__ \
        (
            cls,
            name,
            bases,
            {
                **attrs,
                '__module__': 'builtins',
            },
        )

class BaseType(str, metaclass=BuiltinMeta):
    _patterns = ()

    def __new__(cls, value):
        if not cls._validate(value):
            raise TypeError \
            (
                'Invalid {class_name}: {value}'.format \
                (
                    class_name = cls.__name__,
                    value      = value,
                )
            )

        value = cls._clean(value)

        return str.__new__(cls, value)

    def __repr__(self):
        return '<{class_name}({value})>'.format \
        (
            class_name = self.__class__.__name__,
            value = super().__repr__(),
        )

    @classmethod
    def _validate(cls, value: str):
        if not cls._patterns:
            return True

        if not builtins.isinstance(value, str):
            return False

        for pattern in cls._patterns:
            match = re.match \
            (
                pattern = pattern,
                string  = value,
                flags   = re.DOTALL,
            )

            if match is not None:
                break
        else:
            return False

        return True

    @classmethod
    def _clean(cls, value: str):
        return value
