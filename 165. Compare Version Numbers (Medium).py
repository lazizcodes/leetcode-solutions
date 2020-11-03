class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        t1 = tuple([int(i) for i in version1.split('.')])
        t2 = tuple([int(i) for i in version2.split('.')])
        m, n = len(t1), len(t2)
        if m > n: t2 = t2 + (0,) * (m - n)
        if m < n: t1 = t1 + (0,) * (n - m)
        if t1 > t2: return 1
        if t1 < t2: return -1
        return 0