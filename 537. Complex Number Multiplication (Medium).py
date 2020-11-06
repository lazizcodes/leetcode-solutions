class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def plus(z):
            return z.index('+')
        a1 = int(a[ : plus(a)])
        b1 = int(a[plus(a) + 1 : -1])
        a2 = int(b[ : plus(b)])
        b2 = int(b[plus(b) + 1 : -1])
        return str(a1 * a2 - b1 * b2) + '+' + str(a1 * b2 + a2 * b1) + 'i'