class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        max_sum=0
        ans.append(0)
        curr_sum=0
        for r in range(len(gain)):
            curr_sum += gain[r]
            ans.append(curr_sum)
        return max(ans)