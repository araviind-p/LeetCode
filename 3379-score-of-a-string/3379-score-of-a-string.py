class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        if len(s) <= 1:
            return score

        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))  # Use ord() for ASCII values
        return score