class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=""
        first=""
        second=""
        chars = [char for char in word]
        if ch in chars:
            index = chars.index(ch)
            for i in range(index+1):
                first+=chars[i]
            reverseFirst = first[::-1]
            for i in range(index+1,len(word)):
                second+=chars[i]
            return reverseFirst+second
        else:
            return word
