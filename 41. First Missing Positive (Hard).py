class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums[:] = dict.fromkeys(nums)
        
        for num in range(1, len(nums) + 1):
            if num not in nums: return num
        return len(nums) + 1