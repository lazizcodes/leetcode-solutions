class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            memo = set()
            for l in A:
                if l in memo:
                    return True
                memo.add(l)
            return False
        else:
            p = []
            for a, b in zip(A, B):
                if a != b:
                    p.append((a, b))
                if len(p) > 2:
                    return False
            return len(p) == 2 and p[0] == p[1][::-1]
            