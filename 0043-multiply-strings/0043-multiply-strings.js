/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    let a=BigInt(num1)
    let b=BigInt(num2)
    let res=a*b
    let ans=res.toString()
    return ans
};