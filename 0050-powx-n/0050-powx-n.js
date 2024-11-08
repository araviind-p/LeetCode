/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n === 0) return 1;
    if (x === 1) return 1;
    if (x === -1) return n % 2 === 0 ? 1 : -1;
    
    let result = 1;
    let absN = Math.abs(n);
    
    while (absN > 0) {
        if (absN % 2 === 1) {
            result *= x;
        }
        x *= x;
        absN = Math.floor(absN / 2);
    }
    
    return n < 0 ? 1 / result : result;
};
