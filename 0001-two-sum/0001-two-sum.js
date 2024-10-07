/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
   const numsMap=new Map()
   for(let i=0;i<nums.length;i++){
    const remaining=target-nums[i]
    if(numsMap.has(remaining)){
        return [numsMap.get(remaining),i]
    }
    numsMap.set(nums[i],i)
   }
};