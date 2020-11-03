class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (s[i : j] in wordDict) and (i == 0 or dp[i - 1]):
                    dp[j - 1] = True
        return dp[n - 1]