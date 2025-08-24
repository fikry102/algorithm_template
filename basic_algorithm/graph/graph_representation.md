# 图的表示

图的邻接表和邻接矩阵表示最为常用，但是有时需要建图时这两种表示效率不是很高，因为需要构造每个结点和每一条边。此时使用一些隐式的表示方法可以提升建图效率。

### [word-ladder](https://leetcode-cn.com/problems/word-ladder/)

```Python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        N, K = len(wordList), len(beginWord)
        
        find_end = False
        for i in range(N):
            if wordList[i] == endWord:
                find_end = True
                break
        
        if not find_end:
            return 0
        
        wordList.append(beginWord)
        N += 1
        
        # clustering nodes for efficiency compare to adjacent list
        cluster = collections.defaultdict(list)
        for i in range(N):
            node = wordList[i]
            for j in range(K):
                cluster[node[:j] + '*' + node[j + 1:]].append(node)
        
        # bidirectional BFS
        visited_start, visited_end = set([beginWord]), set([endWord])
        bfs_start, bfs_end = collections.deque([beginWord]), collections.deque([endWord])
        step = 2
        while bfs_start and bfs_end:
          
            # start
            num_level = len(bfs_start)
            while num_level > 0:
                node = bfs_start.popleft()
                for j in range(K):
                    key = node[:j] + '*' + node[j + 1:]
                    for n in cluster[key]:
                        if n in visited_end:
                            return step * 2 - 2
                        if n not in visited_start:
                            visited_start.add(n)
                            bfs_start.append(n)
                num_level -= 1
            
            # end
            num_level = len(bfs_end)
            while num_level > 0:
                node = bfs_end.popleft()
                for j in range(K):
                    key = node[:j] + '*' + node[j + 1:]
                    for n in cluster[key]:
                        if n in visited_start:
                            return step * 2 - 1
                        if n not in visited_end:
                            visited_end.add(n)
                            bfs_end.append(n)
                num_level -= 1
            step += 1
        
        return 0
```

