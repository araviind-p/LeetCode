class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) ==1:
            return nums[0]
        elif len(nums)==k:
            return sum(nums)/k
        else:
            current_sum=sum(nums[:k])
            max_sum=current_sum
            for i in range(k,len(nums)):
                current_sum+=nums[i]-nums[i-k]
                if current_sum>max_sum:
                    max_sum=current_sum
            return max_sum/k

