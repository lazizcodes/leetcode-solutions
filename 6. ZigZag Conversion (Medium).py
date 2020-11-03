class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        res = ''
        mod = 2 * n - 2
        for i in range(n):
            for j in range(i, len(s), mod):
                res += s[j]
                k = j - 2 * i + mod
                if i not in [0, n - 1] and k < len(s):
                    res += s[k]
        return res