class Pair:

    def __init__(self, first=None, second=None):
        self.first = first
        self.second = first
        self.used = False

    def is_empty(self):
        if self.first is None or self.second is None:
            return True
        return False

    def __str__(self):
        if self.is_empty():
            return '=)'
        return f'({self.first} -> {self.second})'
