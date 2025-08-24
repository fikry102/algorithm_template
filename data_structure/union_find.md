# 并查集

用于处理不相交集合 (disjoint sets) 合并及查找的问题，典型应用有连通分量检测，环路检测等。原理和复杂度分析等可以参考[维基百科](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)。

### [redundant-connection](https://leetcode-cn.com/problems/redundant-connection/)

```Python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)
        
        def find(x):
            if parent[parent[x]] != parent[x]:
                parent[x] = find(parent[x]) # path compression
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            # union by rank
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
```

### [accounts-merge](https://leetcode-cn.com/problems/accounts-merge/)

```Python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = []
        rank = []
        
        def find(x):
            if parent[parent[x]] != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1
            return
        
        email2name = {}
        email2idx = {}
        i = 0
        for acc in accounts:
            for email in acc[1:]:
                email2name[email] = acc[0]
                if email not in email2idx:
                    parent.append(i)
                    rank.append(1)
                    email2idx[email] = i
                    i += 1
                union(email2idx[acc[1]], email2idx[email])
        
        result = collections.defaultdict(list)
        for email in email2name:
            result[find(email2idx[email])].append(email)
        
        return [[email2name[s[0]]] + sorted(s) for s in result.values()]
```

### [longest-consecutive-sequence](https://leetcode-cn.com/problems/longest-consecutive-sequence/)

```Python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        parent = {num: num for num in nums}
        length = {num: 1 for num in nums}
        
        def find(x):
            if parent[parent[x]] != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # union by size
            if length[px] > length[py]:
                parent[py] = px
                length[px] += length[py]
            else:
                parent[px] = py
                length[py] += length[px]
            return
        
        max_length = 0
        for num in nums:
            if num + 1 in parent:
                union(num + 1, num)
            if num - 1 in parent:
                union(num - 1, num)
            
            max_length = max(max_length, length[parent[num]])
        
        return max_length
```

### Kruskal's algorithm

### [minimum-risk-path](https://www.lintcode.com/problem/minimum-risk-path/description)

> 地图上有 m 条无向边，每条边 (x, y, w) 表示位置 m 到位置 y 的权值为 w。从位置 0 到 位置 n 可能有多条路径。我们定义一条路径的危险值为这条路径中所有的边的最大权值。请问从位置 0 到 位置 n 所有路径中最小的危险值为多少？

- 最小危险值为最小生成树中 0 到 n 路径上的最大边权。

```Python
# Kruskal's algorithm
class Solution:
    def getMinRiskValue(self, N, M, X, Y, W):
        
        # Kruskal's algorithm with union-find
        parent = list(range(N + 1))
        rank = [1] * (N + 1)
        
        def find(x):
            if parent[parent[x]] != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1
            
            return True
        
        edges = sorted(zip(W, X, Y))
        
        for w, x, y in edges:
            if union(x, y) and find(0) == find(N): # early return without constructing MST
                return w
```