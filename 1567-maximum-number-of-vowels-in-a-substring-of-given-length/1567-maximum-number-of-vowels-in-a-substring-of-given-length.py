class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l,r =0,0
        max_count,count=0,0
        for r in range(len(s)):
            count += 1 if s[r] in vowels else 0
            if r-l+1 > k:
                count -= 1 if s[l] in vowels  else 0
                l += 1
            max_count = max(count,max_count)
        return max_count