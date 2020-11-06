class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                if stack[-2] < abs(stack[-1]):
                    stack.pop(-2)
                elif stack[-2] > abs(stack[-1]):
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()
                    break
        return stack