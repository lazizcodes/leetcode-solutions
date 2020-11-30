# 1
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False
        
        table = {}
        for i in range(97, 123):
            table[chr(i)] = 0
        
        for i in range(len(s)):
            table[s[i]] += 1
            
        for i in range(len(t)):
            table[t[i]] -= 1
            if table[t[i]] < 0:
                return False
            
        return True

# 2
class Solution2:
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
            
