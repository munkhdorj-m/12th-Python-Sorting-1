import ast
import inspect
import textwrap

import pytest

from assignment import (
    bubble_sort,
    bubble_sort_trace,
    insertion_sort,
    insertion_sort_trace,
    rank_students,
)


def check_no_builtin_sort(function):
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "sorted":
                pytest.fail(function.__name__ + " uses sorted(). Write the sorting algorithm yourself.")
            if isinstance(node.func, ast.Attribute) and node.func.attr == "sort":
                pytest.fail(function.__name__ + " uses .sort(). Write the sorting algorithm yourself.")


@pytest.mark.parametrize("data, expected", [
    [[5, 6, 1, 3], [1, 3, 5, 6]],
    [[64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]],
    [[1, 2, 3, 4], [1, 2, 3, 4]],
    [[4, 3, 2, 1], [1, 2, 3, 4]],
    [[3, 1, 3, 1, 2], [1, 1, 2, 3, 3]],
    [[-2, 5, -9, 0], [-9, -2, 0, 5]],
    [[7], [7]],
    [[], []],
])
def test1_bubble_sort(data, expected):
    check_no_builtin_sort(bubble_sort)
    assert bubble_sort(data) == expected


def test1_in_place():
    data = [9, 4, 7, 1]
    result = bubble_sort(data)
    assert data == [1, 4, 7, 9]
    assert result is data


@pytest.mark.parametrize("data, expected", [
    [[5, 6, 1, 3], [[5, 1, 3, 6], [1, 3, 5, 6]]],
    [[4, 3, 2, 1], [[3, 2, 1, 4], [2, 1, 3, 4], [1, 2, 3, 4]]],
    [[3, 2, 1], [[2, 1, 3], [1, 2, 3]]],
    [[1, 3, 2, 4], [[1, 2, 3, 4]]],
    [[3, 1, 3, 1], [[1, 3, 1, 3], [1, 1, 3, 3]]],
    [[2, 1], [[1, 2]]],
    [[1, 2, 3], []],
    [[7], []],
    [[], []],
])
def test2_bubble_trace(data, expected):
    check_no_builtin_sort(bubble_sort_trace)
    assert bubble_sort_trace(data) == expected
    assert data == sorted(data)


@pytest.mark.parametrize("data, expected", [
    [[5, 6, 1, 3], [1, 3, 5, 6]],
    [[64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]],
    [[1, 2, 3, 4], [1, 2, 3, 4]],
    [[4, 3, 2, 1], [1, 2, 3, 4]],
    [[3, 1, 3, 1, 2], [1, 1, 2, 3, 3]],
    [[-2, 5, -9, 0], [-9, -2, 0, 5]],
    [[7], [7]],
    [[], []],
])
def test3_insertion_sort(data, expected):
    check_no_builtin_sort(insertion_sort)
    assert insertion_sort(data) == expected


def test3_in_place():
    data = [9, 4, 7, 1]
    result = insertion_sort(data)
    assert data == [1, 4, 7, 9]
    assert result is data


@pytest.mark.parametrize("data, expected", [
    [[5, 6, 1, 3], [[5, 6, 1, 3], [1, 5, 6, 3], [1, 3, 5, 6]]],
    [[5, 2, 4, 6, 1, 3], [
        [2, 5, 4, 6, 1, 3],
        [2, 4, 5, 6, 1, 3],
        [2, 4, 5, 6, 1, 3],
        [1, 2, 4, 5, 6, 3],
        [1, 2, 3, 4, 5, 6],
    ]],
    [[3, 2, 1], [[2, 3, 1], [1, 2, 3]]],
    [[1, 2, 3], [[1, 2, 3], [1, 2, 3]]],
    [[2, 1], [[1, 2]]],
    [[7], []],
    [[], []],
])
def test4_insertion_trace(data, expected):
    check_no_builtin_sort(insertion_sort_trace)
    assert insertion_sort_trace(data) == expected
    assert data == sorted(data)


def test5_rank_students():
    check_no_builtin_sort(rank_students)
    records = [["Bat", 78], ["Saraa", 91], ["Tuya", 85], ["Anu", 60]]
    result = rank_students(records)
    assert result == [["Saraa", 91], ["Tuya", 85], ["Bat", 78], ["Anu", 60]]
    assert result is records
    assert rank_students([]) == []
    assert rank_students([["Bat", 50]]) == [["Bat", 50]]


def test5_ties_keep_order():
    check_no_builtin_sort(rank_students)
    records = [["Bat", 78], ["Saraa", 91], ["Anu", 78], ["Dorj", 91], ["Tuya", 85]]
    assert rank_students(records) == [
        ["Saraa", 91],
        ["Dorj", 91],
        ["Tuya", 85],
        ["Bat", 78],
        ["Anu", 78],
    ]
