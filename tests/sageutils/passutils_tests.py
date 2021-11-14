from sageutils.passutils import *


def test_permutate():
    assert (
        Permutater.permutate("one two three four five six seven eight nine ten")
        == "one four ten five eight three six seven two nine"
    )
    assert (
        Permutater.reverse_permutate("one four ten five eight three six seven two nine")
        == "one two three four five six seven eight nine ten"
    )
    print("Permutation tests passed")


def test_check_hashseed():
    assert check_hashseed()
