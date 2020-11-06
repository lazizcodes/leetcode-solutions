class Solution:
    def fib(self, N: int) -> int:
        if N == 0: 
            return 0
        if N == 1: 
            return 1
        f0, f1 = 0, 1
        for i in range(1, N):
            f = f1
            f1 = f1 + f0
            f0 = f
        return f1