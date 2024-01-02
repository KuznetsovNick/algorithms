class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0  # высота считается в ребрах

    def __str__(self):
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        return 'key: {}, left: {}, right: {}'.format(self.key, left, right)