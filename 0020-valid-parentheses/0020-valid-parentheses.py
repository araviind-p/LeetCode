class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets={")":"(","]":"[","}":"{"}
        stack=[]
        for char in s:
            if char in matching_brackets.values():
                stack.append(char)
            elif char in matching_brackets.keys():
                if stack == [] or matching_brackets[char] != stack.pop():
                    return False
            else:
                continue
        return stack ==[]