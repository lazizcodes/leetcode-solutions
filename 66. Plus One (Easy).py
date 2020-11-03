class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:   
        s = ''    
        for item in digits:
            s = s + str(item)
        return [int(x) for x in str(int(s)+1)]