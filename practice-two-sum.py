def two_sum(nums:list[int], target:int) -> tuple[int, int] | None:
    """Return indices (i, j) of two numbers that add up to target, or None."""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            print(seen[difference])
            return seen[difference], i
        seen[num] = i


print(two_sum([1,2,1,4], 3))