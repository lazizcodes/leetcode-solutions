class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0
        res = 0
        n = len(timeSeries)
        for i in range(1, n):
            if timeSeries[i] - timeSeries[i - 1] >= duration: 
                res += duration
            else: 
                res += timeSeries[i] - timeSeries[i - 1]
        return res + duration
                