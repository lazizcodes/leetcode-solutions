class Solution:
    def merge(self, ints: List[List[int]]) -> List[List[int]]:
        if not ints or len(ints) == 1:
            return ints
        
        ints.sort(key = lambda x: x[0])
        n = len(ints)
        
        i = 0
        while i < n - 1:
            if ints[i + 1][0] <= ints[i][1]:
                ints[i][1] = max(ints[i][1], ints[i + 1][1])
                ints.pop(i + 1)
                n -= 1
            else: i += 1
        return ints
                
            
            