class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}
        while n != 1:
            if n in memo:
                return False
            memo[n] = 1
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n = n // 10
            n = _sum
        return True