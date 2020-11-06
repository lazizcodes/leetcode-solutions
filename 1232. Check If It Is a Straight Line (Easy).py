class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) == 1:
            return True
        x0, x1 = coordinates[0][0], coordinates[1][0]
        y0, y1 = coordinates[0][1], coordinates[1][1]
        for x, y in coordinates[2:]:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True