class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a = []
        for i in nums:
            if i < 0:
                a.append(0)
            elif i > 0:
                a.append(1)
        return max(a.count(0),a.count(1))