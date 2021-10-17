import typing


def merge(*iterables: typing.Iterable) -> typing.List:
    merged = []
    for iterable in iterables:
        merged.extend(iterable)
    return sorted(merged)
