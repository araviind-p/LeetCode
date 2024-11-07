/**
 * @param {string} sentence
 * @return {boolean}
 */
var isCircularSentence = function(sentence) {
    let words=sentence.split(" ")
    let s=words.length
    const one= words[0][0] === words[s-1][words[s-1].length-1]
    if(!one){
        return false
    }
    for(let i=0;i<words.length-1;i++){
        let first=words[i]
        let second=words[i+1]
        if(first[first.length-1] != second[0]){
            return false
        }
    }
    return true
};