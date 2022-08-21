class Counter:
    count = 0

    def __init__(self, min, max, loop = False) -> None:
        self.min = min
        self.max = max
        self.count = min
        self.loop = loop

    def increment(self):
        self.count = self.count + 1 if self.count < self.max else self.min
    
    def decrement(self):
        self.count = self.count - 1 if self.count > self.min else self.min
    
    def reset(self):
        self.count = self.min

    def get(self):
        return self.count

    def set(self, val):
        self.count = val if self.min <= val and self.max >= val else self.count