class Solution:
    def intervalIntersection(self, A, B):
        if not A and not B:
            return []
        intA, intB = 0, 0
        intersections = []
        while intA < len(A) and intB < len(B):
            low = max(A[intA][0], B[intB][0])
            high = min(A[intA][1], B[intB][1])
            if low <= high: 
                intersections.append([low, high])
            if high == A[intA][1]: 
                intA += 1
            else: 
                intB += 1
        return intersections