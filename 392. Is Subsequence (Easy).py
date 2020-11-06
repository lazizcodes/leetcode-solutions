class Solution:
    def isSubsequence(self, s: string, t: string) -> bool:
        iterator = iter(t)
        return all(i in iterator for i in s)