'''
File to test Sorting Algorithms for 5 different test cases
'''

import pytest
from sorting import *

# _sort_funct can be ["bubble_sort", "selection_sort", "insertion_sort"]
_sort_funct = insertion_sort

# sorting Function to test it with 5 test cases
def test_case_1():
   
    # Test Case 1 - unsorted list
    unsorted_list = [5, 3, 8, 1, 2]
    assert _sort_funct(unsorted_list) == [1, 2, 3, 5, 8]

def test_case_2():
    # Test Case 2 - already sorted list
    sorted_list = [1, 2, 3, 5, 8]
    assert _sort_funct(sorted_list) == [1, 2, 3, 5, 8]

def test_case_3():
    # Test Case 3 - list containing duplicate elements
    duplicate_list = [5, 3, 8, 1, 2, 3, 5]
    assert _sort_funct(duplicate_list) == [1, 2, 3, 3, 5, 5, 8]

def test_case_4():
    # Test Case 4 - empty list
    empty_list = []
    assert _sort_funct(empty_list) == []

def test_case_5():
    # Test Case 5 - list containing only one element
    single_element_list = [42]
    assert _sort_funct(single_element_list) == [42]

if __name__ == "__main__":
    pytest.main(["-vv"])