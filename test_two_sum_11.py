from two_sum_11 import two_sum_sorted, two_sum_pointer

def test_duplicate_values():
        for fn in (two_sum_sorted, two_sum_pointer):
         assert fn([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5], f"{fn.__name__}: duplicate values 4+4"



def test_negatives_allowed():
    for fn in (two_sum_sorted, two_sum_pointer):
         assert fn([-1, 0], -1) == [1, 2], f"{fn.__name__}: negatives allowed"

def test_give_target():
    for fn in (two_sum_sorted, two_sum_pointer):
        assert fn([2, 7, 11, 15], 9) == [1, 2], f"{fn.__name__}: 2+7"
        assert fn([2, 3,4], 6) == [1, 3], f"{fn.__name__}: 2+4"
        assert fn([1, 3, 4, 5, 7, 10, 11], 9) == [3, 4], f"{fn.__name__}:4+5"
        assert fn([5, 25, 75], 100) == [2,3], f"{fn.__name__}:25+75"

