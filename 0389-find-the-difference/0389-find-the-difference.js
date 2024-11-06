/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    const sArr = s.split("")
    const tArr = t.split("")
    sArr.sort()
    tArr.sort()
    for(let i=0;i<t.length;i++){
        if(i==t.length-1){
            return tArr[tArr.length-1]
        }
        if(sArr[i] != tArr[i]) return tArr[i]
    }
};