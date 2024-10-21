/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function (arr) {
    const sortedUniqueArr = [...new Set(arr)].sort((a, b) => a - b);
    const rankMap = {};

    for (let i = 0; i < sortedUniqueArr.length; i++) {
        rankMap[sortedUniqueArr[i]] = i + 1;
    }

    return arr.map(num => rankMap[num]);
};
