class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n // 5 >= 1: 
            count += n // 5
            n //= 5
        return count