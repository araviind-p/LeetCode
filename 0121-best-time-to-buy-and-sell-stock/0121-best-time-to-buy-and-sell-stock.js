/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // let globalProfit=0
    // for(let i=0;i<prices.length;i++){
    //     for(let j=i+1;j<prices.length;j++){
    //         currentprofit=prices[j]-prices[i]
    //         globalProfit=Math.max(globalProfit,currentprofit)
    //     }
    // }
    // return globalProfit
    let profit=0
    let minPrice=prices[0]
    for(let i=0;i<prices.length;i++){
        minPrice=Math.min(minPrice,prices[i])
        currProfit=prices[i]-minPrice
        profit=Math.max(currProfit,profit)
    }
    return profit
};