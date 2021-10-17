import typing
from sortedcontainers import SortedList


def merge(*iterables: typing.Iterable) -> SortedList:
    merged = SortedList()
    for iterable in iterables:
        merged.update(iterable)
    return merged
