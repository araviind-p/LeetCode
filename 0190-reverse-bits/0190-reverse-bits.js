/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let binary = n.toString(2).padStart(32, '0');
    
    let reversedBinary = binary.split("").reverse().join("");
    
    let reversedNumber = parseInt(reversedBinary, 2);
    
    return reversedNumber >>> 0;
};
