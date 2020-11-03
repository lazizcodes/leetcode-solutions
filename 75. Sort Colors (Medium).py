from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
      cnt = Counter(nums)
      for i in range(len(nums)):
        if i in range(cnt[0]):
          nums[i] = 0
        elif i in range(cnt[0], cnt[0] + cnt[1]):
          nums[i] = 1
        elif i in range(cnt[0] + cnt[1], cnt[0] + cnt[1] + cnt[2]):
          nums[i] = 2
      
        
        
        