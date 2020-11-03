class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        openb = ['{', '[', '(']
        closedb = ['}', ']', ')']
        for brace in s:
            if brace in openb:
                    stack.append(brace)
            else:
                if len(stack) == 0:
                    return False
                elif openb[closedb.index(brace)] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
