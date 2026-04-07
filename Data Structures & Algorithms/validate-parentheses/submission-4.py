class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = {"(":")","[":"]","{":"}"}
        
        for char in s:
            if char in reference.keys():
                stack.append(char)
            else: 
                if not stack or reference[stack.pop()] != char:
                    return False
        
        return not stack