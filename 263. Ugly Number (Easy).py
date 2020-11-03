class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        div = [2, 3, 5]
        for i in div:
            while num % i == 0:
                num //= i
        return num == 1