def myZip(a: list, b: list) -> list:
    res = []
    for i in range(min(len(a), len(b))):
        res.append((a[i], b[i]))
    return res

def runTests():
    assert myZip([1, 2, 3], ["a","b"]) == [(1, "a"), (2, "b")]
    assert myZip([1, 1, 1], [1, 1]) == [(1, 1), (1, 1)]
    assert myZip(['1', 1, 0], ["a",'b', 5, 4, 3]) == [('1', "a"), (1, 'b'), (0, 5)]

runTests()
