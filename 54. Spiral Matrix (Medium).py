class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if (not matrix):
            return res
        d = 0
        (m, n) = (len(matrix), len(matrix[0]))
        (top, bottom, right, left) = (0, m - 1, n - 1, 0)
        while (top <= bottom and left <= right):
            
            if (d == 0):
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
                
            if (d == 1):
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right += -1
                
            if (d == 2):
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom += -1
                
            if (d == 3):
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
            d = (d + 1) % 4
            
        return res