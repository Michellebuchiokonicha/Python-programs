# given an array of integers numbers, sorted in non-decreasing order
# and a target

def two_sum_sorted(nums: list[int], target:int)-> list[int] | None:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if  i != j and nums[i] + nums[j] == target:
                return [i + 1, j + 1]
    return None




def two_sum_pointer(nums: list[int], target:int)-> list[int] | None:
    left = 0
    right = len(nums) - 1
    while left < right:
        current  = nums[left] + nums[right]
        if current == target:
            return [left + 1, right + 1]
        elif current > target:
            right -= 1
        else:
            left += 1
    return None
        

for fn in (two_sum_sorted, two_sum_pointer):
    assert fn([2, 7, 11, 15], 9) == [1, 2], f"{fn.__name__}: 2+7"
    assert fn([2, 3,4], 6) == [1, 3], f"{fn.__name__}: 2+4"
    assert fn([-1, 0], -1) == [1, 2], f"{fn.__name__}: negatives allowed"
    assert fn([1, 3, 4, 5, 7, 10, 11], 9) == [3, 4], f"{fn.__name__}:4+5"
    assert fn([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5], f"{fn.__name__}:duplicate values, 4+4"
    assert fn([5, 25, 75], 100) == [2,3], f"{fn.__name__}:25+75"
