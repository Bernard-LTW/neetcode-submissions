class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(s):
            if len(s) == 0:
                return True

            if s in memo:
                return memo[s]

            for word in wordDict:
                if s[0:len(word)] == word:
                    if dfs(s[len(word):]):
                        memo[s] = True
                        return True
            
            memo[s] = False
            return False
        
        return dfs(s)
        