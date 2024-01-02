class Processor:
    def __init__(self, index, start, time):
        self.index = index
        self.start = start
        self.time = time

    def __lt__(self, other):
        if self.time + self.start == other.time + other.start:
            return self.index < other.index
        return self.time + self.start < other.time + other.start

    def __str__(self):
        return f'{self.index} {self.start}'
