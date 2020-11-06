class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        left, right, prod = 0, 0, 1
        while right < n:
            prod *= nums[right]
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
            right += 1
        return res
            
        
                
            