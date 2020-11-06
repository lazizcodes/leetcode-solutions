class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        memo = set()
        k_diff = set()
        
        for n in nums:
            if n + k in memo:
                k_diff.add(n + k)
            if n - k in memo:
                k_diff.add(n)
            memo.add(n)
        
        return len(k_diff)
        