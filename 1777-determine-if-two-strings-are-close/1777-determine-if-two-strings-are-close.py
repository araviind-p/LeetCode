class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        if sorted(c1.values())==sorted(c2.values()) and sorted(c1.keys())==sorted(c2.keys()):
            return True
        else:
            return False
        