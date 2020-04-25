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
