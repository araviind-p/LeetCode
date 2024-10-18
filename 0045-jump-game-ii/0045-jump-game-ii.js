/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    res=0
    let l=0,r=0
    while (r<nums.length-1){
        farthest=0
        for(let i=l;i<=r;i++){
            farthest=Math.max(farthest,i+nums[i])
        }
        l=r+1
        r=farthest
        res+=1
    }
    return res
};