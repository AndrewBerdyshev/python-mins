def bitsCount(n: int) -> int:
    count = 0
    if n < 0:
        count += 1
    while n != 0 and n != -1:
        count += n & 1
        n >>= 1
    return count

def runTests():
    assert bitsCount(10) == 2
    assert bitsCount(-123) == 3
    assert bitsCount(0) == 0
    assert bitsCount(1) == 1
    assert bitsCount(2) == 1

runTests()
