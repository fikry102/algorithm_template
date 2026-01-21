# 算法模板

本项目 [algorithm_template](https://github.com/fikry102/algorithm_template) 基于 **Python** 实现，覆盖了常见的数据结构与算法模板，适合刷题和求职面试快速上手。

## 为什么要用算法模板？

刷题不仅是练习算法本身，更是掌握套路与方法。  
本仓库将常见题型整理为「模板化解法」，帮助你：

- 快速找到切入点，不再无从下手  
- 熟悉高频题型，总结可复用的解题套路  
- 一个月左右完成系统刷题，冲刺大厂面试

也可以直接上手leetcode热题100感受一下，https://leetcode.cn/problem-list/2cktkvj/


## **常见技巧和经典问题**

1. **哈希表 / 计数**

   * **经典问题**：**Two Sum**（两数之和）
   * **问题简述**：在数组中找到两个数，使得它们的和等于目标值。
   * **insight**：用哈希表存储已访问的元素，遍历时查找是否有匹配的补数。

2. **双指针 / 滑动窗口**

   * **经典问题**：**Longest Substring Without Repeating Characters**（最长无重复字符的子串）
   * **问题简述**：找出没有重复字符的最长子串。
   * **insight**：左指针固定，右指针扩展，遇到重复字符时，移动左指针直到不重复。

3. **动态规划 (DP)**

   * **经典问题**：**Climbing Stairs**（爬楼梯）
   * **问题简述**：每次爬1步或2步，求到达第n阶的不同方法数。
   * **insight**：状态转移方程 `dp[i] = dp[i-1] + dp[i-2]`，计算每一步的方法数。

4. **栈与队列**

   * **经典问题**：**Valid Parentheses**（有效括号）
   * **问题简述**：判断一个字符串中的括号是否有效，匹配且顺序正确。
   * **insight**：使用栈存左括号，遇右括号时，检查栈顶是否匹配。

5. **DFS / BFS**

   * **经典问题**：**Number of Islands**（岛屿数量）
   * **问题简述**：在二维网格中，计算有多少个岛屿（连通的 `1`）。
   * **insight**：DFS 或 BFS 遍历每个陆地，标记已访问的地方，递归检查连通的陆地。

6. **并查集 (DSU)**

   * **经典问题**：**Number of Provinces**（省份数量）
   * **问题简述**：给定一个城市的连接矩阵，找出有多少个连通的省份。
   * **insight**：用并查集合并相连的城市，统计连通的省份数量。

7. **贪心算法**

   * **经典问题**：**Activity Selection**（活动选择）
   * **问题简述**：选择最多的互不重叠的活动。
   * **insight**：选择最早结束的活动，确保后续活动不与前面的活动重叠。

8. **二分查找**

   * **经典问题**：**Search Insert Position**（查找插入位置）
   * **问题简述**：在排序数组中查找一个目标值，若不存在，返回它应该插入的位置。
   * **insight**：使用二分查找，通过折半的方法快速定位目标值或插入位置。

9. **位运算**

   * **经典问题**：**Single Number**（只出现一次的数字）
   * **问题简述**：在一个数组中，所有元素出现两次，除了一个元素出现一次，找出那个唯一的元素。
   * **insight**：使用异或操作，两个相同的数异或为 0，最终留下的就是唯一的那个数。

10. **分治与递归**

    * **经典问题**：**Merge Sort**（归并排序）
    * **问题简述**：将一个数组分成两半，递归排序并合并。
    * **insight**：将数组不断拆分为更小的部分，递归排序后，再将结果合并。

### **总结：常见技巧和经典问题**

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

## 核心内容

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


## 使用心得

- 文章主要介绍解题思路和关键技巧，每篇末尾配套练习题，建议动手写一遍，加深理解。  
- 刷完一遍目录，基本能覆盖国内一线大厂（如 BAT：百度、阿里、腾讯；以及 TMD：字节、美团、滴滴）的常考题型。  
- 建议 **按题型分类刷题**，不要盲目从头到尾刷题库，效率更高。  
- 刷题时遇到 Hard 题没思路，可以先跳过，打好基础再回头攻克。  


## 推荐刷题路径

1. 按照 [SUMMARY.md](SUMMARY.md) 的目录顺序刷一遍。  
2. 遇到卡住的题目可以先跳过，保证整体进度。  
3. 建议用一个月时间完成一轮，同时结合投递简历进行面试。  
4. 面试遇到提示，优先套用模板思路，别错过良机。  


## 后续计划

本项目会持续更新和完善，欢迎关注。  
如果对你有帮助，点个 **star** ⭐️ 支持一下！

- [algorithm_template](https://github.com/fikry102/algorithm_template)  


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=fikry102/algorithm_template&type=Date)](https://www.star-history.com/?#fikry102/algorithm_template&Date)

![GitHub visitors](https://visitor-badge.laobi.icu/badge?page_id=fikry102.algorithm_template)
