class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        else:
            n = len(needle)
            c = 0
            for i in range(len(haystack)):
                if needle == haystack[i:i + n]:
                    return i
            return -1   