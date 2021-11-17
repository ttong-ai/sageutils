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
    assert permutate("1 2 3 4 5 6", key="grace") == "5 3 6 2 4 1"
    assert permutate("1 2 3 4 5 6", key="gracE") != "5 3 6 2 4 1"
    assert reverse_permutate("5 3 6 2 4 1", key="grace") == "1 2 3 4 5 6"
    assert reverse_permutate("5 3 6 2 4 1", key="Grace") != "1 2 3 4 5 6"
    assert (
        permutate("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24", key="grace")
        == "11 9 17 14 24 7 4 15 6 19 13 2 10 5 12 1 18 23 20 21 22 8 16 3"
    )
    assert (
        permutate("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24", key="gracE")
        != "11 9 17 14 24 7 4 15 6 19 13 2 10 5 12 1 18 23 20 21 22 8 16 3"
    )
    assert (
        permutate("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24")
        != "11 9 17 14 24 7 4 15 6 19 13 2 10 5 12 1 18 23 20 21 22 8 16 3"
    )
    assert (
        reverse_permutate("11 9 17 14 24 7 4 15 6 19 13 2 10 5 12 1 18 23 20 21 22 8 16 3", key="grace")
        == "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24"
    )
    assert (
        reverse_permutate("11 9 17 14 24 7 4 15 6 19 13 2 10 5 12 1 18 23 20 21 22 8 16 3", key="Grace")
        != "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24"
    )
    assert (
        reverse_permutate("11 9 17 14 24 7 4 15 6 19 13 2 10 5 12 1 18 23 20 21 22 8 16 3")
        != "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24"
    )
    print("Permutation tests passed")


def test_check_hashseed():
    assert check_hashseed()
