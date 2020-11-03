class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:
            return False
        
        if target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return False
        
        first_col = []
        for i in range(len(matrix)):
            first_col.append(matrix[i][0])
            
        row = self.bSearch(first_col, target)[0]
        return self.bSearch(matrix[row], target)[1]
    
        
    def bSearch(self, arr, tar):
        n = len(arr)
        (left, right) = (0, n - 1)
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == tar:
                return [mid, True]
            if arr[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return [left - 1, False]