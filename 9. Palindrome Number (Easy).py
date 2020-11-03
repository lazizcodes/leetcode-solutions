class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        i = 0
        x1 = x
        while x1 != 0:
            y = y * 10 + (x1 % 10)
            i += 1
            x1 //= 10
        return y == x