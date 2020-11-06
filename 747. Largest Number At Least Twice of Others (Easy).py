class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            n, m = sorted(nums)[-2:]
            if m >= 2 * n:
                return nums.index(m)
            else:
                return -1
            
            
