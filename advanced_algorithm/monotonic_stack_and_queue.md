# 单调栈 & 单调队列

## 简介

- **单调栈**：栈中元素保持单调性，常用于找左右第一个比当前元素大/小的位置。  
- **单调队列**：队列中元素保持单调性，常用于滑动窗口最大/最小值。

---

## 单调栈

### 1.单调栈是什么？
- 单调栈是一个在遍历数组时，保持“栈内元素按值单调（递增或递减）”的不变量，从而用 O(n) 的总复杂度解决“下一个/上一个更大（更小）元素”“跨度（span）”“直方图最大矩形”等问题。

### 2.为什么是 O(n)
- 每个下标最多被压栈一次、被弹栈一次。虽然有 while 循环，但每个元素被弹的那一次只发生一次，全程总弹栈次数 ≤ n，所以总复杂度 O(n)。

### 3.核心不变量
- 栈里存“下标”，不用值：
  - 用下标能回看原数组 nums[idx] 取值；
  - 能区分相等值的位置；
  - 常用于计算距离、宽度（索引差）。
- 单调性方向要与需求一致：
  - 想找“下一个更大”：维护“递减栈”（栈顶最小，遇到更大就弹出）。
  - 想找“下一个更小”：维护“递增栈”（栈顶最大，遇到更小就弹出）。
- 弹栈的本质：
  - 当前元素“击败”了栈顶元素（成为它的最近更大/更小的边界），在弹栈的那一刻就能产出答案或更新跨度。

### 4.模板

```python
stack = []
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] >= x:
        stack.pop()
    stack.append(i)
```
维护一个单调栈（存下标），在遍历时用当前元素去弹掉不满足单调性的栈顶：
执行 while 后，栈从底到顶对应的值严格递增：nums[stack[0]] < nums[stack[1]] < ... < nums[stack[-1]] < x。
### 经典题目

#### [84. Largest Rectangle in Histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

```python
class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)
        return res
```

#### [42. Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded = min(h, height[stack[-1]]) - height[top]
                res += distance * bounded
            stack.append(i)
        return res
```

---

## 单调队列

### 1.单调队列是什么？

- 单调队列是在滑动窗口内用一个保持单调性的双端队列，随时间仅保留“有可能成为当前或未来窗口答案”的候选下标，从而以 O(1) 摘取当前窗口极值（最大/最小）。

### 2.为什么能做到 O(n)

- 每个元素只会入队一次。
- 可能被后续更优元素从队尾弹出一次。
- 过期时从队头弹出一次。
- 因此总操作次数与元素个数同阶，整轮遍历为 O(n)。

### 3.核心不变量（背下这三条）

- 只存“下标”而非值：
  - 用下标判断是否过期（是否滑窗左边界之外）。
  - 用下标回看 nums[idx] 取值，正确处理重复值。
- 单调性：
  - 取最大值时，队列按值单调递减（队头最大）。
  - 取最小值时，队列按值单调递增（队头最小）。
- 合法性：
  - 队头必须在当前窗口范围内，若过期（idx < i - k + 1）立即从队头弹出。

### 4.模板（滑动窗口最大值）
```python
from collections import deque

q = deque()
res = []
for i, x in enumerate(nums):
    # 1) 移除过期下标：窗口为 [i - k + 1, i]
    if q and q[0] <= i - k:
        q.popleft()
    # 2) 维持递减：去除所有不如当前元素 x 的尾部候选
    while q and nums[q[-1]] <= x:
        q.pop()
    # 3) 新元素入队（存下标）
    q.append(i)
    # 4) 窗口形成后输出答案
    if i >= k - 1:
        res.append(nums[q[0]])
```
- 若要求最小值，只需把维持单调的比较改为 nums[q[-1]] >= x 即可。

### 经典题目

#### [239. Sliding Window Maximum](https://leetcode-cn.com/problems/sliding-window-maximum/)

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
```python
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        from collections import deque
        q, res = deque(), []
        for i, x in enumerate(nums):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
```

#### [862. Shortest Subarray with Sum at Least K](https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/)

```python
class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        from collections import deque
        n = len(nums)
        pre = [0]
        for x in nums:
            pre.append(pre[-1] + x)
        q = deque()
        res = n + 1
        for i, s in enumerate(pre):
            while q and s - pre[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and pre[q[-1]] >= s:
                q.pop()
            q.append(i)
        return res if res <= n else -1
```

---

## 小结

- 单调栈适合区间边界问题。  
- 单调队列适合滑动窗口问题。

## 练习

- [84. Largest Rectangle in Histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)  
- [42. Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/)  
- [239. Sliding Window Maximum](https://leetcode-cn.com/problems/sliding-window-maximum/)  
- [862. Shortest Subarray with Sum at Least K](https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/)
