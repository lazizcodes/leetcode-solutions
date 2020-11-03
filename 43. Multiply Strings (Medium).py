class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        
        d = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        
        d1 = dict([(val, key) for key, val in d.items()])
        
        def stoi(s: string):
            n = 0
            for i in range(len(s)):
                x = d[s[i]]
                n = n * 10 + x
            return n
        
        def itos(n: int):
            s = ''
            dec = i = 0
            while n != 0:
                s += d1[n % 10]
                n //= 10
            return s[::-1]
        
        return itos(stoi(num1) * stoi(num2))