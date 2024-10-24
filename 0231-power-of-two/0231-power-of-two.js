/**
 * @param {number} n
 * @return {boolean}
 */

var isPowerOfTwo = function (n) {
    let x = 0;

    while (Math.pow(2, x) <= n) {
        if (Math.pow(2, x) === n) {
            return true;
        }
        x++;
    }
    return false;
};
