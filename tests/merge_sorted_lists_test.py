import pytest
from functions.merge_sorted_lists import merge_sorted_lists


def test_for_1_and_2():
    # Arrange
    list1 = [1]
    list2 = [2]

    # Act
    answer = merge_sorted_lists(list1, list2)

    # Assert
    assert answer == [1, 2]


def test_for_2_and_1():
    # Arrange
    list1 = [2]
    list2 = [1]

    # Act
    answer = merge_sorted_lists(list1, list2)

    # Assert
    assert answer == [1, 2]


def test_for_merge_two_list():
    # Arrange
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    # Act
    answer = merge_sorted_lists(list1, list2)

    # Assert
    assert answer == [1, 2, 3, 4, 5, 6]