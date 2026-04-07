class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):

            #overflow protection
            if i >= len(s):
                return 1
            #first char is zero
            if s[i] == '0':
                return 0

            output = dfs(i+1)
            
            #valid 2 char
            if i+1 < len(s) and int(s[i:i+2])<=26:
                output += dfs(i+2)
            return output
        return dfs(0)
        