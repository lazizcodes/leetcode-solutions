class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:        
        mini = len(nums) + 1
        Sum = j = 0
        for i, val in enumerate(nums):
            Sum += val
            while Sum >= s:
                mini = min(mini, i - j + 1)
                Sum -= nums[j]
                j += 1
                
        if mini <= len(nums):
            return mini
        return 0
                
        
        
        
    
    
                   
            
            
        
        