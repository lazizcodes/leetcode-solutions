class Solution:
    def maxPower(self, s: str) -> int:
        local_max = global_max = 1
        prev = '#'
        for char in s:
            
            if char == prev:
                local_max += 1
                global_max = max(global_max, local_max)
                
            else:
                local_max = 1
                prev = char