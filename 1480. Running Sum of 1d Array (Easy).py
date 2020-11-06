class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum([nums[j] for j in range(i + 1)]) for i in range(len(nums))]