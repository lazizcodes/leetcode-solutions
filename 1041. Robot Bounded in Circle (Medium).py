class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if instructions == '':
            return True
        n = len(instructions)
        x = y = 0
        d = 0
        i = 0
        while True:
            i += 1
            for l in instructions:
                if l == 'R': d += 1
                if l == 'L': d -= 1
                if l == 'G':   
                    if d % 4 == 0: y += 1
                    if d % 4 == 1: x += 1
                    if d % 4 == 2: y -= 1
                    if d % 4 == 3: x -= 1
            if i >= n and (x == 0 and y == 0):
                return True
            if i >= n and d == 0:
                return False
            
