class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for word in sentence.split():
            if word.startswith(searchWord):
                return sentence.split().index(word) + 1
        return -1