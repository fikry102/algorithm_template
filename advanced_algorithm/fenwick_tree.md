# 树状数组 (Fenwick Tree)

## 简介

树状数组是一种高效的数据结构：
- 单点更新 O(log n)  
- 前缀和查询 O(log n)  

相比线段树实现更简单，但功能较少。

---

## 模板

```python
class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.query(r) - self.query(l-1)
```

---

## 经典题目

#### [315. Count of Smaller Numbers After Self](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)

思路：离散化数组，倒序遍历，用树状数组统计前缀和。

```python
class Solution:
    def countSmaller(self, nums):
        ranks = {v:i+1 for i,v in enumerate(sorted(set(nums)))}
        ft = FenwickTree(len(ranks))
        res = []
        for x in nums[::-1]:
            res.append(ft.query(ranks[x]-1))
            ft.update(ranks[x], 1)
        return res[::-1]
```

#### [493. Reverse Pairs](https://leetcode-cn.com/problems/reverse-pairs/)

思路：类似，借助离散化与树状数组计数。

---

## 小结

- 树状数组比线段树轻量，适合频繁单点更新 + 区间和查询的场景。

## 练习

- [315. Count of Smaller Numbers After Self](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)  
- [493. Reverse Pairs](https://leetcode-cn.com/problems/reverse-pairs/)  
- [307. Range Sum Query - Mutable](https://leetcode-cn.com/problems/range-sum-query-mutable/)
