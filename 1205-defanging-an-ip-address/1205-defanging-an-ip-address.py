class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=[]
        for num in address:
            if num == ".":
                res.append("[.]")
            else:
                res.append(num)
        org_res=""
        for item in res:
            org_res+=item
        return org_res
