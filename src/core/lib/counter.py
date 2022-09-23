class Counter:
    count = 0

    def __init__(self, min, max, loop = False) -> None:
        self.min = min
        self.max = max
        self.count = min
        self.loop = loop

    def increment(self):
        if self.count < self.max:
            self.count += 1
        elif self.loop and self.count == self.max:
            self.count = self.min
    
    def decrement(self):
        if self.count > self.min:
            self.count -= 1
        elif self.loop and self.count == self.min:
            self.count = self.max
    
    def reset(self):
        self.count = self.min

    def get(self):
        return self.count

    def set(self, val):
        self.count = val if self.min <= val and self.max >= val else self.count