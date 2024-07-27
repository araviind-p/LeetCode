class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if (num % 3) != 0:
                if ((num +1) % 3 ==0 or (num -1) % 3 ==0):
                    count+=1
                elif ((num +2) % 3 ==0 or (num -2) % 3 ==0):
                    count+=2
        return count

        