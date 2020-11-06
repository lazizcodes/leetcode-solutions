class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        res = 0
        for i in range(n):
            if i == 0:
                nums.append(start + 2 * i)
                res = nums[i]
            else:
                nums.append(start + 2 * i)
                res = res ^ nums[i]
        return res
            
        