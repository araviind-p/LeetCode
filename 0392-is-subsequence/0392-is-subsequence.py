class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        s_index = 0
        t_index = 0
        
        while t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                if s_index == len(s):
                    return True
            t_index += 1
        
        return s_index == len(s)
