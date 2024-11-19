class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        i = 0
        while i in nums:
            nums.remove(i)
            count = count + 1
        for i in range(count):
            nums.append(0)
        return nums
        