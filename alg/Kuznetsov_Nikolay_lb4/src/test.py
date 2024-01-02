from modules.solve import solve


def test1():
	assert solve('a', 'aaaaaaaaaaa') == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test2():
	assert solve('a', 'yuopjnmoiujkliuh') == []


def test3():
	assert solve('aba', 'abababababababacaba') == [0, 2, 4, 6, 8, 10, 12, 16]


def test4():
	assert solve('a1', 'a11aa11aa11a') == [0, 4, 8]


def test5(): 
	assert solve('a_', 'aaaabbaa') == []
