class Solution:
    def reverse(self, x):        
        def sign(a):
            return a > 0
       
        if x ==0 or x > 2**31: 
            return 0
        
        y = abs(x)
        res = 0

        while y != 0:
            r = y % 10
            res = 10 * res + r
            y //= 10
        if res in range(-2**31, 2**31):
            return res if sign(x) else -res
        return 0