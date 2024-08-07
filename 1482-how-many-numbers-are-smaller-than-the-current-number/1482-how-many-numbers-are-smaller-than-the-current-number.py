class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            small=0
            for i in range(len(nums)):
                if nums[i] < num:
                    small+=1
            ans.append(small)
        return ans