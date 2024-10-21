/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function (arr) {
    const sortedUniqueArr = [...new Set(arr)].sort((a, b) => a - b); // Get sorted unique elements
    const rankMap = {}; // To store the rank of each element

    // Assign rank to each unique element
    for (let i = 0; i < sortedUniqueArr.length; i++) {
        rankMap[sortedUniqueArr[i]] = i + 1;
    }

    // Transform the original array into its rank representation
    return arr.map(num => rankMap[num]);
};
