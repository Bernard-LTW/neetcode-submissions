class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for i in s:
            if i in s_count.keys():
                s_count[i] = s_count.get(i)+1
            else:
                s_count[i] = 1
        t_count = {}
        for j in t:
            if j in t_count.keys():
                t_count[j] = t_count.get(j)+1
            else:
                t_count[j] = 1  
        return s_count==t_count
        