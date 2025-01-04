#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, Any],
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary by its key.

    Parameters:
        dct (Mapping[Any, Any]): The dictionary to search.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): The default value to return if the key
                                  is not found.

    Returns:
        Union[Any, T]: The value associated with the key if it exists,
                       otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
