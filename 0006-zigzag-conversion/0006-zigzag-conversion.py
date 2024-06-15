class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res=""
        dict = {row:"" for row in range(1,numRows+1)}
        curr_dir=1
        row=1
        for i in range(len(s)):
            dict[row]+=s[i]
            if row == 1:
                curr_dir=1
            elif row==numRows:
                curr_dir=-1

            row+=curr_dir
        for i in dict.values():
            res+=i
        return res


        