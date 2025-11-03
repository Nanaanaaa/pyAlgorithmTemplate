rnd = randint(0, 2**63 - 1)


class defaultdict(collections.defaultdict):
    def __init__(self, default_factory=None):
        super().__init__(default_factory)

    def __getitem__(self, key):
        return super().__getitem__(key ^ rnd)

    def __setitem__(self, key, value):
        super().__setitem__(key ^ rnd, value)

    def __contains__(self, key):
        return super().__contains__(key ^ rnd)

    def __iter__(self):
        for k in super().keys():
            yield k ^ rnd

    def items(self):
        for k, v in super().items():
            yield (k ^ rnd, v)

    def keys(self):
        for k in super().keys():
            yield k ^ rnd

    def __repr__(self):
        body = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"{self.__class__.__name__}({self.default_factory}, {{{body}}})"

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        value = self.default_factory()
        super().__setitem__(key, value)
        return value
