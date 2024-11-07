/**
 * @param {string} s
 * @return {string}
 */
// var makeFancyString = function (s) {
//     let one = 0
//     let two = 1
//     let three = 2
//     if (s.length < 3) {
//         return s
//     }
//     while (three < s.length) {
//         if (s[one] == s[two] && s[two] == s[three]) {
//             s = s.replace(s[one], "")
//             one = two
//             two = three
//             three++
//         } else {

//             one++
//             two++
//             three++
//         }

//     }
//     return s
// };


var makeFancyString = function (s) {
    let res = s.slice(0, 2); 

    for (let i = 2; i < s.length; i++) {
        if (!(s[i] === s[i - 1] && s[i] === s[i - 2])) {
            res += s[i];
        }
    }

    return res;
};
