class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        if len(points) == 1:
            return 1
        n = len(points)
        points.sort(key = lambda x: x[0])
        
        i = 0
        while i < n - 1:
            if points[i][1] >= points[i + 1][0]:
                points[i][1] = min(points[i][1], points[i + 1][1])
                points[i][0] = max(points[i][1], points[i + 1][0])
                points.pop(i + 1)
                n -= 1
            else:
                i += 1
        return n
            