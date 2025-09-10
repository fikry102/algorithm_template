# 线段树

## 简介
- 线段树是一种二叉树结构，支持高效的区间查询与更新，常用于区间和、区间最值以及带修改的区间问题。
- 复杂度：构建 O(n)，查询/更新 O(log n)。

### 1.线段树是什么
- 线段树把数组按区间对半拆分成一棵二叉树，节点存该区间的信息，从而实现构建 O(n)、查询/更新 O(log n)，可维护区间和、最值等。

### 2.先用直观类比
- 把数组想成一排书，线段树把它分成“左半书架”和“右半书架”，再继续对半分，直到每格只放一本书（叶子）。
- 每个“书架格”记一个小结论（例如这段书的总页数/最薄的书），父格的结论来自“左格”和“右格”的合并（如求和/取最小）。
- 查一段书时，不必逐本看，只要用最少的“整格”覆盖这段即可，答案是这些格子的小结论再合并；整段会被拆成 O(log n) 个格子来覆盖。
- 改动一本书的页数，就顺着它所在的叶子往上把经过的格子结论改一下，路径长度是树高 O(log n)。

### 3.为什么要用它（而不是朴素/预处理）
- 朴素做法每次区间查询/修改是 O(n)，在多次操作场景下效率低。
- ST 表预处理 O(n log n)、查询 O(1)，但不支持在线更新。
- 线段树兼顾“多次查询 + 在线更新”，查询/更新都是 O(log n)。

### 4.它长什么样、怎么建
- 区间 [l,r] 的节点：若 l=r，是叶子；否则分成 [l,mid] 和 [mid+1,r] 建左右儿子；父节点的值由左右儿子按所需运算（如 min/sum/max）合并。
- 构建访问每个节点一次，时间/空间都是 O(n)。
- 线段树可存区间和、最小值、最大值等；支持单点修改、区间查询，甚至区间修改（配合懒标记）。


### 5.模板
- 使用“底部对齐”的数组实现：把原数组放在 tree[n..2n-1]，再自底向上父=左子+右子建树，复杂度 O(n)。
- update：把叶子改了，沿父链上去重算，路径 O(log n)。
- query：两端指针从叶子向上跳，遇到“整段在左/右侧”的就吸收贡献，直到两端交叉，步数 O(log n)。
- 另一种常见实现是“完全二叉树的数组树”，通常预分配到 4N 以避免越界，左右儿子用 2k 和 2k+1（或 0-based 的 2k+1、2k+2），实现简洁稳健。

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

query部分解读：


```python
if l % 2 == 1: 	
		s += tree[l]; l += 1
```

如果 l 是右孩子（l % 2 == 1），说明它这一整段无法和它的左兄弟一起上移合并（左兄弟不在区间内）。必须先把它这一段的值计入答案，然后把 l 往右移一个（l += 1）。



```python
if r % 2 == 0: 
		s += tree[r]; r -= 1
```

如果 r 是左孩子（r % 2 == 0），说明它这一整段无法和它的右兄弟一起上移合并（右兄弟不在区间内）。必须先把它这一段的值计入答案，然后把 r 往左移一个（r -= 1）。



```python
l //= 2; r //= 2
```

处理完左右边界后，把 l、r 同时上移到它们的父节点继续处理更高一层的覆盖。



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
