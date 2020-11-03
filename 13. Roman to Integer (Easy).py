class Solution:
    def romanToInt(self, s):
        
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000            
        }
        
        res = 0
        i = 0
        while i < len(s): 
            
            x1 = d[s[i]]  
            
            if i + 1 < len(s):                
                x2 = d[s[i + 1]]                
                if x1 >= x2:                    
                    res += x1 
                    i += 1
                else:                    
                    res += x2 - x1
                    i += 2 
                    
            else:                
                res += x1
                i += 1
        return res