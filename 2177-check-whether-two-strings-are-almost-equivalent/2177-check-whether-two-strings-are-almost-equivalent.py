class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        check = set(word1 + word2)

        for i in check:
            res = abs(word1.count(i) - word2.count(i)) >= 4
            if res:
                return False
        return True