class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(set(A)) == 1:
            return True
        i, sz = 1, len(A)
        while A[i - 1] == A[i] and i < sz:
            i += 1
        if A[i - 1] < A[i]:
            for j in range(i + 1, sz):
                if A[j - 1] > A[j]:
                    return False
        elif A[i - 1] > A[i]:
            for j in range(i + 1, sz):
                if A[j - 1] < A[j]:
                    return False
        return True
        
        