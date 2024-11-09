/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    let sArr=s.split("")
    const len=s.length

    for(let i=0;i<len;i++){
       
       sArr.push(sArr[0])
       sArr.shift(sArr[0])
       
        if(sArr.join("") == goal){
            return true
        }
         console.log(i+1,sArr)
    }
    return false
};