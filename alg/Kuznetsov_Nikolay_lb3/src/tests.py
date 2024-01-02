from modules.process import process


def test1():
    assert process(2, 5, [1, 2, 3, 4, 5]) == [[0, 0], [1, 0], [0, 1], [1, 2], [0, 4]]


def test2():
    assert process(0, 0, []) == []


def test3():
    assert process(10, 2, []) == []


def test4():
    assert process(3, 7, [11, 9, 8, 7, 6, 3, 1]) == [[0, 0], [1, 0], [2, 0], [2, 8], [1, 9], [0, 11], [0, 14]]


def test5():
    assert process(5, 5, [1, 2, 3, 4, 5]) == [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]


def test6():
    assert process(1, 3, [6, 21, 8]) == [[0, 0], [0, 6], [0, 27]]