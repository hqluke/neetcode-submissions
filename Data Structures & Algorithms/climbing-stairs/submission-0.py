class Solution:
    def climbStairs(self, n: int) -> int:
        # cache for visited items
        cache = [-1] * n

        def dfs(i):
            # returns 1 if i == n and 0 if i > n (true and false converts to 1 and 0)
            if i >= n:
                return i == n
            # use cached number if it exists
            if cache[i] != -1:
                return cache[i]
            # recurse
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
                    
        return dfs(0)
