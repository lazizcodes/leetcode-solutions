class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {c: 0 for i, c in enumerate(s)}
        for i in range(len(s)):
            count[s[i]] += 1
        for c in count:
            if count[c] == 1:
                return s.find(c)
        return -1