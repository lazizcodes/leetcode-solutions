class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = dp = nums[0]
        
        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            res = max(res, dp)
        
        return res