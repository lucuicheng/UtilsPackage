class Target(object):

    def __init__(self, name, alias) -> None:
        self._name = name
        self._alias = alias
        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def alias(self):
        return self._alias
