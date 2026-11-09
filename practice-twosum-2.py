def two_sum(nums: list[int], target:int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return seen[difference], i
        seen[num] = i
    return None


print(two_sum([1,2,3,4], 3))



  