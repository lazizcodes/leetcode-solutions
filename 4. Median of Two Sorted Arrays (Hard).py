from bisect import insort
from numpy import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            insort(nums1, i)
        return median(nums1)