class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = nums.sort()
        return nums[len(nums)//2]