class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [0,0] + [1 for i in range(2, n)]

        for i in range(2, n):
            if primes[i] == 1:
                for j in range(i * i, n, i):
                    primes[j] = 0

        return sum(primes)