class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:        
        return [candies[i] + extraCandies >= max(candies) for i in range(len(candies))]       