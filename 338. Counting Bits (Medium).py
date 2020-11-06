from collections import Counter
class Solution:
    def countBits(self, num: int) -> List[int]:
        return [Counter(bin(i))['1'] for i in range(num + 1)]
    
    