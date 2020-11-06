class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stack = dict()
        for i in range(len(nums)):
            if nums[i] in stack:
                return nums[i]
            else:
                stack[nums[i]] = nums[i]

# Follow-ups:

# 1. By Pigeonhole Principle there must exist
# at least one duplicate since n + 1 > n.

# 2. Yes, see the solution

# 3. With only constant extra space I could solve with O(n^2)
# runtime complexity [worst case] (counting each number)

# 4. Not yet :)
        
        