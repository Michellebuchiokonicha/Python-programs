# def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
#     """Return indices (i, j) with i < j of the first pair summing to target, or None if no pair exists."""
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return i, j
#     return None


# assert two_sum([1, 2, 3, 4, 5, 6], 3) == (0, 1), "basic case: 1 + 2 = 3"
# print(two_sum([1, 2, 3, 4, 5, 6], 3), 'memme')



def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """0(n) version: one pass, remembering each value's index in a dict."""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return seen[diff], i
        seen[num] = i

    return None
print(two_sum_fast([1, 2, 3, 4, 5, 6], 3))
print(two_sum_fast([3, 3], 6))
print(two_sum_fast([3], 6))
print(two_sum_fast([1, 5], 2))
print(two_sum_fast([], 5))
print(two_sum_fast([-1,4,2], 3))

assert two_sum_fast([1, 2, 3, 4, 5, 6], 3) == (0, 1)
assert two_sum_fast([3, 3], 6) == (0, 1), "duplicates: must not pair an element with itself"
assert two_sum_fast([3], 6) == None, "duplicates: must not pair an element with itself"
assert two_sum_fast([1, 5], 2) == None, "duplicates: must not pair an element with itself"
assert two_sum_fast([-1, 4, 2], 3) == (0, 1), "duplicates: must not pair an element with itself"



