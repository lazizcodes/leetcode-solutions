class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        j = 0
        for l in pattern:
            if l not in d.keys() and words[j] not in d.values():
                d[l] = words[j]
            elif l in d.keys() and words[j] in d.values():
                if d[l] != words[j]:
                    return False
            else:
                return False
            j += 1
        return True
               