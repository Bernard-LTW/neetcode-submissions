class Solution:
    def countSubstrings(self, s: str) -> int:
        out = 0

        for i in range(len(s)):

            #odd length
            l = i
            r = i

            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1

            
            #even length
            l = i
            r = i + 1

            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1

        return out
        