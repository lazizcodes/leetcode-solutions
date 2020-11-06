# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    
    def __init__(self):
        self.x = 0
        
    
    def rand10(self):
        x = (7 * self.x + rand7()) % 10 + 1
        self.x = x
        return x
        