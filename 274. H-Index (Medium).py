class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = [0] * (n + 1)
        for i in range(n):
            l[min(n, citations[i])] += 1
        s = 0
        i = n
        while i >= 0:
            s += l[i]
            if i <= s: return i
            i -= 1