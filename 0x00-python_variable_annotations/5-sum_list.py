#!/usr/bin/env python3
""" type-annotated function """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sums a list of floats
    Args:
        input_list (list): A list floats
    Returns:
        float: the sum of the floats in the List
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
