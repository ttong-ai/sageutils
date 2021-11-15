#!/usr/bin/env python
import fire
from sageutils.passutils import (
    permutate as _permutate,
    reverse_permutate as _reverse_permutate,
)


class Permutater:
    @classmethod
    def permutate(cls, input: str, key: str = None):
        return _permutate(input=input, key=key)

    @classmethod
    def reverse_permutate(cls, input: str, key: str = None):
        return _permutate(input=input, key=key)


if __name__ == "__main__":
    fire.Fire(Permutater)
