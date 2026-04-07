class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(a):
            if a in memo:
                return memo[a]
            minimum = amount + 1
            if a == 0:
                return 0
            if a < 0:
                return amount + 1

            for coin in coins:
                res = dfs(a-coin)
                if res != amount +1:
                    minimum = min(minimum, 1+res)
            memo[a] = minimum
            return minimum
            
        
        a = dfs(amount)
        if a != amount +1:
            return a
        else:
            return -1
        return a

            

        