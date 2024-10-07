/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    stringLen=s.length
    // t=s.split("")
    while(s.includes("AB") || s.includes("CD")){
        if(s.includes("AB")){
            s=s.replace("AB","")
        }else{
            s=s.replace("CD","")
        }
        stringLen-=2
    }
    return stringLen
};