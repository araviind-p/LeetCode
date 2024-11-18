/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let binaryNum=n.toString(2)
    count=0
    for(let i=0;i<binaryNum.length;i++){
        if(parseInt(binaryNum[i])===1){
            count++
        }
    }
    return count
};