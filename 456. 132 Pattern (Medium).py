class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        k = sys.maxsize * (-1)
        stack = []
        
        i = n - 1
        while i >= 0:
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = stack[-1]
                stack.pop()
            stack.append(nums[i])
            i -= 1
        return False