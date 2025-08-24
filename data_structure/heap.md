# 优先级队列 (堆)

用到优先级队列 (priority queue) 或堆 (heap) 的题一般需要维护一个动态更新的池，元素会被频繁加入到池中或从池中被取走，每次取走的元素为池中优先级最高的元素 (可以简单理解为最大或者最小)。用堆来实现优先级队列是效率非常高的方法，加入或取出都只需要 O(log N) 的复杂度。

## Kth largest/smallest

找数据中第 K 个最大/最小数据是堆的一个典型应用。以找最大为例，遍历数据时，使用一个最小堆来维护当前最大的 K 个数据，堆顶数据为这 K 个数据中最小，即是你想要的第 k 个最大数据。每检查一个新数据，判断是否大于堆顶，若大于，说明堆顶数据小于了 K 个值，不是我们想找的第 K 个最大，则将新数据 push 进堆并 pop 掉堆顶，若小于则不操作，这样当遍历完全部数据后堆顶即为想要的结果。找最小时换成最大堆即可。

### [kth-largest-element-in-a-stream](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)

> 设计一个找到数据流中第K大元素的类。

```Python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.min_heap = []
        for num in nums:
            if len(self.min_heap) < self.K:
                heapq.heappush(self.min_heap, num)
            elif num > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.K:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]
```

### [kth-smallest-element-in-a-sorted-matrix](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)

> 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。

- 此题使用 heap 来做并不是最优做法，相当于 N 个 sorted list 里找第 k 个最小，列有序的条件没有充分利用，但是却是比较容易想且比较通用的做法。

```Python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        N = len(matrix)
        
        min_heap = []
        for i in range(min(k, N)): # 这里用了一点列有序的性质，第k个最小只可能在前k行中(k行以后的数至少大于了k个数)
            min_heap.append((matrix[i][0], i, 0))
        
        heapq.heapify(min_heap)
        
        while k > 0:
            num, r, c = heapq.heappop(min_heap)
            
            if c < N - 1:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            
            k -= 1
        
        return num
```

### [find-k-pairs-with-smallest-sums](https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/)

```Python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        m, n = len(nums1), len(nums2)
        result = []
        
        if m * n == 0:
            return result
        
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set()
        
        while min_heap and len(result) < k:
            _, i1, i2 = heapq.heappop(min_heap)
            result.append([nums1[i1], nums2[i2]])
            if i1 < m - 1 and (i1 + 1, i2) not in seen:
                heapq.heappush(min_heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
                seen.add((i1 + 1, i2))
            if i2 < n - 1 and (i1, i2 + 1) not in seen:
                heapq.heappush(min_heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                seen.add((i1, i2 + 1))
        
        return result
```

## Greedy + Heap

Heap 可以高效地取出或更新当前池中优先级最高的元素，因此适用于一些需要 greedy 算法的场景。

### [maximum-performance-of-a-team](https://leetcode-cn.com/problems/maximum-performance-of-a-team/)

> 公司有 n 个工程师，给两个数组 speed 和 efficiency，其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的团队的最大表现值。表现值的定义为：一个团队中所有工程师速度的和乘以他们效率值中的最小值。
>

