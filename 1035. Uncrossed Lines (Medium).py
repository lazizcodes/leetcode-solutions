class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        '''
        Example 2:
        2  5  1  2  5
           |    \   | 
        10 5  2  1  5  2
        '''
        
        '''
        Example 3:
        1  3  7  1  7  5
        |         \
        1  9  2  5  1
        '''
        A = [0] + A
        B = [0] + B
        rw = len(A)
        cl = len(B)
        dp = [([0] * cl) for r in range(1, rw)]

        for i in range(1, rw):
            for j in range(1, cl):            
                    if A[i] == B[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
