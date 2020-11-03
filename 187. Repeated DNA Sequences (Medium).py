class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []
        
        d = {}
        repeated = []
        
        for i in range(n - 9):
            key = s[i : i + 10]
            if key in d:
                d[key] += 1
                if d[key] == 2:
                    repeated.append(key)
            else:
                d[key] = 1
        
        return repeated