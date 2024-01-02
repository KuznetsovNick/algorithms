from modules.find_length import find_length
from modules.make_tree import make_tree


def test_1():
    parents = [-1]
    leafs = make_tree(parents)
    assert find_length(leafs, parents) == 1


def test_2():
    parents = [-1, 0, 4, 0, 3]
    leafs = make_tree(parents)
    assert find_length(leafs, parents) == 4


def test_3():
    parents = [-1, 0, 0, 0, 0, 0, 0, 0]
    leafs = make_tree(parents)
    assert find_length(leafs, parents) == 2


def test_4():
    parents = [7, 0, 6, 2, 5, 1, 4, -1]
    leafs = make_tree(parents)
    assert find_length(leafs, parents) == 8


def test_5():
    parents = [-1, 0, 1, 2, 2, 4]
    leafs = make_tree(parents)
    assert find_length(leafs, parents) == 5
