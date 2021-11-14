from sageutils.passutils import *


def test_permutate():
    assert (
        permutate("one two three four five six seven eight nine ten")
        == "one four ten five eight three six seven two nine"
    )
    assert (
        reverse_permutate("one four ten five eight three six seven two nine")
        == "one two three four five six seven eight nine ten"
    )
    print("Permutation tests passed")
