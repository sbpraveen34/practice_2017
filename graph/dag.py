class edge:
    def __init__(self, end, weight):
        self.end = end
        self.weight = weight

class graph:
    def __init__(self, n):
        self.edge = [ [] for _ in xrange(0, n) ]
    
