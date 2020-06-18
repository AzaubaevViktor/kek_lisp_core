class BaseSource:
    def __init__(self, name=None):
        self.name = name

    def __iter__(self):
        raise NotImplementedError()


class SourceStr(BaseSource):
    def __init__(self, data, name=None):
        super().__init__(name)
        self._data = data
