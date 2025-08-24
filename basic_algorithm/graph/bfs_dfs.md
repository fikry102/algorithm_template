# 深度优先搜索，广度优先搜索

### 深度优先搜索模板

- 先序，递归

```Python
def DFS(x):
    visit(x)
    for n in neighbor(x):
        if not visited(n):
            DFS(n)
    return
```

- 先序，迭代，出栈时访问

```Python
def DFS(x):
    dfs = [x] # implement by a stack
    while dfs:
        v = dfs.pop()
        if not visited(v):
            visit(v)
            for n in neighbor(v):
                if not visited(n):
                    dfs.append(n)
    return
```

- 后序，递归

```Python
def DFS(x): # used when need to aggregate results from children
    discovering(x)
    for n in neighbor(x):
        if not discovering(n) and not visited(n):
            DFS(n)
    visit(x)
    return
```

### 广度优先搜索模板

相对于 dfs 可能收敛更慢，但是可以用来找不带权的最短路径

- 以结点为单位搜索

```Python
def BFS(x):
    visit(x)
    bfs = collections.deque([x])
    while bfs:
        v = bfs.popleft()
        for n in neighbor(v):
            if not visited(n):
                visit(n)
                bfs.append(n)
    return
```

- 以层为单位搜索，典型应用是找不带权的最短路径

```Python
def BFS(x):
    visit(x)
    bfs = collections.deque([x])
    while bfs:
        num_level = len(bfs)
        for _ in range(num_level)
            v = bfs.popleft()
            for n in neighbor(v):
                if not visited(v):
                    visit(n)
                    bfs.append(n)
    return
```

## 例题

### [walls-and-gates](https://leetcode-cn.com/problems/walls-and-gates/)

> 给定一个二维矩阵，矩阵中元素 -1 表示墙或是障碍物，0 表示一扇门，INF (2147483647) 表示一个空的房间。你要给每个空房间位上填上该房间到最近门的距离，如果无法到达门，则填 INF 即可。

- 思路：典型的多源最短路径问题，将所有源作为 BFS 的第一层即可

```Python
inf = 2147483647

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        if not rooms or not rooms[0]:
            return
        
        M, N = len(rooms), len(rooms[0])
        
        bfs = collections.deque([])
        
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    bfs.append((i, j))
        
        dist = 1
        while bfs:
            num_level = len(bfs)
            for _ in range(num_level):
                r, c = bfs.popleft()
                
                if r - 1 >= 0 and rooms[r - 1][c] == inf:
                    rooms[r - 1][c] = dist
                    bfs.append((r - 1, c))
                    
                if r + 1 < M and rooms[r + 1][c] == inf:
                    rooms[r + 1][c] = dist
                    bfs.append((r + 1, c))
                    
                if c - 1 >= 0 and rooms[r][c - 1] == inf:
                    rooms[r][c - 1] = dist
                    bfs.append((r, c - 1))
                    
                if c + 1 < N and rooms[r][c + 1] == inf:
                    rooms[r][c + 1] = dist
                    bfs.append((r, c + 1))
            
            dist += 1
        
        return
```

### [shortest-bridge](https://leetcode-cn.com/problems/shortest-bridge/)

> 在给定的 01 矩阵 A 中，存在两座岛 (岛是由四面相连的 1 形成的一个连通分量)。现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。返回必须翻转的 0 的最小数目。
>

- 思路：DFS 遍历连通分量找边界，从边界开始 BFS找最短路径

```Python
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        M, N = len(A), len(A[0])
        neighors = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        dfs = []
        bfs = collections.deque([])

        for i in range(M):
            for j in range(N):
                if A[i][j] == 1: # start from a 1
                    dfs.append((i, j))
                    break
            if dfs:
                break
                    
        while dfs:
            r, c = dfs.pop()
            if A[r][c] == 1:
                A[r][c] = -1

                for dr, dc in neighors:
                    nr, nc = r + dr, c + dc
                    if 0<= nr < M and 0 <= nc < N:
                        if A[nr][nc] == 0: # meet and edge
                            A[nr][nc] = -2
                            bfs.append((nr, nc))
                        elif A[nr][nc] == 1:
                            dfs.append((nr, nc))

        flip = 1
        while bfs:
            num_level = len(bfs)
            for _ in range(num_level):
                r, c = bfs.popleft()
                
                for dr, dc in neighors:
                    nr, nc = r + dr, c + dc
                    if 0<= nr < M and 0 <= nc < N:
                        if A[nr][nc] == 0:
                            A[nr][nc] = -2
                            bfs.append((nr, nc))
                        elif A[nr][nc] == 1:
                            return flip
            flip += 1
```

### [sliding-puzzle](https://leetcode-cn.com/problems/sliding-puzzle)

```Python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        next_move = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        start = tuple(itertools.chain(*board))
        target = (1, 2, 3, 4, 5, 0)
        
        if start == target:
            return 0
        
        SPT = set([start])
        bfs = collections.deque([(start, start.index(0))])
        
        step = 1
        while bfs:
            num_level = len(bfs)
            for _ in range(num_level):
                state, idx0 = bfs.popleft()
            
                for next_step in next_move[idx0]:
                    next_state = list(state)
                    next_state[idx0], next_state[next_step] = next_state[next_step], next_state[idx0]
                    next_state = tuple(next_state)
                    
                    if next_state == target:
                        return step
                    
                    if next_state not in SPT:
                        SPT.add(next_state)
                        bfs.append((next_state, next_step))
            step += 1
        return -1
```

