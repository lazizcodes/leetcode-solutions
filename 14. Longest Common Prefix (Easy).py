class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        ans = ""
        s = min(strs, key=len)
        for i in range(len(s)):
            for word in strs:
                if s[i] != word[i]:
                    return ans
            ans += s[i]
        return ans