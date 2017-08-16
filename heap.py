class Heap:
    def __init__(self, n):
        self.heap = [None]*n
        self.capacity = n
        self.heap_len = 0

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2
