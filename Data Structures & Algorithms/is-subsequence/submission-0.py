class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        y = 0
        while x < len(t) and y < len(s):
            if t[x] == s[y]:
                x += 1
                y += 1
            else:
                x += 1

        return y == len(s)