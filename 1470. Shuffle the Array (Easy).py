class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        new_nums = []
        for i, j in zip(x,y):
            new_nums += [i,j]
        return new_nums
                