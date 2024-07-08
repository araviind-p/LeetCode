class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        ans=[]
        def listt_to_stringg(lis):
            ans_string=""
            for char in lis:
                ans_string+=char
            return ans_string
        while len(word1) != 0 or len(word2) != 0:
            if len(word1) == 0:
                ans=ans+word2
                return listt_to_stringg(ans)
            elif len(word2) == 0:                
                ans=ans+word1
                return listt_to_stringg(ans)
            ans.append(word1[0])
            word1.remove(word1[0])
            ans.append(word2[0])
            word2.remove(word2[0])
        return listt_to_stringg(ans)
        
