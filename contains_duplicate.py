# [1, 2, 3, 1]        → True
# [1, 2, 3, 4]        → False
# [1, 1, 1, 3, 3, 4]  → True

# given a list of integers nums, return True if any value appears at least twice, and False if every element is distinct.


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice in nums, otherwise False."""
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# def contains_duplicate_size(nums: list[int]) -> bool:
#     """Same answer as contains_duplicate: set() drops repeats, so a smaller set means a duplicate."""
    # return len(set(nums)) != len(nums)

def contains_duplicate_size(nums: list[int]) -> bool:
    """Same answer as contains_duplicate: set() drops repeats, so a smaller set means a duplicate."""
    return len(set(nums)) != len(nums)


for fn in (contains_duplicate, contains_duplicate_size):
    assert fn([1, 2, 3, 1]) is True, f"{fn.__name__}: duplicate at the ends"
    assert fn([1, 1, 1, 3, 3, 4]) is True, f"{fn.__name__}: multiple duplicates"
    assert fn([1, 2, 3, 4]) is False, f"{fn.__name__}: all distinct"
    assert fn([]) is False, f"{fn.__name__}: empty list has no duplicates"
    assert fn([7]) is False, f"{fn.__name__}: single element can't repeat"
