class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            res.append(num)
        ans=nums+res
        return ans