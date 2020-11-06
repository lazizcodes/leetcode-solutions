# Binary Search Solution

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        if n == 1:
            return True
        left, right = 0, n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * mid == n:
                return True
            elif mid * mid > n:
                right = mid
            else:
                left = mid
        return False
        
        