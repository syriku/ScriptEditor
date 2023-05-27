class FakeDict(object):

    def __init__(self, tov):
        self.items = []
        self.type = tov

    def __dict__(self):
        return dict(self.items)

    def __getitem__(self, item):
        for key, value in self.items:
            if key == item:
                return value

    def keys(self):
        return [key for key, _ in self.items]

    def values(self):
        return [value for _, value in self.items]

    def insert(self, key, value, index=-1):
        assert isinstance(value, self.type), TypeError(f"value:{value} that try to insert is not {self.type}")
        assert index >= -1, ValueError("index cannot be negative.")
        if index == -1:
            self.items.append([key, value])
        else:
            self.items.insert(index, [key, value])
