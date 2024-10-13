/**
 * @param {string} sequence
 * @param {string} word
 * @return {number}
 */
var maxRepeating = function (sequence, word) {
    if (!sequence.includes(word)) {
        return 0;
    }
    let curr = word
    let count = 0
    while (sequence.includes(curr)) {
        count++
        curr += word
    }
    return count
};