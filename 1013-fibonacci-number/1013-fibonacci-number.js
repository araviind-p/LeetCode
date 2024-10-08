/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    fibArr = [0, 1]
    if (n < 2) {
        return fibArr[n]
    }
    for (let i = 2; i <= n; i++) {
        fibArr.push(fibArr[i-1] + fibArr[i - 2])
        console.log('fibArr: ', fibArr);
    }
    return fibArr[n]
};
