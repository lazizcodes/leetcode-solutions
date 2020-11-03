class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            if min(nums) - target > 0:
                return 0
            elif target - max(nums) > 0:
                return len(nums)
            else:
                for i in range(len(nums) - 1):
                    if nums[i] < target and target < nums[i + 1]:
                        return i + 1
        return -1