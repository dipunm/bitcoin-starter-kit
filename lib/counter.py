class Counter:
    count = 0

    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max
        self.count = min

    def increment(self):
        self.count = self.count + 1 if self.count < self.max else self.max
    
    def decrement(self):
        self.count = self.count - 1 if self.count > self.min else self.min
    
    def reset(self):
        self.count = self.min

    def get(self):
        return self.count