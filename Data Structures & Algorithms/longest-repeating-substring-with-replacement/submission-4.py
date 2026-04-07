class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxlen = 0
        count = {}

        while l <= r and r < len(s):

            count[s[r]] = count.get(s[r],0)+1

            most_occur = 0
            for i in count.values():
                if i > most_occur:
                    most_occur = i
            
            if (r-l+1)-most_occur <= k:
                maxlen=max(maxlen,(r-l+1))
            else:
                count[s[l]] = count[s[l]] -1
                l += 1

            r+=1
        return maxlen
            

                




        