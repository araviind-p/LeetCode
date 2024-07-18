class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        num1 = list(set(nums1))
        ans1 = []
        for i in range(len(num1)):
            0 if num1[i] in nums2 else ans1.append(num1[i])
        num2=list(set(nums2))
        ans2=[]
        for i in range(len(num2)):
            0 if num2[i] in nums1 else ans2.append(num2[i])
        res.append(ans1)
        res.append(ans2)
        return res
    