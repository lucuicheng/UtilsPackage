class Target(object):

    def __init__(self, name, alias, columns) -> None:
        self._name = name
        self._alias = alias
        self._columns = columns
        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def alias(self):
        return self._alias

    @property
    def columns(self):
        return self._columns
