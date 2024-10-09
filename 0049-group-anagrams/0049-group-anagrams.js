/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map=new Map()
    for(let i=0;i<strs.length;i++){
        let curr=strs[i].split("").sort().join()
        if(map.has(curr)){
            map.get(curr).push(strs[i])
        }else{
            map.set(curr,[strs[i]])
        }
    }
    return Array.from(map.values())
};