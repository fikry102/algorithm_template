# 算法模板

本项目 [algorithm_template](https://github.com/fikry102/algorithm_template) 基于 **Python** 实现，覆盖了常见的数据结构与算法模板，适合刷题和求职面试快速上手。


## 0.LeetCode Hot100速通
可以直接上手LeetCode热题100感受一下，https://leetcode.cn/problem-list/2cktkvj/

新增LeetCode Hot 100解题思路和代码：[leetcode_hot_100_solutions](leetcode_hot100/insight_and_solution.md)

欢迎大家提Issue讨论和提交PR贡献更好的解法。

## 1.为什么要用算法模板？

刷题不仅是练习算法本身，更是掌握套路与方法。  
本仓库将常见题型整理为「模板化解法」，帮助你：

- 快速找到切入点，不再无从下手  
- 熟悉高频题型，总结可复用的解题套路  
- 一个月左右完成系统刷题，冲刺大厂面试

## 2.常见解题技巧和经典问题

###1. 哈希表 / 计数

**经典问题**:Two Sum(两数之和)

**问题简述**:给定一个整数数组 `nums` 和一个目标值 `target`,在数组中找到两个数,使它们的和等于 `target`,返回这两个数的下标。

**解法**:遍历数组,对于当前元素 `x`,在哈希表中查找是否存在 `target - x`。如果存在,直接返回这两个下标;否则把 `x` 存入哈希表,继续遍历。

**insight**:哈希表把"查找一个数是否存在"的操作从 O(n) 降到 O(1),用空间换时间,一次遍历即可解决,整体时间复杂度 O(n)。

---

###2. 双指针 / 滑动窗口

**经典问题**:Longest Substring Without Repeating Characters(最长无重复字符的子串)

**问题简述**:给定一个字符串,找出其中不含重复字符的最长子串的长度。例如 `"abcabcbb"` 的答案是 `"abc"`,长度为 3。

**解法**:维护一个窗口 `[left, right]`,窗口内的字符始终无重复。右指针不断向右扩展,遇到重复字符时,左指针向右移动直到窗口内无重复。过程中记录窗口的最大长度,通常配合哈希集合判断重复。

**insight**:左右指针都只向右移动,每个字符最多被访问两次,时间复杂度 O(n)。滑动窗口适用于"连续子数组/子串"的最值问题。

---

###3. 动态规划 (DP)

**经典问题**:Climbing Stairs(爬楼梯)

**问题简述**:有 n 阶楼梯,每次可以爬 1 阶或 2 阶,问到达第 n 阶有多少种不同的方法。

**解法**:到达第 i 阶,要么从第 i-1 阶爬 1 步上来,要么从第 i-2 阶爬 2 步上来,所以 `dp[i] = dp[i-1] + dp[i-2]`,初始条件 `dp[1] = 1`,`dp[2] = 2`。

**insight**:DP 的核心是**最优子结构**(大问题的解由子问题推出)和**重叠子问题**(子问题会被重复计算,所以要存起来)。解题关键是找到状态定义和状态转移方程。

---

###4. 栈与队列

**经典问题**:Valid Parentheses(有效括号)

**问题简述**:给定一个只包含 `()[]{}` 的字符串,判断括号是否合法匹配。例如 `"()[]{}"` 合法,`"([)]"` 不合法。

**解法**:遍历字符串,遇到左括号压栈,遇到右括号时弹出栈顶元素并检查是否匹配。最后栈必须为空,否则说明有未匹配的左括号。

**insight**:栈的"后进先出"特性天然适合处理**就近匹配**问题——最近的左括号应该最先被匹配。这种对称嵌套结构通常都能用栈解决。

---

###5. DFS / BFS

**经典问题**:Number of Islands(岛屿数量)

**问题简述**:给一个由 `'1'`(陆地)和 `'0'`(水)组成的二维网格,计算岛屿的数量。岛屿由水平或垂直相邻的陆地连接而成。

**解法**:遍历网格,每遇到一个未访问的 `'1'`,岛屿数 +1,然后用 DFS 或 BFS 把与它相连的所有 `'1'` 标记为已访问,确保每个岛屿只被计数一次。

**insight**:DFS 一条路走到底,通常用递归实现,代码简洁;BFS 一层一层扩展,用队列实现,适合求**最短路径**。两者都要处理好"已访问"标记,避免死循环。

---

###6. 并查集 (DSU)

**经典问题**:Number of Provinces(省份数量)

**问题简述**:给定 n 个城市和一个 n×n 的邻接矩阵 `isConnected`,如果两个城市直接或间接相连,则属于同一个省份。求一共有多少个省份。

**解法**:用并查集维护元素的集合归属,核心是两个操作:`find(x)` 找到 x 所在集合的根,`union(x, y)` 合并两个集合。遍历邻接矩阵,把相连的城市合并,最后统计不同根的个数。

**insight**:并查集擅长处理**动态连通性**——边在不断加入的过程中,快速判断两点是否连通。配合路径压缩和按秩合并,单次操作近似 O(1)。

---

###7. 贪心算法

**经典问题**:Activity Selection(活动选择)

**问题简述**:有 n 个活动,每个活动有开始时间和结束时间。同一时刻只能参加一个活动,求最多能参加多少个不重叠的活动。

**解法**:按**结束时间**从小到大排序,从最早结束的活动开始选,每次选择开始时间不早于上一个已选活动结束时间的活动。

**insight**:贪心的核心是"每步都做局部最优,期望得到全局最优"。难点不在实现,而在**证明策略的正确性**——选最早结束的活动,是因为它给后面留下了最多的时间空间。错误的贪心策略会得到错误的答案。

---

###8. 二分查找

**经典问题**:Search Insert Position(查找插入位置)

**问题简述**:给定一个排序数组和目标值,如果找到目标值返回其下标,否则返回它应该插入的位置(保持数组有序)。

**解法**:维护 `left` 和 `right` 两个边界,每次取中点 `mid`。`nums[mid] == target` 直接返回;`nums[mid] < target` 则 `left = mid + 1`;否则 `right = mid - 1`。最后 `left` 就是插入位置。

**insight**:时间复杂度 O(log n),前提是数据**有序**或具有某种**单调性**。难点在于边界处理,推荐固定一种写法(如左闭右闭),避免出错。

---

###9. 位运算

**经典问题**:Single Number(只出现一次的数字)

**问题简述**:一个非空数组中,除了一个元素只出现一次外,其他每个元素都出现两次。找出那个只出现一次的元素,要求线性时间复杂度且不使用额外空间。

**解法**:把所有数字异或起来。利用 `a ^ a = 0` 和 `a ^ 0 = a`,成对的数字两两抵消,最后剩下的就是那个唯一的数。

**insight**:异或是"无进位加法",也可以理解成"差异检测器"——相同消失,不同保留。位运算常常能给出**空间 O(1)** 的优雅解法。

---

###10. 分治与递归

**经典问题**:Merge Sort(归并排序)

**问题简述**:对一个数组进行排序,要求时间复杂度 O(n log n)。

**解法**:三步走——**分**:把数组从中间分成两半;**治**:递归地对两半分别排序;**合**:用双指针把两个已排序的子数组合并成一个有序数组。

**insight**:分治的精髓是把大问题拆成结构相同的小问题,分别解决后再合并。递归式 `T(n) = 2T(n/2) + O(n)` 得到 O(n log n)。写递归要明确**终止条件**和**问题规模缩小**两个要素。

### 常见解题技巧和经典问题-简短总结

1. **哈希表 / 计数**：用来快速查找和统计元素
2. **双指针 / 滑动窗口**：处理区间问题，优化时间复杂度
3. **动态规划**：通过拆解问题，逐步求解最优解
4. **栈与队列**：用于处理顺序问题，解决括号匹配、最小栈等
5. **DFS/BFS**：图的遍历，路径查找，连通性
6. **并查集 (DSU)**：合并集合、动态连通
7. **贪心算法**：选择最优局部解，确保全局最优
8. **二分查找**：在有序数据中快速查找目标值
9. **位运算**：高效地进行数值操作、状态压缩
10. **分治与递归**：将问题分解，递归求解，最终合并结果

## 3.核心内容目录

### 🐣 入门篇
- [使用 Python3 写算法题](./introduction/python.md)
- [算法快速入门](./introduction/quickstart.md)
- [VS Code编程快捷键](./introduction/shortcuts.md)
- [Python高阶语法](./introduction/advanced_python.md) 
- [Python元编程](./introduction/metaprogramming.md)

### 🐰 数据结构篇
- [二叉树](./data_structure/binary_tree.md)
- [链表](./data_structure/linked_list.md)
- [栈和队列](./data_structure/stack_queue.md)
- [优先级队列 (堆)](./data_structure/heap.md)
- [并查集](./data_structure/union_find.md)
- [二进制](./data_structure/binary_op.md)

### 🐮 基础算法篇
- [二分搜索](./basic_algorithm/binary_search.md)
- [排序算法](./basic_algorithm/sort.md)
- [动态规划](./basic_algorithm/dp.md)
- [图相关算法](./basic_algorithm/graph)
  - [图的表示](./basic_algorithm/graph/graph_representation.md)
  - [深度优先搜索 / 广度优先搜索](./basic_algorithm/graph/bfs_dfs.md)
  - [拓扑排序](./basic_algorithm/graph/topological_sorting.md)
  - [最小生成树](./basic_algorithm/graph/mst.md)
  - [最短路径](./basic_algorithm/graph/shortest_path.md)

### 🦁 高阶算法篇
- [前缀和 & 差分数组](./advanced_algorithm/prefix_sum_and_difference.md)
- [单调栈 & 单调队列](./advanced_algorithm/monotonic_stack_and_queue.md)
- [线段树 (Segment Tree)](./advanced_algorithm/segment_tree.md)
- [树状数组 (Fenwick Tree)](./advanced_algorithm/fenwick_tree.md)

### 🐲 算法策略
- [递归策略](./algorithm_strategies/recursion.md)
- [滑动窗口策略](./algorithm_strategies/slide_window.md)
- [二叉搜索树](./algorithm_strategies/binary_search_tree.md)
- [回溯策略](./algorithm_strategies/backtrack.md)


## 4.使用心得

- 文章主要介绍解题思路和关键技巧，每篇末尾配套练习题，建议动手写一遍，加深理解。  
- 刷完一遍目录，基本能覆盖国内一线大厂（如 BAT：百度、阿里、腾讯；以及 TMD：字节、美团、滴滴）的常考题型。  
- 建议 **按题型分类刷题**，不要盲目从头到尾刷题库，效率更高。  
- 刷题时遇到 Hard 题没思路，可以先跳过，打好基础再回头攻克。  


## 5.推荐刷题路径

1. 按照 [SUMMARY.md](SUMMARY.md) 的目录顺序刷一遍。  
2. 遇到卡住的题目可以先跳过，保证整体进度。  
3. 建议用一个月时间完成一轮，同时结合投递简历进行面试。  
4. 面试遇到提示，优先套用模板思路，别错过良机。  


## 6.后续计划

本项目会持续更新和完善，欢迎关注。  
如果对你有帮助，点个 **star** ⭐️ 支持一下！

- [algorithm_template](https://github.com/fikry102/algorithm_template)  


## 7.Star History

[![Star History Chart](https://api.star-history.com/svg?repos=fikry102/algorithm_template&type=Date)](https://www.star-history.com/?#fikry102/algorithm_template&Date)

![GitHub visitors](https://visitor-badge.laobi.icu/badge?page_id=fikry102.algorithm_template)
