class Solution:    
    def combinationSum(self, cands, target):
        
        def solve(target, curr, k): 
            if target < 0 or k >= len(cands):
                return
            if target == 0:
                self.comb.append(curr)
            for i in range(k, len(cands)):
                solve(target - cands[i], curr + [cands[i]], i)
        
        self.comb = []
        solve(target, [], 0)   
        return self.comb