class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:return False
        stack = []
        reference = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in reference:
                if stack and stack[-1] == reference[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
        
        