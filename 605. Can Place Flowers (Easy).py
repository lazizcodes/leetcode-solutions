# Explanation:
# To avoid the edgy cases, we add 1,0 and 0,1 to both ends of the flowerbed. 
# Then we calculate how many consecutive zeros appear between two ones. 
# If there are k of them, there will be [(k + 1) / 2] places available for planting, 
# where [x] stands for the floor function. 
# As soon as available places exceeds n we return true.

# RT ~ O(n) | Extra SC ~ O(1)


# The code:

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed[:] = [1, 0] + flowerbed + [0, 1]
        zeros = 0
        available = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if zeros > 0:
                    available += (zeros - 1) // 2
                    if available >= n:
                        return True
                zeros = 0
            else:
                zeros += 1
        return False