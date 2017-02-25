'''Create a list class'''


class SimpleList:
    '''The list base class'''

    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        '''Append to list'''
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        '''Sort the list'''
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    '''Sorts the list after every method'''

    def __init__(self, items=[]):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    '''List of only integers'''

    def __init__(self, items=[]):
        for element in items:
            self._validate(element)
        super().__init__(items)

    @staticmethod
    def _validate(element):
        if not isinstance(element, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))


class SortedIntList(IntList, SortedList):

    def __repr__(self):
        return 'SortedIntList({!r})'.format(list(self))
