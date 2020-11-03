class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i = 1
        while i * i <= x:
            if (i + 1) * (i + 1) > x:
                return i
            i += 1