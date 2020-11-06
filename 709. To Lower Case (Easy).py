class Solution:
    def toLowerCase(self, str: str) -> str:
        d = ord('A') - ord('a')
        def charLower(c):
            if ord('A') <= ord(c) <= ord('Z'):
                return chr(ord(c) - d)
            return c
        return ''.join(map(charLower, str))