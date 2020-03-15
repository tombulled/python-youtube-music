# Call program 'delve' ? -> dd

class TypeShell(object):
    def __init__(self, data):
        self.prompt = '>'
        self.depth = []
        self.data = data

    def interactive(self):
        while True:
            command = input(self._make_prompt()).strip()

            if command == 'ls':
                ...

    def _make_prompt(self):
        prompt = ''

        if not self.depth: return f'{self.prompt} '

        for item in self.depth:
            if isinstance(item, str):
                item = repr(item)

            prompt += f'{item} {self.prompt} '

        return prompt

    def _get_nested(self, iterable, *keys, default=None):
        if not keys or not iterable: return default

        working_val = iterable

        for key in keys[:-1]:
            working_val = self.iter_get(working_val, key, {})

        return self.iter_get(working_val, keys[-1], default=default) if working_val else default

    def iter_get(self, iterable, key, default=None):
        if not iterable: return iterable

        try:
            return iterable.__getitem__(key)
        except (KeyError, IndexError):
            return default

def type_shell(data):
    shell = TypeShell(data)

    shell.interactive()
