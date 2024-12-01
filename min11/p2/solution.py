import itertools

def chain(*args):
    for it in args:
        if len(it) == 0:
            continue
        i = iter(it)
        curr = next(i)
        while True:
            try:
                yield curr
                curr = next(i)
            except StopIteration:
               break

def test1(capsys):
    assert list(itertools.chain([1, 2, 3], ['a', 'b'], [42, 13, 7])) == \
    list(chain([1, 2, 3], ['a', 'b'], [42, 13, 7]))

def test2(capsys):
    assert list(itertools.chain([], [], [])) == list(chain([], [], []))

def test3(capsys):
    assert list(itertools.chain([1, 2, 3])) == list(chain([1, 2, 3]))

def test4(capsys):
    assert list(itertools.chain((1, 2), {3, 4}, 'abc')) == list(chain((1, 2), {3, 4}, 'abc'))

def test5(capsys):
    assert list(itertools.chain([[1, 2], [3, 4], [5]])) == list(chain([[1, 2], [3, 4], [5]]))