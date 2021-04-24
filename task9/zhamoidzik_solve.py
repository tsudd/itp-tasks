class Range(object):
    def __init__(self, *args):
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        else:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        self.left = min(self.start, self.stop) - 1
        self.right = max(self.start, self.stop)
        if self.step < 0:
            self.right += 1
            self.left += 1

    def __iter__(self):
        self.counter = self.start
        return self

    def __next__(self):
        if (self.counter > self.left) & (self.counter < self.right):
            temp = self.counter
            self.counter += self.step
            return temp
        else:
            raise StopIteration()
