def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

    seen = set()

    # for num in nums:
    #     if num in seen:
    #         return True
    #     seen.add(num)
    # return False


assert contains_duplicate([1, 2, 3, 1]) is False, "not duplicates fives False"
