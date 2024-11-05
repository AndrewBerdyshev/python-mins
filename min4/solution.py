def reverse(data: dict) -> dict:
    result = {}
    for i in data:
        if data[i] not in result:
            result[data[i]] = i
        elif not isinstance(result[data[i]], tuple):
            result[data[i]] = tuple([result[data[i]], i])
        else:
            result[data[i]] += tuple([i])
    return result
def runTests():
    assert reverse({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}
    assert reverse({}) == {}
    assert reverse({"John": 12345}) == {12345: "John"}
    assert reverse({"Alice": 11111, "Bob": 11111, "Charlie": 22222}) == {11111: ("Alice", "Bob"), 22222: "Charlie"}
    assert reverse({"User 1": 1, "User 2": 2, "User 3": 3, "User 4": 1, "User 5": 2, "User 6": 3}) == {1: ("User 1", "User 4"), 2: ("User 2", "User 5"), 3: ("User 3", "User 6")}
    assert reverse({"Ivanov": 97832, "Petrov": 55521, "I": 97832, "K": 97832, "Kuznecov": 97832, "U": 97832}) == {97832: ('Ivanov', 'I', 'K', 'Kuznecov', 'U'), 55521: 'Petrov'}

runTests()
