# given an array of integers numbers, sorted in non-decreasing order
# and a target

def two_sum_sorted(nums: list[int], target:int)-> list[int] | None:
    nums_list:list[int] = []
    for n in range(len(nums)):
        for j in range(len(nums)):
            # print(nums[n], nums[j])
            if nums[n] + nums[j] == target:
                print(n,j)
                nums_list.append(n+1)
                nums_list.append(j+1)
                return nums_list

print(two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8))

# assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], "2+7"
# assert two_sum_sorted([2, 3,4], 6) == [1, 3], "2+4"
# assert two_sum_sorted([-1, 0], -1) == [1, 2], "negatives allowed"
# assert two_sum_sorted([1, 3, 4, 5, 7, 10, 11], 9) == [3, 4], "4+5"
# assert two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5], "duplicate values, 4+4"
# assert two_sum_sorted([5, 25, 75], 100) == [2,3], "duplicate values, 4+4"
