class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for k,v in edges:
            adj[k].append(v)
            adj[v].append(k)
        
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        
        res = 0
        for node in range(n):
            if visited[node] == False:
                visited[node] = True
                dfs(node)
                res += 1
        return res