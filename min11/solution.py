from typing import Iterable, List
import itertools

def cycle(it: Iterable):
    if len(it) == 0:
        return []
    i = iter(it)
    curr = next(i)
    while True:
        try:
            yield curr
            curr = next(i)
        except StopIteration:
            i = iter(it)
            curr = next(i)

def take(seq, num) -> List:
    return list(itertools.islice(seq, num))

def test1(capsys):
    assert take(itertools.cycle([1, 2, 3]), 10) == take(cycle([1, 2, 3]), 10)

def test2(capsys):
    assert take(itertools.cycle([]), 5) == take(cycle([]), 5)

def test3(capsys):
    assert take(itertools.cycle([42]), 5) == take(cycle([42]), 5)

def test4(capsys):
    assert take(itertools.cycle([1, 2, 3, 4, 5]), 12) == take(cycle([1, 2, 3, 4, 5]), 12)

def test5(capsys):
    assert take(itertools.cycle(['a', 'b', 'c']), 9) == take(cycle(['a', 'b', 'c']), 9)
