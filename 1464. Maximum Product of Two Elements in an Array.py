class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M = max(nums)
        i = nums.index(M)
        nums.pop(i)
        m = max(nums)
        j = nums.index(m)
        return (M - 1) * (m - 1)