def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class GlobalCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

def runTests():
    gc1 = GlobalCounter()
    gc2 = GlobalCounter()
    assert id(gc1) == id(gc2)

runTests()