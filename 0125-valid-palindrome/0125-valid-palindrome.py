class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        if len(s) == 1 or len(s) == 0:
            return True
        string=""
        for i in range(len(s)):
            if s[i] in alphabets:
                string+=s[i].lower()
        reverse=""
        for i in range(len(s)-1,-1,-1):
            if s[i] in alphabets:
                reverse+=s[i].lower()
        if string == reverse:
            return True
        else:
            return False
        