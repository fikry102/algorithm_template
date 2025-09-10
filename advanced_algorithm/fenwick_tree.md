# 树状数组 (Fenwick Tree)

## 简介
- 用一个数组维护“若干右端点对齐的块的和”，把单点更新与前缀和查询都做到 O(log n)。

### 1. 树状数组是什么
- 轻量的数据结构，专门支持：
  - 单点更新：A[i] += delta（O(log n)）
  - 前缀和：sum(1..r)（O(log n)）
  - 区间和：sum(l..r) = sum(1..r) - sum(1..l-1)

### 2. lowbit(i) 是什么
- 定义：lowbit(i) = i & -i。
- 含义：保留 i 二进制中“最右侧的那个 1”，其余位清零，结果必是 2 的幂（1、2、4、8…）。
- 原理（补码直觉）：-i = ~i + 1；i 与 -i 按位与时，只有最低位的 1 在两者同为 1，高位一正一反为 0。
- 在树状数组里：节点 i 管的区间是 (i - lowbit(i) + 1 .. i]，长度就是 lowbit(i)。

### 3. 两个核心操作怎么走（直觉）
- 前缀和 sum_prefix(r)：把 [1..r] 拆成几块“右端点对齐、长度为 2 的幂”的区间。
  - 每次累加当前块 [r - lowbit(r) + 1 .. r]，然后 r -= lowbit(r) 跳到左边的上一块，直到 r=0。
- 单点增加 add(i, delta)：A[i] 变了，要把所有“右端点对齐且包含 i 的块”都加上 delta。
  - 先更新块右端点 i（块长 lowbit(i)），然后 i += lowbit(i) 跳到更大的父块，直到越界。
- 两者都在“处理/去掉最低位的 1”，步数与二进制位数同阶，O(log n)。

### 4. 小例子（n=8，1-based，用不抽象的方式看块）
- 说明：“5(1) → 6(2) → 8(8)”中括号是 lowbit(i)，也是该节点覆盖区间的长度；节点 i 覆盖 (i - lowbit(i) + 1 .. i]，右端点就是 i。
- 单点更新 update(5, +x)：
  - 节点 5：lowbit=1，覆盖 [5,5]，包含下标 5 → 加 x
  - 跳到 6：lowbit=2，覆盖 [5,6]，包含 5 → 再加 x
  - 跳到 8：lowbit=8，覆盖 [1,8]，包含 5 → 再加 x
  - 跳到 16 越界结束。触达并更新的节点索引是 {5,6,8}。
- 前缀和 sum_prefix(13)（13 的二进制 1101）：
  - 取 [13,13]（长 1），r=12
  - 取 [9,12]（长 4），r=8
  - 取 [1,8]（长 8），r=0 结束
  - 前缀和 = 三块之和
- 为了直观感受覆盖区间（n=8）：
  - 1: lowbit=1 覆盖[1,1]
  - 2: lowbit=2 覆盖[1,2]
  - 3: lowbit=1 覆盖[3,3]
  - 4: lowbit=4 覆盖[1,4]
  - 5: lowbit=1 覆盖[5,5]
  - 6: lowbit=2 覆盖[5,6]
  - 7: lowbit=1 覆盖[7,7]
  - 8: lowbit=8 覆盖[1,8]

### 5. 模板（Python，API 采用 1-based 索引）
```python
class FenwickTree:
    def __init__(self, n):
        # 有效下标 1..n
        self.tree = [0] * (n + 1)

    @staticmethod
    def _lowbit(i):
        return i & -i

    def update(self, i, delta):
        """A[i] += delta，i 为 1-based"""
        while i < len(self.tree):
            self.tree[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        """返回 sum(1..i)，i 为 1-based"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= self._lowbit(i)
        return s

    def range_sum(self, l, r):
        """返回 sum(l..r)，闭区间，l/r 为 1-based"""
        return self.query(r) - self.query(l - 1)
```
- 若你的原数组是 0-based，下标需先 +1 再调用；或建树时用 enumerate(arr, start=1) 逐点 update。
  

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
