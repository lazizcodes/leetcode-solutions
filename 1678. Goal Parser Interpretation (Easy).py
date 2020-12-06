# Solution 1

class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
                i += 1
            elif command[i] == '(':
                if command[i + 1] == ')':
                    res += 'o'
                    i += 2
                elif command[i + 1] == 'a':
                    res += 'al'
                    i += 4
        return res

# Solution 2

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')
            