- [See my review here.](https://leetcode.com/problems/maximum-performance-of-a-team/discuss/741822/Met-this-problem-in-my-interview!!!-(Python3-greedy-with-heap)) [或者这里(中文)](https://leetcode-cn.com/problems/maximum-performance-of-a-team/solution/greedy-with-min-heap-lai-zi-zhen-shi-mian-shi-de-j/)

```Python
# similar question: LC 857
class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        
        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        
        result, sum_speed = 0, 0
        min_heap = []
		
        for i, (s, e) in enumerate(people):
            if i < k:
                sum_speed += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_speed += s - heapq.heappushpop(min_heap, s)
            
            result = max(result, sum_speed * e)
        
        return result #% 1000000007
```

### [ipo](https://leetcode-cn.com/problems/ipo/)

- 贪心策略为每次做当前成本范围内利润最大的项目。

```Python
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        N = len(Profits)
        projects = sorted([(-Profits[i], Capital[i]) for i in range(N)], key=lambda x: x[1])
        
        projects.append((0, float('inf')))
        
        max_profit_heap = []
        
        for i in range(N + 1):
            while projects[i][1] > W and len(max_profit_heap) > 0 and k > 0:
                W -= heapq.heappop(max_profit_heap)
                k -= 1
            
            if projects[i][1] > W or k == 0:
                break
            
            heapq.heappush(max_profit_heap, projects[i][0])

        return W
```

### [meeting-rooms-ii](https://leetcode-cn.com/problems/meeting-rooms-ii/)

- 此题用 greedy + heap 解并不是很 intuitive，存在复杂度相同但更简单直观的做法。

```Python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 0: return 0
        
        intervals.sort(key=lambda item: item[0])
        end_times = [intervals[0][1]]
        
        for interval in intervals[1:]:
            if end_times[0] <= interval[0]:
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, interval[1])
        
        return len(end_times)
```

### [reorganize-string](https://leetcode-cn.com/problems/reorganize-string/)

> 给定一个字符串 S，检查是否能重新排布其中的字母，使得任意两相邻的字符不同。若可行，输出任意可行的结果。若不可行，返回空字符串。

- 贪心策略为每次取前两个最多数量的字母加入到结果。

```Python
class Solution:
    def reorganizeString(self, S: str) -> str:
        
        max_dup = (len(S) + 1) // 2
        counts = collections.Counter(S)
        
        heap = []
        for c, f in counts.items():
            if f > max_dup:
                return ''
            heap.append([-f, c])
        heapq.heapify(heap)
        
        result = []
        while len(heap) > 1:
            first = heapq.heappop(heap)
            result.append(first[1])
            first[0] += 1
            second = heapq.heappop(heap)
            result.append(second[1])
            second[0] += 1
            
            if first[0] < 0:
                heapq.heappush(heap, first)
            if second[0] < 0:
                heapq.heappush(heap, second)
        
        if len(heap) == 1:
            result.append(heap[0][1])
        
        return ''.join(result)
```

### Prim's Algorithm

实现上是 greedy + heap 的一个应用，用于构造图的最小生成树 (MST)。

### [minimum-risk-path](https://www.lintcode.com/problem/minimum-risk-path/description)

> 地图上有 m 条无向边，每条边 (x, y, w) 表示位置 m 到位置 y 的权值为 w。从位置 0 到 位置 n 可能有多条路径。我们定义一条路径的危险值为这条路径中所有的边的最大权值。请问从位置 0 到 位置 n 所有路径中最小的危险值为多少？

- 最小危险值为最小生成树中 0 到 n 路径上的最大边权。

```Python
class Solution:
    def getMinRiskValue(self, N, M, X, Y, W):
        
        # construct graph
        adj = collections.defaultdict(list)
        for i in range(M):
            adj[X[i]].append((Y[i], W[i]))
            adj[Y[i]].append((X[i], W[i]))
            
        # Prim's algorithm with min heap
        MST = collections.defaultdict(list)
        min_heap = [(w, 0, v) for v, w in adj[0]]
        heapq.heapify(min_heap)
        
        while N not in MST:
            w, p, v = heapq.heappop(min_heap)
            if v not in MST:
                MST[p].append((v, w))
                MST[v].append((p, w))
                for n, w in adj[v]:
                    if n not in MST:
                        heapq.heappush(min_heap, (w, v, n))
                
        # dfs to search route from 0 to n
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_w = dfs.pop()
            for n, w in MST[v]:
                cur_max_w = max(max_w, w)
                if n == N:
                    return cur_max_w
                if n != p:
                    dfs.append((n, v, cur_max_w))
```

### Dijkstra's Algorithm

实现上是 greedy + heap 的一个应用，用于求解图的单源最短路径相关的问题，生成的树为最短路径树 (SPT)。

### [network-delay-time](https://leetcode-cn.com/problems/network-delay-time/)

- 标准的单源最短路径问题，使用朴素的的 Dijikstra 算法即可，可以当成模板使用。

```Python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        # construct graph
        graph_neighbor = collections.defaultdict(list)
        for s, e, t in times:
            graph_neighbor[s].append((e, t))
        
        # Dijkstra
        SPT = {}
        min_heap = [(0, K)]
        
        while min_heap:
            delay, node = heapq.heappop(min_heap)
            if node not in SPT:
                SPT[node] = delay
                for n, d in graph_neighbor[node]:
                    if n not in SPT:
                        heapq.heappush(min_heap, (d + delay, n))
        
        return max(SPT.values()) if len(SPT) == N else -1
```

### [cheapest-flights-within-k-stops](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)

- 在标准的单源最短路径问题上限制了路径的边数，因此需要同时维护当前 SPT 内每个结点最短路径的边数，当遇到边数更小的路径 (边权和可以更大) 时结点需要重新入堆，以更新后继在边数上限内没达到的结点。

```Python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # construct graph
        graph_neighbor = collections.defaultdict(list)
        for s, e, p in flights:
            graph_neighbor[s].append((e, p))
        
        # modified Dijkstra
        prices, steps = {}, {}
        min_heap = [(0, 0, src)]
        
        while len(min_heap) > 0:
            price, step, node = heapq.heappop(min_heap)
            
            if node == dst: # early return
                return price

            if node not in prices:
                prices[node] = price
            
            steps[node] = step
            if step <= K:
                step += 1
                for n, p in graph_neighbor[node]:
                    if n not in prices or step < steps[n]:
                        heapq.heappush(min_heap, (p + price, step, n))
        
        return -1
```
