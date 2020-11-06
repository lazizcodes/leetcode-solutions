class Solution:
    def reconstructQueue(self, ppl: List[List[int]]) -> List[List[int]]:        
        ppl = sorted(ppl, key=lambda a: (-a[0],a[1]))        
        res = []        
        for each in ppl:
            res.insert(each[1], each)
            
        return res