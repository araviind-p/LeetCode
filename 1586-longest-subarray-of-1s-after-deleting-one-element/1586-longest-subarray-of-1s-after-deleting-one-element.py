class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r=0,0
        num_zeros=0
        max_w=0
        for r in range(len(nums)):
            num_zeros += 1 if nums[r]  == 0 else 0
            while num_zeros > 1:
                num_zeros -= 1 if nums[l] == 0 else 0
                l+=1
            w=r-l
            max_w=max(w,max_w)
        return max_w

