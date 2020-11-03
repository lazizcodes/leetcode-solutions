class Solution:
    def rob(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        
        if len(nums) in [1, 2]:
            return max(nums)        
        
        def HouseRob(array):
            if not array:
                return 0
            if len(array) in [1, 2]:
                return max(array)
            sz = len(array)
            dp = [array[0], max(array[0], array[1])]
            for i in range(2, sz):
                dp.append(max(dp[i - 1], dp[i - 2] + array[i]))
            return dp[sz - 1]
        
        n = len(nums)
        return max(HouseRob(nums[0 : n - 1]), HouseRob(nums[1 : n]))