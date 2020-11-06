class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ls = [s.lower() + s.upper() if s.isalpha() else s for s in S ]
        return [''.join(s) for s in product(*ls)]