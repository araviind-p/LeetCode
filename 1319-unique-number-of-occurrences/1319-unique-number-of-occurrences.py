class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set_arr = list(set(arr))
        count_nums=[]
        for num in set_arr:
            count_nums.append(arr.count(num))
        return len(count_nums) == len(set(count_nums))