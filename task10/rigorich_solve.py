
class SequenceIterator():

    def __init__(self, sequence: object):
        self._sequence = sequence
        self._iterator = iter(self._sequence._contents)
    
    def __next__(self):
        while True:
            elem = next(self._iterator)
            if self._sequence._filter(elem):
                return elem


class Sequence():

    def __init__(self, iterable: object):
        self._contents = iterable
        self._filter = lambda foo: True
    
    def __iter__(self):
        return SequenceIterator(self)
    
    def Filter(self, func):
        newseq = Sequence(self)
        newseq._filter = func
        return newseq



def test():

    numbers = [i for i in range(1, 10)]
    seq = Sequence(numbers)

    print(numbers)
    print(seq)

    def Print(iterable):
        for elem in iterable:
            print(elem, end=' ')
        print()

    Print( numbers )

    Print( seq )

    Print( seq )

    Print( seq.Filter(lambda x: x % 2 == 0) )

    Print( Sequence(numbers).Filter(lambda x: x % 3 == 0).Filter(lambda x: x > 5) )

#test()