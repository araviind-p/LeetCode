import java.util.List;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        if (nums.length == 1) {
            return nums[0];
        } else if (nums.length == k) {
            int total = 0;
            for (int num : nums) {
                total += num;
            }
            return (double) total / k;
        } else {
            int currentSum = 0;
            for (int i = 0; i < k; i++) {
                currentSum += nums[i];
            }
            int maxSum = currentSum;
            
            for (int i = k; i < nums.length; i++) {
                currentSum += nums[i] - nums[i - k];
                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
            }
            return (double) maxSum / k;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 12, -5, -6, 50, 3};
        int k = 4;
        System.out.println(solution.findMaxAverage(nums, k));  // Output: 12.75
    }
}
