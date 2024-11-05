def parseMatrix(data: str) -> list:
    res = []
    for i in data.split("|"):
        line = []
        for j in i.split():
            line.append(float(j))
        res.append(line)
    return res

def runTests():
    assert parseMatrix("1 2 | 3 4") == [[1.0, 2.0], [3.0, 4.0]]
    assert parseMatrix("1 2 3 | 4 5 6 | 7 8 9") == [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    assert parseMatrix("1 2 3 4 | 5 6 7 8") == [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]]

runTests()
