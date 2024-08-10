class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = list(set(nums))
        distinct_nums = sorted(distinct_nums, reverse = True)
        if len(distinct_nums) >= 3:
            return distinct_nums[2]
        else:
            return distinct_nums[0]

