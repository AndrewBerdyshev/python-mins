from typing import Callable
import math
import pytest


def flatten(lst: list, depth = math.inf) -> list:
    if depth < 0:
        raise NameError('Negative depth')
    result = []
    for el in lst:
        if isinstance(el, list) and depth > 0:
            for fel in flatten(el, depth - 1):
                result.append(fel)
        else:
            result.append(el)
    return result

def runTests():
    assert flatten([1, 2, [4, 5], [6, [7]], 8]) == [1, 2, 4, 5, 6, 7, 8]
    assert flatten([1, 2, [4, 5], [6, [7]], 8], 1) == [1, 2, 4, 5, 6, [7], 8]
    assert flatten([], 2) == []
    assert flatten([1, [2, [3, [4]]]], 1) == [1, 2, [3, [4]]]
    assert flatten([1, [2, [3, [4]]]], 1) == [1, 2, [3, [4]]]
    assert flatten([1, [2, [3, [4]]]], 0) == [1, [2, [3, [4]]]]
    assert flatten([[1, 2], [3, 4]], 1) == [1, 2, 3, 4]
    assert flatten([[1, 2], [3, 4]], 2) == [1, 2, 3, 4]
    assert flatten([[[1]], [[2]], [[3]]], 0) == [[[1]], [[2]], [[3]]]
    assert flatten([[[1]], [[2]], [[3]]], 2) == [1, 2, 3]
    assert flatten([1, [2, [3, [4, [5]]]]], 2) == [1, 2, 3, [4, [5]]]
    assert flatten([1, [2, [3, [4, [5]]]]], 4) == [1, 2, 3, 4, 5]
    with pytest.raises(NameError):
        assert flatten([1], -1)


runTests()
