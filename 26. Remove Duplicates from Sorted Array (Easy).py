class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        el = None
        idx = 0
        for i in range(len(nums)):
            if el != nums[i]:
                el = nums[i]
                nums[idx] = el
                idx += 1
        return idx