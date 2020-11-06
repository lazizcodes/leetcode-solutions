class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        mangle = (6 * minutes)
        
        hangle = (30 * hour) % 360 + 0.5 * minutes
        
        angle = abs(mangle - hangle)
        
        return min(angle, 360 - angle)
        