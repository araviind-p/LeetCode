/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if(num.toString().length==1){
        return num
    }
    while(num.toString().length!=1){
        let nums=num.toString().split("")
        let res=0
        for(let i=0;i<nums.length;i++){
            res+=parseInt(nums[i])
        }
        num=res
    }
    return num
};