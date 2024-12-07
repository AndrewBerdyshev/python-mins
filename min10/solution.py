class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GlobalCounter(metaclass=SingletonMeta):
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


def test1(capsys):
    gc1 = GlobalCounter()
    gc2 = GlobalCounter()
    assert id(gc1) == id(gc2)
    gc1.increment()
    assert gc1.get_count() == 1
    assert gc2.get_count() == 1