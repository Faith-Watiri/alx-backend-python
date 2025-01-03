#!/usr/bin/env python3
""" Contains a function that converts a Python variable to a KV pair. """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Convert a python variable to a kv pair. """
    return k, v ** 2
