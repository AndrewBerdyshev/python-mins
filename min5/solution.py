from typing import Callable
import math
import pytest

def cos(x):
    return math.cos(x)

def f(x, y):
    return x + y

def specialize(func: Callable, **kwargs) -> Callable:
    def specialized_func(*some_args):
        return func(*some_args, **kwargs)
    return specialized_func

def runTests():
    assert specialize(f, y=1)(2) == 3
    assert specialize(f, x=1, y=1)() == 2
    assert specialize(cos, x=math.pi)() == -1.0
    with pytest.raises(TypeError):
        assert specialize(f, z=1)()

runTests()
