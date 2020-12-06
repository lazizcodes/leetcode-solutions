class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        memo = {i: 0 for i in nums}
        for i in range(len(nums)):
            if k - nums[i] in memo and memo[k - nums[i]] > 0:
                res += 1
                memo[k - nums[i]] -= 1
            else:
                memo[nums[i]] += 1
        return res