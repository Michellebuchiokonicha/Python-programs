# given an array of integers numbers, sorted in non-decreasing order
# and a target




assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], "2+7"
assert two_sum_sorted([2, 3,4], 6) == [1, 3], "2+4"
assert two_sum_sorted([-1, 0], -1) == [1, 2], "negatives allowed"
assert two_sum_sorted([1, 3, 4, 5, 7, 10, 11], 9) == [3, 4], "4+5"
assert two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5], "duplicate values, 4+4"
assert two_sum_sorted([5, 25, 75], 100) == [2,3], "duplicate values, 4+4"
