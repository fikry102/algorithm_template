# 线段树

## 简介

线段树是一种二叉树结构，支持高效的区间查询与更新。常用于：
- 区间和查询
- 区间最值查询
- 区间修改

复杂度：构建 O(n)，查询/更新 O(log n)。

---

## 模板

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def update(self, i, val):
        pos = i + self.n
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]

    def query(self, l, r):
        l += self.n; r += self.n
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.tree[l]; l += 1
            if r % 2 == 0:
                s += self.tree[r]; r -= 1
            l //= 2; r //= 2
        return s
```

---

## 经典题目

#### [307. Range Sum Query - Mutable](https://leetcode-cn.com/problems/range-sum-query-mutable/)

```python
class NumArray:
    def __init__(self, nums):
        self.seg = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.seg.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.seg.query(left, right)
```

---

## 小结

- 线段树灵活但实现复杂。  
- 更适合需要多次区间查询 + 更新的场景。

## 练习

- [307. Range Sum Query - Mutable](https://leetcode-cn.com/problems/range-sum-query-mutable/)  
- [699. Falling Squares](https://leetcode-cn.com/problems/falling-squares/)
