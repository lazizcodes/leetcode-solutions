# O(1) extra space

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                duplicates.append(abs(n))
        return duplicates


# For a more general problem (with no bounds on elements)
# we use O(n) extra space

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = {}
        duplicates = []
        for i in nums:
            if i not in unique:
                unique[i] = 1
                continue
            duplicates.append(i)
        return duplicates