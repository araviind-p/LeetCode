class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        vow=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                vow.append(s[i])
                s[i]="_"
        index=len(vow)-1
        for i in range(len(s)):
            if s[i] == "_":
                s[i]=vow[index]
                index-=1
        return "".join(s)

        