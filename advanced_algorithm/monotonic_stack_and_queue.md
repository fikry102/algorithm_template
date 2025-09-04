# 单调栈 & 单调队列

## 简介

- **单调栈**：栈中元素保持单调性，常用于找左右第一个比当前元素大/小的位置。  
- **单调队列**：队列中元素保持单调性，常用于滑动窗口最大/最小值。

---

## 单调栈

### 模板

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

### 模板

```python
from collections import deque

q = deque()
for i, x in enumerate(nums):
    if q and q[0] <= i - k:
        q.popleft()
    while q and nums[q[-1]] <= x:
        q.pop()
    q.append(i)
    if i >= k - 1:
        res.append(nums[q[0]])
```

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
