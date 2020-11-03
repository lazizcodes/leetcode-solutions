class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [i for i in s.lower() if i.isalnum()]
        return s_list == s_list[::-1]