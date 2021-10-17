import typing


class SortedList:
    """ Sorted List """

    def __init__(self):
        self._data = []
        self._index = 0

    def bisect(self, item: int) -> int:
        """ Returns the insertion point of the 'item' that will maintain the sorted order of the 'self._data' """
        begin = 0
        end = len(self._data)
        while begin < end:
            mid = (begin + end) // 2
            if item < self._data[mid]:
                end = mid
            else:
                begin = mid + 1
        return begin

    def add(self, value: int) -> None:
        """ Add an item to data list by keeping it sorted"""
        index = self.bisect(value)
        self._data.insert(index, value)

    def __iter__(self):
        """ Returns self as iterator object """
        return self

    def __next__(self):
        """ Returns the next value from self._data """
        if self._index < len(self._data):
            result = (self._data[self._index])
            self._index += 1
            return result
        # End of Iteration
        raise StopIteration

    def __repr__(self):
        """ Returns a string representation """
        return '{}({})'.format(self.__class__.__name__, ''.join(str(self._data)))

    def __str__(self):
        """ Returns a human readable representation """
        return ''.join(str(self._data))


def merge(*iterables: typing.Iterable) -> SortedList:
    """ Returns merged queue of sorted iterables """
    merged = SortedList()
    for iterable in iterables:
        for item in iterable:
            merged.add(item)
    return merged
