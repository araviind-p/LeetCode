/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let set=new Set()
    let left=0,right=0,max_len=0;
    while(right<s.length){
        let letter=s[right]
        if(!set.has(letter)){
            set.add(letter);
            max_len=Math.max(max_len,set.size)
            right++;
        }else{
            set.delete(s[left])
            left++
        }
    }
    return max_len
};