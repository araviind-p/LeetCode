/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    let monotoneIncreasing=0
    let monotoneDecreasing=0
    for(let i=1;i<nums.length;i++){
        if(nums[i] >= nums[i-1]){
            monotoneIncreasing+=1
        }
    }
    for(let i=1;i<nums.length;i++){
        if(nums[i] <= nums[i-1]){
            monotoneDecreasing+=1
        }
    }
    if(monotoneIncreasing==nums.length-1 || monotoneDecreasing==nums.length-1){
        return true
    }else{
        return false
    }
};