class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = [i for i in range(1, 10)]
        
        if N == 1: 
            return list(range(10))
        
        for i in range(N - 1):
            for j in range(len(res)):
                num = res[0]
                res.remove(res[0])
                r = num % 10
                if r - K >= 0:   
                    res.append(10 * num + r - K)
                if r + K <= 9:   
                    res.append(10 * num + r + K)
        return set(res)
    