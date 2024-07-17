class Solution:
    def left_sum(i):
        left_sum = 0
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            if left == right:
                return i
        if sum(nums[1:]) == 0:
            return 0
        elif  sum(nums[:len(nums)-1]) == 0:
            return len(nums)-1
        else:
            return -1