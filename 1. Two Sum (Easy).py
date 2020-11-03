class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in memo:
                memo[num] = i
            else:
                return [memo[n], i]