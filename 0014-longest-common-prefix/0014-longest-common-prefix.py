class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        s=sorted(strs)
        a=s[0]
        b=s[-1]
        for i in range(min(len(a),len(b))):
            if a[i] != b[i]:
                return res
            res+=a[i]
        return res
