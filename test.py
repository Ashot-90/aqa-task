from functools import wraps
import merge_1
import merge_2
import merge_3
import merge_4
import heapq
import time
import pytest


def test_single():
    expected = [0, 1, 2]
    result1 = list(merge_1.merge(range(3)))
    result2 = list(merge_2.merge(range(3)))
    result3 = list(merge_3.merge(range(3)))
    assert result1 == expected
    assert result2 == expected
    assert result3 == expected

    result1 = list(merge_1.merge(range(3)))
    result2 = list(merge_2.merge(range(3)))
    result3 = list(merge_3.merge(range(3)))
    assert result1 == expected
    assert result2 == expected
    assert result3 == expected


def test_simple():
    expected = [0, 1, 2, 3, 4, 5]
    result1 = list(merge_1.merge([0, 1, 2], [3, 4, 5]))
    result2 = list(merge_2.merge([0, 1, 2], [3, 4, 5]))
    result3 = list(merge_3.merge([0, 1, 2], [3, 4, 5]))
    assert result1 == expected
    assert result2 == expected
    assert result3 == expected

    result1 = list(merge_1.merge([0, 2, 4], [1, 3, 5]))
    result2 = list(merge_2.merge([0, 2, 4], [1, 3, 5]))
    result3 = list(merge_3.merge([0, 2, 4], [1, 3, 5]))
    assert result1 == expected
    assert result2 == expected
    assert result3 == expected

    result1 = list(merge_1.merge([3, 4, 5], [0, 1, 2], ))
    result2 = list(merge_2.merge([3, 4, 5], [0, 1, 2], ))
    result3 = list(merge_3.merge([3, 4, 5], [0, 1, 2], ))
    assert result1 == expected
    assert result2 == expected
    assert result3 == expected


def test_not_supported_types():
    with pytest.raises(TypeError, match="not supported between instances of"):
        list(merge_1.merge([0, 1, 2], ["a", "b", "c"]))
    with pytest.raises(TypeError, match="not supported between instances of"):
        list(merge_2.merge([0, 1, 2], ["a", "b", "c"]))
    with pytest.raises(TypeError, match="not supported between instances of"):
        list(merge_3.merge([0, 1, 2], ["a", "b", "c"]))


def timeit(test_function):
    @wraps(test_function)
    def wrapper():
        start = time.perf_counter_ns()
        test_function()
        print("\nExecution time of '{}' was : '{}'".format(test_function.__name__, time.perf_counter_ns() - start))
    return wrapper


@timeit
def test_performance_merge_1():
    merge_1.merge(range(0, 1000), range(0, 1000))


@timeit
def test_performance_merge_2():
    merge_2.merge(range(0, 1000), range(0, 1000))


@timeit
def test_performance_merge_3():
    merge_3.merge(range(0, 1000), range(0, 1000))


@timeit
def test_performance_merge_4():
    merge_4.merge([*range(0, 1000)], [*range(0, 1000)])


@timeit
def test_performance_merge_heapq():
    heapq.merge(range(0, 1000), range(0, 1000))
