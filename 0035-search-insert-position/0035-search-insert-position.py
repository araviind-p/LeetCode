from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Check if target is in the list
        if target in nums:
            return nums.index(target)
        
        # If target is not in the list, find the correct insertion position
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        # If target is greater than all elements, it should be inserted at the end
        return len(nums)
