class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if i < j and nums[i] == nums[j]:
                    res.append((i,j))
        return len(res)