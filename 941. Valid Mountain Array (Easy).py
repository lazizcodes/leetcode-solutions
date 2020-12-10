class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False        
        
        if arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False        
        
        flag = False        
        
        for i in range(1, n - 1):
            
            if flag and arr[i] <= arr[i + 1]:
                return False
            
            if not flag and arr[i] >= arr[i + 1]:
                flag = True
                
        return True
        