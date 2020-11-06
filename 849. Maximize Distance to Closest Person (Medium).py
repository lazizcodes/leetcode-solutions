class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        res = left = -1
        for i in range(n):
            if seats[i] == 1:
                if left == -1:
                    res = i
                else:
                    res = max(res, (i - left) // 2)
                left = i
        res = max(res, n - 1 - left)
        return res