class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        if n == 2:
            return 1
        
        #-------------------------------
        
        def countPrimes(m):
            
            prms = [0,0] + [True] * (m - 2)
            
            for i in range(2, m):
                if prms[i] == True:
                    for j in range(i * i, m, i):
                        prms[j] = False
            
            return sum(prms)
        
        #-------------------------------
        
        primes = countPrimes(n + 1)
        return (factorial(primes) * factorial(n - primes)) % (10**9 + 7)
                    
            