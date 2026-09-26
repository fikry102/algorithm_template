# LeetCode算法速通笔记-python版本

> 视频链接：[30分06秒 Leetcode速通—python路线](https://www.bilibili.com/video/BV1dcUMBeEH4?vd_source=51eb5bc15bb407fbaa7b6162df159e2a)
> 

本笔记围绕常见算法题，整理问题识别、思路推导、Python 实现与易错点，并附 LeetCode 练习链接。

- **第一部分：核心算法与解题方法。** 覆盖哈希表、双指针、前缀和、链表、二叉树、图论、回溯和动态规划。各章先概括适用场景与方法，再通过例题说明实现。
- **第二部分：Python 语法糖与其他技巧。** 汇总常用语法与容器、排序算法、二分查找、单调栈和单调队列，供解题时查阅。

## 目录

**第一部分：核心算法与解题方法**

| 章节 | 内容 |
| --- | --- |
| [1. 哈希表](about:blank#1-%E5%93%88%E5%B8%8C%E8%A1%A8) | 题 1 两数之和；题 2 字母异位词分组 |
| [2. 双指针](about:blank#2-%E5%8F%8C%E6%8C%87%E9%92%88) | 题 3 移动零；题 4 三数之和；题 5 接雨水；题 6 滑动窗口最大值；题 7 最小覆盖子串 |
| [3. 前缀和](about:blank#3-%E5%89%8D%E7%BC%80%E5%92%8C) | 题 8 和为 K 的子数组；题 9 除自身以外数组的乘积 |
| [4. 链表](about:blank#4-%E9%93%BE%E8%A1%A8) | 题 10 相交链表；题 11 环形链表 II；题 12 K 个一组反转链表 |
| [5. 二叉树](about:blank#5-%E4%BA%8C%E5%8F%89%E6%A0%91) | 定义、DFS 递归/迭代、BFS；题 13 路径总和 III；题 14 验证 BST；题 15 翻转二叉树；题 16 右视图 |
| [6. 图论](about:blank#6-%E5%9B%BE%E8%AE%BA) | 题 19 岛屿数量 DFS；题 20 岛屿数量 BFS |
| [7. 回溯算法](about:blank#7-%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95) | 题 17 全排列；题 18 N 皇后 |
| [8. 动态规划](about:blank#8-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92) | 题 21 爬楼梯；题 22 打家劫舍；题 23 LIS；题 24 0/1 背包；题 25 完全背包；题 26/27 股票买卖 |

**第二部分：Python 工具与其他技巧**

| 章节 | 内容 |
| --- | --- |
| [9. Python 语法与常用工具](about:blank#9-python-%E8%AF%AD%E6%B3%95%E4%B8%8E%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7) | lambda、推导式、enumerate、zip、作用域、复制、Counter、defaultdict、deque、heapq |
| [10. 排序算法](about:blank#10-%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95) | 冒泡、选择、归并、快速、堆排序 |
| [11. 二分查找](about:blank#11-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE) | 普通二分；查找目标的第一个和最后一个位置 |
| [12. 单调栈与单调队列](about:blank#12-%E5%8D%95%E8%B0%83%E6%A0%88%E4%B8%8E%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97) | 原理、循环数组下一个更大元素、滑动窗口最大值 |

**使用约定**

「题 1～27」为笔记题目序号，LeetCode 官方题号见各节链接。通用背包模板另附标为「背包变体」的对应练习，其题意与模板存在区别。

- 题解主要使用独立函数，便于阅读和测试；提交到要求 `class Solution` 的平台时，改成对应方法并添加 `self` 参数。若递归函数本身改成了方法，内部调用也要相应改成 `self.方法名(...)`；方法内部的局部辅助函数仍按普通函数调用。
- 链表和树题使用下面定义的 `ListNode`、`TreeNode`；平台通常会提供它们。
- 除特别说明外，额外空间不计返回答案。`n` 是元素/节点数，`h` 是树高，`w` 是树的最大层宽。
- 哈希表、集合操作按平均 `O(1)` 分析；整数运算按算法题常用的定长整数模型分析。

## 第一部分：核心算法与解题方法

### 1. 哈希表

哈希表通过「键 → 信息」快速查找已记录的数据，适合把重复的遍历查找变成平均 `O(1)` 的查询。

- **查存在性**：用 `set` 判断某个值是否出现过。
- **查位置或次数**：用 `dict` 保存下标，用 `Counter` 或字典计数。
- **按特征分组**：把排序后的字符串、计数元组等作为统一的键。

设计时先确定「查什么、键是什么、值存什么」。查询顺序也属于算法的一部分：如果不能使用当前元素两次，应先查找，再记录当前元素。

#### 题 1：两数之和

**原题链接**：[LeetCode 1 · 两数之和](https://leetcode.cn/problems/two-sum/)

**题意**：给定数组 `nums` 和目标值 `target`，返回两个数之和等于目标值的下标。不能重复使用同一个位置；题目保证存在唯一答案。

示例：`nums = [2, 7, 11, 15]`，`target = 9`，返回 `[0, 1]`。

**思路**：遍历当前数 `num`，查找之前有没有 `target - num`。字典保存「数值 → 下标」。

```python
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]

        # 先查找，再记录，避免使用当前元素两次
        seen[num] = i

    return []
```

例如 `[3, 3]`、目标 `6`：第一个 `3` 先存入字典；第二个 `3` 来时找到前一个，返回 `[0, 1]`。数字相同没关系，只要下标不同。

复杂度：时间 `O(n)`，空间 `O(n)`。

#### 题 2：字母异位词分组

**原题链接**：[LeetCode 49 · 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)

**题意**：把字符种类与出现次数相同、排列顺序可以不同的字符串分到同一组。

示例：`["eat", "tea", "tan", "ate", "nat", "bat"]` 可以分为 `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`。

**思路**：异位词排序后的字符串相同。例如 `eat`、`tea`、`ate` 都变成 `aet`，以它作为字典的键。

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

`sorted(word)` 得到字符列表；`"".join(...)` 把它拼成可作为字典键的字符串。列表本身不能作为字典键。

设有 `m` 个字符串，最长长度为 `L`：时间 `O(mL log(L+1))`，空间上界 `O(m(L+1))`。若字符限定为 26 个小写字母，也可用 26 项计数元组作为键，避免排序。

### 2. 双指针

双指针通过两个位置的配合，避免反复扫描。关键是明确每个指针的职责，以及移动后仍然成立的条件。

| 形式 | 两个位置的职责 | 典型场景 |
| --- | --- | --- |
| 快慢指针 | 一个扫描，一个记录写入位置或跟踪进度 | 移动零、原地去重 |
| 左右指针 | 从两端缩小待处理范围 | 有序数组配对、三数之和、接雨水 |
| 滑动窗口 | 维护连续区间的左右边界 | 窗口最值、最小覆盖子串 |

写代码前先回答：当前区间表示什么？什么条件下移动左端或右端？什么时候更新答案？若每个指针只沿一个方向移动，总移动次数通常是线性的；嵌套 `while` 不一定意味着 `O(n²)`。

#### 题 3：移动零

**原题链接**：[LeetCode 283 · 移动零](https://leetcode.cn/problems/move-zeroes/)

**题意**：把所有 `0` 移到数组末尾，保持非零元素的相对顺序，要求原地修改。

示例：`[0, 1, 0, 3, 12]` 变为 `[1, 3, 12, 0, 0]`。

**思路**：换个角度，把非零数依次放到前面。

- `right`：逐个检查元素。
- `left`：下一个非零数应该放的位置。

```python
def moveZeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
```

**指针初始化：为什么都从 0 开始？**

检查要从下标 `0` 开始，第一项非零数也要放在下标 `0`，所以起点相同，但工作不同。只有找到非零数、放好一个位置后，`left` 才移动；`right` 每轮都移动。

若 `left == right`，交换只是自己与自己交换。若 `left < right`，`left` 到 `right-1` 的位置都已经是零，交换不会打乱前面放好的非零元素。

复杂度：时间 `O(n)`，额外空间 `O(1)`。函数直接修改 `nums`，不需要返回新数组。

#### 题 4：三数之和

**原题链接**：[LeetCode 15 · 三数之和](https://leetcode.cn/problems/3sum/)

**题意**：返回所有和为 `0`、不重复的三元组。三个下标必须不同，相同数值可以来自不同位置。

示例：`[-1, 0, 1, 2, -1, -4]` 返回 `[[-1, -1, 2], [-1, 0, 1]]`。

**思路**：先排序，固定第一个数 `nums[i]`，再用左右指针找另外两个数。

```python
def threeSum(nums):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return ans
```

**为什么先排序？**

- 和太小：左边这个数配上当前可选的最大数都不够，配其他更小的数也不行，因此可以排除它，移动 `left`。
- 和太大：右边这个数配上当前可选的最小数都超了，因此可以排除它，移动 `right`。
- 排序使这种排除不会漏解，也让相同值相邻，便于去重。

去重不是禁止 `[-1, -1, 2]`，而是禁止重复输出同一个三元组。

复杂度：时间 `O(n²)`；Python 排序辅助空间最坏 `O(n)`，不计答案。该实现会排序原数组。

#### 题 5：接雨水

**原题链接**：[LeetCode 42 · 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

**题意**：每根柱子宽度为 `1`，高度非负，求柱子之间能接住多少雨水。

示例：`[0,1,0,2,1,0,1,3,2,1,2,1]` 返回 `6`。

**先理解每一个位置**：水位由左右最高柱子中较矮的一边决定。

`水量[i] = min(左侧最高值, 右侧最高值) - height[i]`

最高值统计包含当前位置，因此差值不会为负。例如 `[3, 0, 2]` 的中间位置接水 `min(3, 2) - 0 = 2`。

先记容易推导的前后缀最高值版本：

```python
def trap_prefix(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    return sum(
        min(left_max[i], right_max[i]) - height[i]
        for i in range(n)
    )
```

时间 `O(n)`，额外空间 `O(n)`。

**进阶：双指针省掉两个数组。** 这里比较两侧已知最高值，比直接比较当前柱高更方便解释。

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    ans = 0

    while left <= right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            ans += left_max - height[left]
            left += 1
        else:
            ans += right_max - height[right]
            right -= 1

    return ans
```

若 `left_max <= right_max`，左位置右侧已经有足够高的墙，限制左位置水位的是 `left_max`，可以立即结算左位置。另一种情况对称。时间 `O(n)`，额外空间 `O(1)`。

#### 题 6：滑动窗口最大值

**原题链接**：[LeetCode 239 · 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)

**题意**：大小为 `k` 的窗口每次右移一格，返回每个完整窗口的最大值。假设 `1 <= k <= len(nums)`。

示例：`nums = [1,3,-1,-3,5,3,6,7]`，`k = 3`，返回 `[3,3,5,5,6,7]`。

**实现：堆 + 延迟删除。**

```python
import heapq

def maxSlidingWindow_heap(nums, k):
    heap = [(-nums[i], i) for i in range(k)]
    heapq.heapify(heap)
    ans = [-heap[0][0]]

    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))

        # 当前窗口是 [i-k+1, i]，下标 <= i-k 的都已过期
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        ans.append(-heap[0][0])

    return ans
```

**过期判断：`heap[0][1] <= i-k` 的含义。**

- 堆中存 `(-数值, 原数组下标)`。`heap[0]` 是堆顶，`heap[0][1]` 是堆顶的原下标。
- 比如 `i=4, k=3`，窗口包含下标 `2、3、4`，所以 `<=1` 的下标都过期；`1` 正是 `i-k`。
- 用 `while`，因为弹出一个过期元素后，新露出的堆顶也可能过期。
- 非堆顶的过期元素先保留，等它来到堆顶再删，不影响当前答案。
- 新入堆的下标 `i` 一定有效，所以这里不会把堆删空。

这份延迟删除实现最坏时间 `O(n log n)`、空间 `O(n)`，不能直接记为 `O(n log k)`、`O(k)`：过期元素可能长期留在堆中。

最优常规解法是**单调队列**，时间 `O(n)`、空间 `O(k)`，完整代码与原理见第 12 章。

#### 题 7：最小覆盖子串

**原题链接**：[LeetCode 76 · 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

**题意**：在 `s` 中找最短的连续子串，使其包含 `t` 的所有字符及足够的出现次数。不存在时返回 `""`。

示例：`s = "ADOBECODEBANC"`，`t = "ABC"`，返回 `"BANC"`。

**思路**：右边扩大窗口，直到字符数量够用；然后左边不断缩小，寻找更短答案。顺序无需与 `t` 相同。

```python
from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    window = {}
    matched = 0  # 已满足数量要求的字符种类数
    left = 0
    best_start = 0
    best_len = float("inf")

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1
        if char in need and window[char] == need[char]:
            matched += 1

        while matched == len(need):
            if right - left + 1 < best_len:
                best_start = left
                best_len = right - left + 1

            old = s[left]
            window[old] -= 1
            if old in need and window[old] < need[old]:
                matched -= 1
            left += 1

    if best_len == float("inf"):
        return ""
    return s[best_start:best_start + best_len]
```

**理解要点**

- 若 `t = "AAAB"`，窗口必须至少有 `3` 个 `A` 和 `1` 个 `B`，不是「有 A、有 B」就够。
- `matched` 统计满足要求的**种类数**。这里总共只需满足 `2` 种字符。
- 添加时只在数量刚好等于需求时 `matched += 1`，第 `4` 个 `A` 不能再次加一。
- 缩小前窗口一定合法，移除一个字符使数量低于要求时，才把对应种类从已满足状态中扣除。
- 先记录当前合法窗口，再移除左字符；移除后可能不再合法。

复杂度：时间 `O(len(s)+len(t))`；空间 `O(Σ)`，`Σ` 为两字符串中不同字符的数量。

### 3. 前缀和

前缀和把「每次重新累加一段」变成「两个累计值相减」。适合静态数组的多次区间求和，也常与哈希表配合，统计满足条件的连续子数组。

**统一下标定义**：`prefix[i]` 表示前 `i` 个元素之和，即 `nums[0:i]` 的和。额外保留 `prefix[0] = 0`，长度为 `n+1`。

```python
def build_prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] + num
    return prefix

def range_sum(prefix, left, right):
    # 原数组闭区间 [left, right] 的和
    return prefix[right + 1] - prefix[left]
```

例如 `nums = [2, -1, 3]`，前缀和为 `[0, 2, 1, 4]`；下标 `[1,2]` 的区间和是 `4-2=2`。预处理 `O(n)`，每次查询 `O(1)`。

**常见变化**：

- 求某段的和：用两个前缀和作差。
- 统计和为 `k` 的连续子数组：当前前缀为 `P`，查询之前出现过多少次 `P-k`。
- 排除当前位置：分别累计左侧和右侧的信息，再合并，例如前缀积 × 后缀积。

前缀也可以保存乘积或最大值，但不都能通过「相减」恢复任意区间；两个前缀最大值就不足以确定区间最大值。

#### 题 8：和为 K 的子数组

**原题链接**：[LeetCode 560 · 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)

**题意**：统计连续子数组中，元素之和恰好等于 `k` 的个数。数组可以包含负数和零。

示例：`[1, 1, 1]`，`k = 2`，返回 `2`。

**推导**：当前前缀和为 `P`，之前某个前缀和为 `Q`，中间子数组之和为 `P-Q`。要等于 `k`，就查找之前的 `Q = P-k`。

```python
def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}

    for num in nums:
        prefix_sum += num
        count += freq.get(prefix_sum - k, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count
```

**容易忘的地方**

- `{0: 1}` 表示空前缀，可以统计从数组开头开始的子数组；不是把空子数组计入答案。
- 相同前缀和可能出现多次，每次对应不同的起点，所以加的是次数。
- 先查询，再记录当前前缀和。如果反过来，在 `k=0` 时会把当前前缀与自己配对，误算空子数组。
- 普通滑动窗口的「和大缩小、和小扩大」不适用：有负数时，移动窗口与总和增减没有固定关系。

复杂度：时间 `O(n)`，空间 `O(n)`。

#### 题 9：除自身以外数组的乘积

**原题链接**：[LeetCode 238 · 除了自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)

**题意**：返回 `answer[i]`，等于除 `nums[i]` 之外所有元素的乘积；不能使用除法，要求线性时间。

示例：`[1, 2, 3, 4]` 返回 `[24, 12, 8, 6]`。

**如何想到？** 「除自己以外」可以拆成「自己左边」和「自己右边」：

`answer[i] = 左边所有数的乘积 × 右边所有数的乘积`

可以先想两个辅助数组，再优化：把左侧乘积直接写到答案数组，右侧乘积用一个变量维护。

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

| 位置 `i` | 数值 | 左边乘积 | 右边乘积 | 答案 |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 24 | 24 |
| 1 | 2 | 1 | 12 | 12 |
| 2 | 3 | 2 | 4 | 8 |
| 3 | 4 | 6 | 1 | 6 |

**先使用，再更新**：先保存 `prefix`，再乘 `nums[i]`，才能排除自己。右侧同理。没有元素的空乘积为 `1`，所以两侧初始值都是 `1`。这也能自然处理数组中的零。

复杂度：时间 `O(n)`，额外空间 `O(1)`。

### 4. 链表

链表通过节点的 `next` 引用连接，不能像数组一样按下标直接访问。解题重点是确定节点关系，并在修改连接时保留后续入口。

- **区分移动与改链**：`p = p.next` 只移动变量的引用；`p.next = q` 才修改连接。
- **修改前先保存**：反转或删除节点时，先保存仍要访问的后继节点。
- **统一头节点处理**：用虚拟头节点 `dummy` 简化可能改变表头的操作。
- **比较节点身份**：相交、相遇等问题使用 `is`，不能只比较 `val`。

每轮都说清楚指针指向什么，再写赋值顺序。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

#### 题 10：相交链表

**原题链接**：[LeetCode 160 · 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

**题意**：给定两个无环单链表的头节点，返回它们首次相交的节点；没有交点则返回 `None`，不改变链表结构。相交指共享同一个节点对象，不是节点值恰好相等。

**思路**：A 指针走完 A 后去走 B，B 指针走完 B 后去走 A，抵消两条链表相交前的长度差。

```python
def getIntersectionNode(headA, headB):
    a, b = headA, headB

    while a is not b:
        a = a.next if a is not None else headB
        b = b.next if b is not None else headA

    return a
```

若有公共尾部，两者最终在交点相遇；若不相交，两者最终都为 `None`。时间 `O(m+n)`，空间 `O(1)`。

#### 题 11：环形链表 II

**原题链接**：[LeetCode 142 · 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

**题意**：返回链表的环入口，没有环则返回 `None`。不修改链表。

**思路**：快指针每次两步，慢指针每次一步；相遇后，让一个指针回到头节点，两个指针都改为每次一步，再次相遇就是入口。

```python
def detectCycle(head):
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            p = head
            while p is not slow:
                p = p.next
                slow = slow.next
            return p

    return None
```

**入口定位原理**：设头到入口距离为 `a`、入口到相遇点的环内距离为 `b`、环长为 `L`。相遇时，快指针比慢指针多走了若干整圈，可推出 `a+b` 是 `L` 的整数倍，即 `a ≡ -b (mod L)`。因此，从头节点和相遇点各走 `a` 步，都会到达入口。相遇点到入口的路程可以包含多圈，不能简单认为它与头到入口的距离完全相等。

时间 `O(n)`，空间 `O(1)`。

#### 基础：普通链表反转

**原题链接**：[LeetCode 206 · 反转链表](https://leetcode.cn/problems/reverse-linked-list/)

**指针含义与反转步骤**

- `prev` 指向**已经反转好的部分的头节点**，不是尾节点。
- `cur` 指向下一个等待处理的节点。
- 一开始已反转部分为空，所以 `prev = None`。
- 每轮把 `cur` 接到已反转部分的最前面。

```python
def reverseList(head):
    prev = None
    cur = head

    while cur is not None:
        next_node = cur.next  # 先保存原来的下一站
        cur.next = prev       # 唯一真正改变节点连接的一句
        prev = cur            # 当前节点成为已反转部分的新头
        cur = next_node       # 去处理下一站

    return prev
```

例如原顺序为 `[1, 2, 3]`：

| 时刻 | 从 `prev` 开始的已反转部分 | 从 `cur` 开始的待处理部分 |
| --- | --- | --- |
| 开始 | 空 | `[1, 2, 3]` |
| 处理 1 后 | `[1]` | `[2, 3]` |
| 处理 2 后 | `[2, 1]` | `[3]` |
| 处理 3 后 | `[3, 2, 1]` | 空 |

若不先保存 `cur.next`，改完箭头就失去通往剩余链表的这条引用。不要把后三句中的变量赋值都理解成修改链表：真正改箭头的是 `cur.next = prev`。

#### 题 12：K 个一组反转链表

**原题链接**：[LeetCode 25 · K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

**题意**：每 `k` 个节点为一组反转，最后不足 `k` 个保持不变；必须修改节点连接，不能只交换数值。

示例：`[1, 2, 3, 4, 5]`，`k=2`，得到 `[2, 1, 4, 3, 5]`。

**思路**：找到完整的一组，保存下一组起点，按普通反转的四句处理 `k` 次，然后把前后两端接好。

| 引用 | 反转前的含义 | 反转后的角色 |
| --- | --- | --- |
| `group_prev` | 当前组前一个节点 | 需要接向新的组头 |
| `group_start` | 当前组第一个节点 | 新的组尾 |
| `kth` | 当前组第 k 个节点 | 新的组头 |
| `group_next` | 下一组起点 | 当前组处理完后接向它 |

```python
def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        # 先确认后面有完整的 k 个节点
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_start = group_prev.next
        group_next = kth.next

        # 反转这一组：先按普通链表反转理解
        prev = None
        cur = group_start
        for _ in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # prev 现在是新组头，group_start 现在是新组尾
        group_prev.next = prev
        group_start.next = group_next

        # 下一组前面的节点，就是当前组的新组尾
        group_prev = group_start
```

`dummy` 统一处理第一组，避免反转后需要单独更换头节点。这里先用 `prev=None`，最后显式接回后面；也可以一开始写 `prev=group_next`，但前者更贴近普通反转模板。

时间 `O(n)`，额外空间 `O(1)`。假设 `k >= 1`。

### 5. 二叉树

二叉树由「当前节点、左子树、右子树」组成，左右子树又具有相同结构，因此很多问题可以递归求解。

- **DFS**：先深入子树。前序适合向下传递信息，中序常用于 BST，后序适合先获得子树结果再计算当前节点。
- **BFS**：用队列逐层处理，适合层序遍历、按层统计和左右视图。
- **递归三步**：说明函数处理哪棵子树、空节点返回什么、当前节点如何利用左右子树的信息。

先区分函数是在「向结果列表追加内容」，还是「返回子树计算结果」。前者常用共享列表，后者依赖每层递归的返回值；两者不要混为一谈。

#### 节点定义与常见概念

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

| 概念 | 定义/注意事项 |
| --- | --- |
| 严格二叉树 | 每个节点有 0 或 2 个孩子，通常对应英文 Full Binary Tree |
| 满二叉树（国内教材常见含义） | 每层填满；所有叶子同层，非叶节点都有两个孩子；对应 Perfect Binary Tree |
| 完全二叉树 | 除最后一层外全满，最后一层从左向右连续排列 |
| 高度平衡二叉树 | 每个节点的左右子树高度差不超过 1；AVL 满足该条件 |
| 二叉搜索树 BST | 本笔记题目采用严格定义：左子树所有值 < 当前值 < 右子树所有值 |
| 二叉堆 | 完全二叉树 + 堆序；最小堆父节点不大于孩子，最大堆反之 |

**概念辨析**：仅仅「最后一层都是叶子」不足以定义满二叉树，因为任何有限树的最深层都是叶子。国内教材中的满二叉树强调所有层都填满；英文 Full Binary Tree 通常只要求每个节点有 0 或 2 个孩子，应与 Perfect Binary Tree 区分。

红黑树也常归为自平衡 BST，但不保证每个节点左右子树高度差都不超过 1；不能把 AVL 的严格高度差条件直接套到红黑树上。

#### DFS：三种遍历顺序

**对应练习**：[LeetCode 144 · 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)；[LeetCode 94 · 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)；[LeetCode 145 · 二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/)。递归和后面的迭代实现都可以用于这三道题。

| 遍历方式 | 处理顺序 | 访问当前节点的位置 |
| --- | --- | --- |
| 前序 | 根、左、右 | 两次递归之前 |
| 中序 | 左、根、右 | 两次递归之间 |
| 后序 | 左、右、根 | 两次递归之后 |

递归的核心是让左右子树重复做同一件事。这里把结果加进同一个列表，避免反复拼接大列表。

```python
def preorder_recursive(root):
    res = []

    def dfs(node):
        if node is None:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res

def inorder_recursive(root):
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res

def postorder_recursive(root):
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res
```

三者时间 `O(n)`，递归栈空间 `O(h)`。`res.append()` 修改列表内容，不给 `res` 重新赋值，因此不需要 `nonlocal res`。

**返回值与效率**：若递归函数通过列表拼接返回遍历结果，空节点必须返回 `[]`，不能返回 `None`。反复拼接在链状树上可能达到 `O(n²)` 时间；使用同一个结果列表并逐项 `append`，可避免重复复制。

#### DFS：迭代实现

**前序**：弹出节点立刻访问。栈后进先出，所以先压右孩子，再压左孩子。

```python
def preorder_iterative(root):
    if root is None:
        return []

    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return res
```

**中序**：先一路向左入栈，走到底后弹出访问，再进入右子树。即使 `cur` 为空，只要栈里还有节点，就没遍历结束。

```python
def inorder_iterative(root):
    res = []
    stack = []
    cur = root

    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    return res
```

**后序**：先生成「根、右、左」，反转结果就得到「左、右、根」。

```python
def postorder_iterative(root):
    if root is None:
        return []

    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    res.reverse()
    return res
```

这里用 `res.reverse()` 原地反转，避免 `res[::-1]` 再复制一份结果。三者时间 `O(n)`，不计结果的显式栈空间 `O(h)`。后序这种技巧适合输出遍历序列；若计算父节点时必须先得到孩子结果，不能把它当作已经真正完成了后序计算。

#### BFS：层序遍历

**原题链接**：[LeetCode 102 · 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

每轮开始时，队列里恰好是当前层的节点。先记住这一层的数量；处理过程中加入的孩子留给下一轮。

```python
from collections import deque

def levelOrder(root):
    if root is None:
        return []

    ans = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        ans.append(level)

    return ans
```

`for _ in range(len(queue))` 会在本轮循环开始前确定次数，不会随入队操作而变长。用 `level_size = len(queue)` 显式保存这一层的节点数，也能清楚地区分当前层和下一层。

时间 `O(n)`，队列空间 `O(w)`。Python 队列用 `deque.popleft()`；列表 `pop(0)` 需要移动后面的元素。

#### 题 13：路径总和 III

**原题链接**：[LeetCode 437 · 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)

**题意**：统计和为 `targetSum` 的向下路径。可以从任意节点开始、在任意节点结束，但只能沿父节点到子节点方向。

**思路**：把当前根到节点的路线当作一个数组，用「和为 K 的子数组」的前缀和计数；离开分支时撤销当前节点的前缀和。

```python
def pathSum(root, targetSum):
    prefix = {0: 1}

    def dfs(node, current_sum):
        if node is None:
            return 0

        current_sum += node.val
        count = prefix.get(current_sum - targetSum, 0)

        prefix[current_sum] = prefix.get(current_sum, 0) + 1
        count += dfs(node.left, current_sum)
        count += dfs(node.right, current_sum)

        # 只保留当前祖先路径的信息，避免串到别的分支
        prefix[current_sum] -= 1
        if prefix[current_sum] == 0:
            del prefix[current_sum]

        return count

    return dfs(root, 0)
```

例如根到当前节点依次为 `10、5、3`，目标为 `8`：当前和 `18`，查找之前前缀和 `18-8=10`，便发现路径 `5、3`。

**为什么必须回溯？** 左分支的前缀不能成为右分支的祖先前缀。共享的是 `prefix` 字典，所以需要加一、减一；`current_sum` 是每层自己的整数参数，不需要额外减回去。

这里删除计数为零的键，使表中只保留有效路径信息，时间 `O(n)`，递归栈和表空间 `O(h)`。若只将次数减为零而不删除键，结果仍正确，但零计数键会积累，表空间最坏为 `O(n)`。

#### 题 14：验证二叉搜索树

**原题链接**：[LeetCode 98 · 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)

**题意**：判断是否满足「每个节点左子树所有值更小，右子树所有值更大」。本题不允许重复值。

**思路**：BST 的中序遍历必须严格递增。一边遍历，一边与上一个访问值 `prev` 比较。

```python
def isValidBST(root):
    prev = None

    def inorder(node):
        nonlocal prev

        if node is None:
            return True

        if not inorder(node.left):
            return False

        if prev is not None and node.val <= prev:
            return False
        prev = node.val

        return inorder(node.right)

    return inorder(root)
```

**递归返回值怎么理解？**

- `if node is None: return True`：空树不会违反规则，是递归的结束条件。
- `if not inorder(node.left): return False`：先执行左边的检查；若已发现中序顺序不合法，整棵树立即判错。
- 在共享 `prev` 的实现中，递归检查还会与前面已访问的节点比较，不只是孤立地检查某一棵子树。
- `prev` 可能来自当前节点的左子树，也可能是更早访问的祖先；因此能够检查整个中序序列，而不只是直接比较父子。

**`nonlocal` 难点笔记**

`prev` 属于外层 `isValidBST()`，不是模块全局变量。内部所有递归调用都需要读写同一份「上次访问值」。

- `prev = node.val`：给变量名重新赋值，要写 `nonlocal prev` 才会修改外层那份。
- `res.append(x)`：只修改外层列表的内容，没有重新绑定 `res`，不需要 `nonlocal`。
- 只把 `prev` 当普通参数传入不够：左递归更新后的值还需要通过返回值传回当前层。
- `global prev` 指向模块全局变量，不适合这里的每次调用独立状态。完整例子见第 9 章。

中序遍历时直接检查相邻值是否严格递增，就能同时排除重复与逆序，无需额外统计频率或排序。

有的 BST 变体允许重复值，但必须遵循题目指定的规则；若规定重复值只能放右侧，单靠中序非递减还不足以验证该放置规则。本题统一采用严格 BST。

时间 `O(n)`，递归栈空间 `O(h)`。

#### 题 15：翻转二叉树

**原题链接**：[LeetCode 226 · 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

**题意**：将每个节点的左右孩子交换，返回根节点。

**思路**：访问一个节点就交换它的左右孩子，然后递归处理两棵子树。

```python
def invertTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
```

这是前序版本。把交换语句放到两次递归后，就是后序版本，也正确。改的是节点属性，所以上面的递归调用不必再接收返回值。

时间 `O(n)`，空间 `O(h)`；会直接修改原树。

#### 题 16：二叉树的右视图

**原题链接**：[LeetCode 199 · 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/)

**题意**：从右边看树，按从上到下的顺序返回每一层能看到的节点值。

**思路**：BFS 从左到右处理每一层，记录最后一个节点。

```python
from collections import deque

def rightSideView(root):
    if root is None:
        return []

    ans = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                ans.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return ans
```

**右视图的含义**：每层取最右侧实际存在的节点，因此左孩子也可能出现在结果中。不能只沿着 `right` 指针查找。

例如 `1` 的左孩子是 `2`，`2` 的右孩子是 `3`，三层分别只有 `1、2、3`，结果就是 `[1, 2, 3]`。不同层不会互相遮挡。

时间 `O(n)`，队列空间 `O(w)`。

### 6. 图论

图由节点和边组成。与树相比，图中可能存在环，同一个节点也可能通过多条路径到达，因此遍历时通常需要记录已访问状态。

- **DFS**：沿一个方向深入，再返回探索其他分支；可用递归或栈实现。
- **BFS**：使用队列逐层扩展；在无权图中可用于求最少边数。
- **连通分量计数**：遍历所有节点，每遇到一个未访问节点，就启动一次搜索，并把该连通区域全部标记。

网格也是一种图：陆地格子是节点，上下左右的邻接关系是边，岛屿就是陆地的连通分量。要在递归深入前或入队时标记，避免重复访问。

#### 题 19：岛屿数量——DFS

**原题链接**：[LeetCode 200 · 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

**题意**：网格中字符串 `"1"` 是陆地、`"0"` 是水；上下左右相连的陆地组成一座岛屿，求岛屿数量，对角线不算相连。

示例：`[["1","1","1"],["0","1","0"],["1","0","0"],["1","0","1"]]`，有 `3` 座岛。

**思路**：遍历网格，每遇到一块未访问陆地就计数一次，并用 DFS 标记它连通的整座岛。

```python
def numIslands_dfs(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return
        if grid[r][c] != "1":
            return

        grid[r][c] = "0"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count
```

标记必须在继续搜索之前完成，否则相邻格子可能互相递归。这里**不恢复为 `"1"`**：已经统计的陆地应保持已访问，不像全排列要撤销选择。

时间 `O(rows×cols)`，递归栈最坏 `O(rows×cols)`。大块或长条陆地可能触及 Python 递归深度限制，实际提交时 BFS 更稳妥。

#### 题 20：岛屿数量——BFS

**原题链接**：[LeetCode 200 · 岛屿数量](https://leetcode.cn/problems/number-of-islands/)（与题 19 为同一道原题，这里练习 BFS 写法。）

**题意相同**，这次用队列向四周扩散。

```python
from collections import deque

def numIslands_bfs(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = "0"

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == "1"
                ):
                    # 入队时就标记，避免同一格子重复入队
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                bfs(r, c)

    return count
```

这里不需要 `level_size`，因为只要访问整个连通区域，无需输出每层或计算距离。时间 `O(rows×cols)`，队列空间上界 `O(rows×cols)`。

两种代码都会修改网格。若要保留输入，可以使用额外 `visited`，或者调用前按行复制：`working = [row[:] for row in grid]`。

### 7. 回溯算法

回溯是在逐步构造答案：做选择，递归尝试下一步，回来后撤销选择，再尝试其他选择。适合枚举排列、组合，以及满足约束的放置方案。

写代码前明确四件事：**当前路径、可选项、结束条件、需要恢复的状态**。不符合约束的分支提前跳过，称为剪枝。

**Python 风格伪代码**（`is_complete`、`get_choices`、`is_valid` 表示题目相关的判断，需要按具体问题实现）：

```python
def backtrack(path):
    if is_complete(path):          # 已构成一个完整答案
        ans.append(path.copy())   # 保存快照
        return

    for choice in get_choices(path):
        if not is_valid(path, choice):
            continue              # 剪枝：跳过不合法选择

        path.append(choice)       # 做选择
        # 若维护 used、列集合等状态，也在这里标记
        backtrack(path)           # 递归构造下一步
        path.pop()                # 撤销选择
        # 将本层新增的标记一并恢复
```

`ans` 是外围的结果列表；`path` 记录当前方案。每次递归返回后，都要把本层修改恢复到尝试该选择之前的状态，再试下一个选项。

- 全排列：递归深度对应已填的位置数，可选项是尚未使用的数字。
- N 皇后：递归深度对应行号，可选项是这一行满足列和对角线约束的位置。
- 普通图遍历中的 `visited` 通常不撤销；回溯中的 `used` 描述当前方案，返回时通常需要撤销。

若只要求方案数量或最优值，不一定要把所有方案保存下来；当不同路径重复遇到相同子问题时，还可考虑记忆化搜索或动态规划。

#### 题 17：全排列

**原题链接**：[LeetCode 46 · 全排列](https://leetcode.cn/problems/permutations/)

**题意**：给定没有重复数字的数组，返回所有全排列，结果顺序任意。

示例：`[1,2,3]` 有 `6` 种排列，包括 `[1,2,3]`、`[1,3,2]` 等。

**思路**：每个位置选一个尚未使用的数字。`path` 记录当前排列，`used[i]` 记录下标 `i` 是否已在当前排列中使用。

```python
def permute(nums):
    n = len(nums)
    ans = []
    path = []
    used = [False] * n

    def backtrack():
        if len(path) == n:
            ans.append(path.copy())
            return

        for i in range(n):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return ans
```

**理解要点**

- `ans.append(path)` 保存的是同一个列表引用，后面 `path.pop()` 会改变已保存内容。`path.copy()` 或 `path[:]` 才是保存当前排列。
- `path` 只操作末尾，使用 `list.append/pop` 即可，没必要换成 `deque`。
- `used[i]` 是本条路径上的状态，回来必须恢复。否则其他排列也无法再使用这个数字。
- `path.append()`、`used[i] = True` 都只是修改容器内容，不需要 `nonlocal`。

时间 `O(n×n!)`，共 `n!` 个答案，每个复制 `O(n)`；不计答案，空间 `O(n)`。

#### 题 18：N 皇后

**原题链接**：[LeetCode 51 · N 皇后](https://leetcode.cn/problems/n-queens/)

**题意**：在 `n×n` 棋盘放 `n` 个皇后，使任意两个不同排、不同列、不同对角线；返回所有方案，`Q` 表示皇后，`.` 表示空位。

**思路**：从 `row=0` 开始，每行恰好选一列，合法就递归下一行。每行只放一个，自然避免行冲突。

| 冲突类型 | 集合保存什么 | 原因 |
| --- | --- | --- |
| 同一列 | `col` | 列下标相同 |
| 左上到右下的对角线 | `row-col` | 例如 `(0,0)、(1,1)、(2,2)` 的差都为 0 |
| 右上到左下的对角线 | `row+col` | 例如 `(0,2)、(1,1)、(2,0)` 的和都为 2 |

```python
def solveNQueens(n):
    ans = []
    board = [["."] * n for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            ans.append(["".join(line) for line in board])
            return

        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue

            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return ans
```

**递归过程**：依次确定每一行皇后所在的列。下一行无处可放时，返回上一行，撤销该行的选择并尝试其他列。找到完整方案后仍需回溯，才能枚举全部方案。

`ans.append(["".join(line) for line in board])`：每一行字符拼成字符串，再把整个方案加入答案。例如得到：

```python
one_solution = [".Q..", "...Q", "Q...", "..Q."]
all_solutions = [one_solution]
```

拼接生成的新字符串不会随之后的棋盘修改而变化。不能直接把可变的 `board` 加入答案。

设合法方案数为 `S`。此实现的一个保守时间上界是 `O(n×n! + S×n²)`：每个搜索状态尝试 `n` 列，保存每个棋盘要 `O(n²)`；实际搜索受到对角线剪枝。辅助空间 `O(n²)`，主要是棋盘；返回方案空间 `O(S×n²)`。

### 8. 动态规划

动态规划把重复出现的子问题计算一次并保存结果，再利用这些结果构造更大的问题。常见目标是求方案数、最大或最小值，以及判断是否可行。

**写 DP 的五步**：

1. **定义状态**：用一句完整的话说明 `dp` 的含义，包括考虑的范围，以及是否必须选择某个元素。
2. **推导转移**：按最后一步或当前选择分类，列出所有合法来源。
3. **确定初值**：从空问题、一个元素等最小规模出发，区分可达与不可达状态。
4. **安排顺序**：先算依赖项，再算当前状态；顺序由转移关系决定。
5. **确定答案**：判断应返回末尾状态、所有状态的最大值，还是某个指定状态。

**根据题目选择状态**：

| 问题 | 状态抓住什么 | 转移的主要依据 |
| --- | --- | --- |
| 爬楼梯 | 到达第 `i` 阶的方法数 | 最后一步爬 1 阶或 2 阶，两类方法数相加 |
| 打家劫舍 | 前 `i+1` 间房的最大金额 | 不选当前房，或选当前房并跳过相邻房 |
| 最长递增子序列 | 必须以 `nums[i]` 结尾的最长长度 | 枚举能接到当前元素前面的较小元素 |
| 0/1 背包 | 前 `i` 件物品、容量 `w` 的最大价值 | 当前物品不选或选一次，来源均在上一行 |
| 完全背包 | 前 `i` 种物品、容量 `w` 的最大价值 | 选当前物品后，仍可使用当前种类 |
| 股票买卖 | 第 `i` 天末持仓或不持仓的最佳现金状态 | 不操作、买入或卖出；交易次数限制体现在合法来源中 |

**容易迁移到其他题的技巧**：

- **“前 i 个”与“以 i 结尾”不同。** 打家劫舍允许不选当前房，所以答案在末尾状态；LIS 必须以当前元素结尾，最长序列可能在更早的位置结束，所以返回 `max(dp)`。
- **运算对应目标。** 不重叠的方案分类通常相加；最大收益取 `max`，最小代价取 `min`，可行性用逻辑“或”。统计方案时要避免重复计算同一方案。
- **初值没有万能的 0。** 爬楼梯的空方案数为 `1`；LIS 每个元素单独成序列，初值为 `1`；股票首次持仓为负买入价。要求恰好达到目标时，不可达状态应单独表示，不能当成已完成的零价值方案。
- **状态要包含影响后续选择的信息。** 股票题只记录“今天赚了多少”还不够，还需区分是否持仓；背包题还需记录剩余或可用容量。
- **空间压缩放在推导之后。** 先写清二维或完整数组转移，再考虑只保存必要状态。0/1 背包一维容量倒序是为了读取上一轮；完全背包正序是为了允许本轮重复使用。滚动变量更新时要保留仍会用到的旧值。

两层循环不一定代表同一种关系：LIS 内层在枚举前驱，背包内层在枚举容量。先说清楚每个循环变量的含义，再确定遍历范围。

#### 题 21：爬楼梯

**原题链接**：[LeetCode 70 · 爬楼梯](https://leetcode.cn/problems/climbing-stairs/)

**题意**：每次爬 1 或 2 阶，到第 `n` 阶有多少种走法？顺序不同算不同方案。

`dp[i]` 表示到达第 `i` 阶的方法数。最后一步只能从 `i-1` 爬 1 阶，或从 `i-2` 爬 2 阶；两类不重叠，因此相加。

```python
def climbStairs(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

`dp[0]=1` 表示空走法：站在底部不走，算一种完成 0 阶的方式。`n=3` 的三种方案是 `1+1+1`、`1+2`、`2+1`。

只依赖前两项，也可压缩空间：

```python
def climbStairs_compact(n):
    prev2 = prev1 = 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1
```

时间 `O(n)`；数组版空间 `O(n)`，压缩版 `O(1)`。输入假设 `n>=0`，原题通常要求 `n>=1`。

#### 题 22：打家劫舍

**原题链接**：[LeetCode 198 · 打家劫舍](https://leetcode.cn/problems/house-robber/description/)

**题意**：一排房屋各有非负金额，不能选择相邻房屋，求最大总金额。

`dp[i]` 表示考虑下标 `0～i` 的所有房屋时的最大金额，**不要求一定选择第 i 间**。

- 不选 `i`：答案是 `dp[i-1]`。
- 选 `i`：不能选 `i-1`，答案是 `dp[i-2] + nums[i]`。

```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]
```

例如 `[1,2,3,1]`，`dp=[1,2,4,4]`，选下标 `0、2`，金额为 `4`。

空间优化：

```python
def rob_compact(nums):
    prev2 = prev1 = 0
    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current
    return prev1
```

时间 `O(n)`；数组版空间 `O(n)`，压缩版 `O(1)`。

#### 题 23：最长递增子序列 LIS

**原题链接**：[LeetCode 300 · 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

**题意**：求最长严格递增子序列的长度。子序列可以不连续，但不能改变原来的相对顺序。

示例：`[10,9,2,5,3,7,101,18]` 的答案为 `4`，例如 `[2,3,7,18]`。

**状态很关键**：`dp[i]` 表示**必须以 `nums[i]` 结尾**的 LIS 长度。

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1) #dp[i]可能会经过多次更新
        return  max(dp)
```

**循环顺序：外层 i、内层 j。**

- 外层固定「以谁结尾」，从左往右保证前面的 `dp[j]` 已计算好。
- 内层 `range(i)` 枚举 `0～i-1`，找所有能接到当前数之前的位置。
- 只有 `nums[j] < nums[i]` 才能接上，再比较 `dp[j]+1` 谁更长。
- 不能使用 `i` 后面的元素作为前一个元素，否则破坏原数组顺序。
- `i=0` 没有前驱，保留初始值 `1`；所以从 `1` 开始即可。

例如 `[2,5,3,7]`：`dp=[1,2,2,3]`。最后返回 `max(dp)`，因为全局最优不一定以最后一个数结尾。

时间 `O(n²)`，空间 `O(n)`。该题还可用贪心 + 二分优化至 `O(n log n)：`

> 对于相同长度的递增子序列，**结尾越小越好**，因为更容易接上后续元素。因此用 `tails[k]` 记录长度为 `k+1` 的递增子序列中最小的结尾值。
> 

```python
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[k]：在所有长度为 k+1 的递增子序列中，
        # 结尾元素所能取得的最小值
        tails = []

        for x in nums:
            # 找到 tails 中第一个 >= x 的位置
            i = bisect_left(tails, x)

            if i == len(tails):
                # x 比当前所有结尾值都大，可以扩展出更长的递增子序列
                tails.append(x)
            else:
                # 用 x 更新该长度下的最小结尾值
                tails[i] = x

        return len(tails)
```

#### 题 24：0/1 背包

**对应练习（背包变体）**：[LeetCode 416 · 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)。

本节讲的是通用的「重量、价值、容量」最大价值模板；这道练习则判断能否选出总和为数组总和一半的元素，每个元素最多选一次。它练习同一类 0/1 背包思想，但不是本节题意完全相同的原题，提交时需要调整状态与返回值。

**题意**：给定物品重量、价值以及背包容量，每个物品最多选一次，求总重量不超过容量的最大价值。

这里约定重量为正整数、容量为非负整数，允许不选物品；不是要求恰好装满。

`dp[i][w]`：只考虑前 `i` 个物品，容量上限为 `w` 时的最大价值。第 `i` 个物品的数组下标是 `i-1`。

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]  # 不选当前物品
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weight] + value
                )

    return dp[n][capacity]
```

选当前物品后，剩余容量 `w-weight`，再从**前 i-1 个物品**中选择，保证不能再选当前这一件。`dp[0][w]=0` 表示没有物品；正重量前提下，`dp[i][0]=0`。

例：重量 `[1,3,4]`、价值 `[15,20,30]`、容量 `4`，最优选重量 `1+3`，价值 `35`。

一维优化：

```python
def knapsack_01_compact(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]
```

**为什么容量倒序？** 保证读取的 `dp[w-weight]` 还没有在当前这一轮更新，仍代表「不包含当前物品」的上一轮状态。

反例：只有重量 `2`、价值 `3` 的一件物品，容量 `4`。若正序更新，先把 `dp[2]` 变成 `3`，再用它把 `dp[4]` 变成 `6`，就把同一件物品用了两次。

二维时间/空间均为 `O(nW)`；一维时间 `O(nW)`、空间 `O(W)`，其中 `W=capacity`。

#### 题 25：完全背包（无限背包）

**对应练习（背包变体）**：[LeetCode 322 · 零钱兑换](https://leetcode.cn/problems/coin-change/)；[LeetCode 518 · 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/)。

本节模板求最大价值；322 题求凑出指定金额的最少硬币数，518 题求组合数。三者都允许同一种物品重复使用，但状态定义、初始化和转移目标不同，不能直接提交本节的最大价值代码。

**题意**：与 0/1 背包相同，但每种物品可以重复选择任意多次。仍假设重量为正整数。

关键变化：选当前物品后，还能在**前 i 种物品**中继续选，包括当前种类。

```python
def knapsack_unbounded(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i][w - weight] + value
                )

    return dp[n][capacity]
```

一维优化：

```python
def knapsack_unbounded_compact(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for w in range(weight, capacity + 1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]
```

| 题型 | 二维「选择」分支 | 一维容量顺序 | 目的 |
| --- | --- | --- | --- |
| 0/1 背包 | `dp[i-1][w-weight]+value` | 从大到小 | 不能重复选当前物品 |
| 完全背包 | `dp[i][w-weight]+value` | 从小到大 | 允许使用本轮结果，再选一次 |

例：重量 `[2,3]`，价值 `[3,4]`，容量 `7`，选 `2+2+3`，价值 `10`。

时间 `O(nW)`；二维空间 `O(nW)`，一维空间 `O(W)`。注意「容量倒序/正序」的这个对比针对物品在外层的一维模板；不能把规则不加区分地套到所有二维写法上。

#### 股票 DP 先理解的两件事

1. `dp[i][0]`、`dp[i][1]` 是**不同候选方案各自的最优结果**，不是同一条实际交易记录。更新 `hold` 不表示现实中把已经发生的买入改掉，而是在比较「当初选择哪天买更好」。
2. 以初始现金为 `0` 记账：买入扣钱、卖出加钱。持仓状态记录的是累计现金变化，**没有加上手中股票的市值**，所以会出现负数。这是算法状态，不是现实账户余额要求。

#### 题 26：买卖股票一次

**原题链接**：[LeetCode 121 · 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

**题意**：给定每日价格，最多买入一次并在之后卖出一次；不能获利时可以不交易，返回 `0`。

| 状态 | 含义 |
| --- | --- |
| `dp[i][0]` | 第 i 天末不持仓的最大收益：从未交易，或已经完成一次交易 |
| `dp[i][1]` | 第 i 天末持仓的最大现金变化：只买入过一次，尚未卖出 |

```python
def maxProfit_once_dp(prices):
    if not prices:
        return 0

    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = -prices[0]

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],                # 已不持仓，今天不操作
            dp[i - 1][1] + prices[i]     # 昨天持仓，今天卖出
        )
        dp[i][1] = max(
            dp[i - 1][1],                # 继续持有
            -prices[i]                   # 今天才第一次买入
        )

    return dp[-1][0]
```

**如何保证最多一次交易？**

- 卖出公式中的 `dp[i-1][1]` 已限定为「只买过一次，还未卖」，加今天价格只完成一次交易。
- 买入公式只能从 `0-prices[i]` 开始，不从 `dp[i-1][0]-prices[i]` 开始，所以不能接上之前卖出的利润再买。
- 只看卖出公式无法判断交易次数，必须与买入公式及状态定义一起看。

例：价格 `[7,1,5]`：

| 天数（下标） | 价格 | 持仓最优状态 | 不持仓最优收益 |
| --- | --- | --- | --- |
| 0 | 7 | -7 | 0 |
| 1 | 1 | -1 | 0 |
| 2 | 5 | -1 | 4 |
- `1` 表示选择在价格 `1` 的那天首次买入；最后卖出得到 `1+5=4`。两个状态是在同时比较不同方案，不是在同一天真的既持仓又空仓。

**这题更直接的写法：维护历史最低价。**

```python
def maxProfit_once(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
```

`min_price` 来自到今天为止的价格。若最低价恰好是今天，算出 `0`，相当于不交易，不会产生错误的正利润；任何正利润都来自更早的低价。

不要用 `max(prices)-min(prices)`，因为全局最高价可能发生在最低价之前。

两种时间都为 `O(n)`；二维 DP 空间 `O(n)`，最低价写法空间 `O(1)`。

#### 题 27：买卖股票多次

**原题链接**：[LeetCode 122 · 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

**题意**：可以多次买卖，但同一时间最多持有一股。此基础题没有手续费、冷冻期等额外限制。

卖出公式不变；买入时允许使用之前已经获得的收益。

```python
def maxProfit_many_dp(prices):
    if not prices:
        return 0

    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = -prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

    return dp[-1][0]
```

买入只能从昨天**不持仓**的状态来，卖出只能从昨天**持仓**的状态来，因此不会同时持有多股。

| 版本 | 今天买入的候选状态 |
| --- | --- |
| 最多一次交易 | `-prices[i]` |
| 不限交易次数 | `dp[i-1][0] - prices[i]` |

例如 `[1,5,3,6]`：卖出第一笔后赚 `4`，再以 `3` 买入，持仓现金状态为 `4-3=1`；再以 `6` 卖出，总收益为 `7`。持仓状态可以为正，但它仍没有包含手中股票的市值。

**贪心：累加相邻两天的所有正差价。**

```python
def maxProfit_many(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```

**收益分解**：累加正差价是在计算可实现的总收益，不必对应每天实际买卖。连续上涨 `1、3、6` 的收益满足：

`(3-1) + (6-3) = 6-1 = 5`

实际可以价格 `1` 买、价格 `6` 卖；按天累加的答案相同。多个连续上涨区间分别合并为谷底买、峰顶卖即可实现。题目给出了完整价格数组，是求已知数组上的最优值，不是要求仅凭过去价格在线预测。

例：`[1,3,6,4,7]` 的利润为 `2+3+3=8`，对应两笔交易 `1→6`、`4→7`。

贪心的适用条件是本题的无限次交易、无手续费、无冷冻期；有额外约束时不能直接照搬。时间 `O(n)`，空间 `O(1)`；二维 DP 时间 `O(n)`，空间 `O(n)`。

## 第二部分：Python 语法糖与其他技巧

### 9. Python 语法糖与常用工具

#### 9.1 lambda 与排序规则

`lambda 参数: 表达式` 表示一个简短函数。

```python
pairs = [(1, 3), (2, 2), (4, 1)]
pairs.sort(key=lambda x: x[1])
# [(4, 1), (2, 2), (1, 3)]

# 第一项升序，第一项相同时第二项降序
pairs.sort(key=lambda x: (x[0], -x[1]))
```

`lambda x: x[1]` 表示对每个元素取第二项作为排序依据。

```python
nums = [3, 1, 2]
ordered = sorted(nums)  # 返回新列表，不修改 nums
nums.sort()            # 修改原列表，返回 None
nums.sort(reverse=True)  # 降序
```

不要写 `nums = nums.sort()`，否则变量会变成 `None`。

#### 9.2 列表、集合、字典推导式

```python
squares = [x * x for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

unique = {x for x in [1, 2, 2, 3]}
# {1, 2, 3}，集合不保证排序

mapping = {x: x * 2 for x in range(3)}
# {0: 0, 1: 2, 2: 4}

grid = [[0] * 3 for _ in range(2)]
# 两个独立的行列表
```

二维列表不要写 `[[0] * cols] * rows`：这样每一行引用同一个列表，改一个位置可能连其他行一起改。

#### 9.3 enumerate 与 zip

```python
nums = [10, 20, 30]
indexed = list(enumerate(nums))
# [(0, 10), (1, 20), (2, 30)]

numbered = list(enumerate(nums, start=1))
# [(1, 10), (2, 20), (3, 30)]

weights = [1, 3, 4]
values = [15, 20, 30]
items = list(zip(weights, values))
# [(1, 15), (3, 20), (4, 30)]
```

`enumerate(..., start=1)` 改的是生成的编号，不改变原列表下标。`zip` 默认到最短的输入结束，所以背包中的重量表与价值表应等长。

#### 9.4 切片、复制与 join

```python
a = [1, 2, 3, 4]
copy1 = a[:]
copy2 = a.copy()
reversed_a = a[::-1]
middle = a[1:3]  # [2, 3]，左闭右开

chars = [".", "Q", ".", "."]
row_string = "".join(chars)  # ".Q.."
```

- `path.copy()` 是浅复制，但路径里是整数时已经够用。
- 二维列表 `board.copy()` 只复制外层，行列表仍然共享；按行复制用 `[row[:] for row in board]`。
- `a.reverse()` 原地反转并返回 `None`；`a[::-1]` 创建倒序的新列表。
- `ans.append(solution)` 把整个方案作为一项加入；`ans.extend(solution)` 会把方案中的各项逐个加入，结构不同。

#### 9.5 `None`、`not`、`is` 与短路判断

```python
node = None
is_empty = node is None  # True

valid = False
invalid = not valid     # True

items = []
empty_list = not items  # True
```

- 对本笔记的普通树节点，`if not node` 表示没有节点，写成 `if node is None` 更明确；节点的 `val=0` 不等于节点不存在。
- `if not dfs(...)` 是先调用函数，再判断它返回的结果是否为假。
- `is` 比较是否为同一个对象，适合 `None` 和节点身份判断；数值相等使用 `==`。
- `or` 遇真停止，`and` 遇假停止。例如 `first == n or nums[first] != target`：当 `first==n` 时不会再访问越界位置。
- `return` 省略返回值时，实际返回 `None`；如果需要布尔值、列表或计数，要明确返回 `True/False`、`[]`、`0` 等。

#### 9.6 nonlocal：为什么 prev 要声明，而 res.append 不用？

Python 在函数中看到对变量名赋值，默认认为它是该函数的局部变量。要重新绑定外层函数的同名变量，使用 `nonlocal`。

```python
def scope_example():
    prev = None
    res = []

    def dfs(value):
        nonlocal prev
        prev = value       # 修改外层变量名的绑定
        res.append(value)  # 修改列表内容，无需 nonlocal res

    dfs(1)
    dfs(2)
    return prev, res       # (2, [1, 2])
```

这里 `prev`、`res` 都属于外层函数，不是全局变量。所有内部调用访问同一份外层状态，每次重新调用 `scope_example()` 又有新的一份。

| 在内部函数中的操作 | 要修改外层变量时是否需要 nonlocal | 原因 |
| --- | --- | --- |
| 只读取 `prev` | 不需要 | 可以沿作用域向外查找 |
| `prev = x` | 需要 | 重新绑定变量名 |
| `count += 1` | 需要 | 会给变量名赋值 |
| `res.append(x)` / `res.pop()` | 不需要 | 改列表内容 |
| `res[0] = x` | 不需要 | 改列表元素 |
| `freq[x] += 1` | 不需要 | 改字典条目 |
| `res = []` | 需要 | 让外层变量改为指向新列表 |
| `res += [x]` | 需要 | 即使列表支持原地加，语法仍会赋值给变量名 |

**global 与 nonlocal**：`global` 指模块层变量；`nonlocal` 指外围函数的已有变量。若内部函数自己需要给全局变量赋值，也要在内部声明 `global`，外层的声明不会自动替它声明。仅在模块层定义 `x`，不能在函数中声明 `nonlocal x`；`nonlocal` 必须能找到外围函数中的已有绑定，否则会产生语法错误。

不写 `nonlocal prev` 却先读取、后赋值 `prev`，会因局部变量尚未赋值而报 `UnboundLocalError`。是否需要它，取决于**重新绑定变量名**，不是简单取决于是否递归、是否可变类型。

#### 9.7 Counter：统计频率

```python
from collections import Counter

counts = Counter("aabbbcc")
b_count = counts["b"]  # 3
missing_count = counts["z"]  # 0
```

`Counter` 适合字符/数字计数；不存在的键用下标读取时返回 `0`。`len(counts)` 是保存的键种类数，不是元素总数。

#### 9.8 defaultdict：访问缺失键时创建默认值

```python
from collections import defaultdict

graph = defaultdict(list)
graph[0].append(1)
graph[0].append(2)
# graph[0] 是 [1, 2]

frequency = defaultdict(int)
frequency["a"] += 1
# int() 默认得到 0
```

使用 `list`、`int` 这类可调用工厂，而不是 `list()`。`d[key]` 访问缺失键时会生成并保存默认值；`d.get(key, default)` 不会插入缺失键。

#### 9.9 deque：双端队列

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)       # [1, 2, 3, 4]
q.appendleft(0)   # [0, 1, 2, 3, 4]
right_item = q.pop()       # 4
left_item = q.popleft()    # 0
```

两端插入/删除均为 `O(1)`。回溯路径、普通栈用 `list`；BFS、单调队列用 `deque`。

#### 9.10 heapq：堆与 heapify

```python
import heapq

heap = [5, 3, 8, 1, 2]
heapq.heapify(heap)  # 原地建最小堆；正确拼写是 heapify

smallest = heap[0]           # 查看最小值，1
heapq.heappush(heap, 0)      # 加入一个元素
removed = heapq.heappop(heap)  # 弹出当前最小值，0
```

| 操作 | 作用 | 时间 |
| --- | --- | --- |
| `heapq.heapify(heap)` | 原地把列表变为最小堆 | `O(n)` |
| `heapq.heappush(heap, x)` | 插入 | `O(log n)` |
| `heapq.heappop(heap)` | 删除并返回最小值 | `O(log n)` |
| `heap[0]` | 查看最小值 | `O(1)` |

**易错点**

- `heapq` 直接 `import heapq`，不是从 `collections` 导入。
- `heapify` 返回 `None`，不能写 `heap = heapq.heapify(heap)`。
- 堆不是完全排序的列表，`heap[-1]` 不保证是最大值。
- 一次 `heapify` 是 `O(n)`；逐个 `heappush` 建堆的最坏总时间是 `O(n log n)`。建堆的大多数节点都在底部，只需很少下沉。

兼容常见 Python 环境的最大堆技巧：所有值先取负，取出时再取负还原，不能把正负两种表示混进同一个堆。

```python
import heapq

max_heap = [-x for x in [3, 1, 2]]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)  # 3
```

#### 9.11 range、整除与取模

```python
forward = list(range(4))          # [0, 1, 2, 3]
backward = list(range(3, -1, -1)) # [3, 2, 1, 0]
half = 7 // 2                    # 3，向下取整
wrapped = -1 % 5                 # 4
```

`range(start, stop, step)` 不包含 `stop`。倒序遍历到下标 `0`，应把 `stop` 写为 `-1`；循环下标用 `i % n`，前提是 `n>0`。

### 10. 排序算法

**综合练习**：[LeetCode 912 · 排序数组](https://leetcode.cn/problems/sort-an-array/)。该题要求手写排序并达到 `O(n log n)` 时间，可用本章归并排序练习；冒泡、选择排序用于理解基础过程，不满足该题的时间复杂度要求。

题目不要求手写时，可直接用 `nums.sort()` 或 `sorted(nums)`。以下实现用于理解原理。冒泡和选择会修改原列表；归并、下面的快排和堆排序返回新列表。

#### 10.1 冒泡排序

**原理**：相邻元素比较并交换，每轮把未排序部分的最大值送到右端。某轮没有交换时，说明已经有序。

```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
```

最好时间 `O(n)`，平均/最坏 `O(n²)`；空间 `O(1)`，稳定。

#### 10.2 选择排序

**原理**：每一轮从未排序部分选最小值，与当前待填位置交换。

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```

时间 `O(n²)`，空间 `O(1)`，不稳定。

#### 10.3 归并排序

**原理**：分成两半，各自排序，再用两个指针把两个有序列表合并。相等时先取左侧，保持稳定性。

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums.copy()

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

时间 `O(n log n)`，峰值辅助空间 `O(n)`。递归深度 `O(log n)`，稳定。

#### 10.4 快速排序：易读的三路列表版

**原理**：选一个基准值，把元素分成小于、等于、大于它的三组，递归排序左右两组。

```python
def quick_sort(nums):
    if len(nums) <= 1:
        return nums.copy()

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

平均时间 `O(n log n)`，最坏 `O(n²)`。取中间**下标**不代表取到了数值中位数，仍可能划分不平衡。

这份易读实现不是原地快排：创建了额外列表，平衡划分时峰值空间 `O(n)`，极端不平衡时保留的递归列表可能达到 `O(n²)`，也可能遇到递归深度限制。

稳定性要区分实现：常规原地交换版快排通常不稳定；这里按原顺序筛出三组，相等项的先后顺序会保留，不能直接把「快排不稳定」不加说明地套到这份代码。

#### 10.5 堆排序：heapq 版

**原理**：先建最小堆，再不断取出最小值，得到升序结果。

```python
import heapq

def heap_sort(nums):
    heap = nums.copy()
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]
```

`range(len(heap))` 在开始前已经确定次数，所以后面堆不断变短也没问题。

建堆 `O(n)`，全部弹出 `O(n log n)`；总时间 `O(n log n)`，这份实现额外空间 `O(n)`。传统原地堆排序可用 `O(1)` 辅助空间，但不是这段写法。普通堆排序不保证相等键的原顺序。

#### 10.6 对照表

| 算法 | 核心动作 | 平均时间 | 最坏时间 | 本文实现辅助空间 |
| --- | --- | --- | --- | --- |
| 冒泡 | 相邻交换 | `O(n²)` | `O(n²)` | `O(1)` |
| 选择 | 每轮选最小 | `O(n²)` | `O(n²)` | `O(1)` |
| 归并 | 分治后合并 | `O(n log n)` | `O(n log n)` | `O(n)` |
| 快排 | 按基准分组 | `O(n log n)` | `O(n²)` | 平均 `O(n)`，最坏 `O(n²)` |
| heapq 堆排 | 不断取堆顶 | `O(n log n)` | `O(n log n)` | `O(n)` |

稳定排序是指：排序键相同的元素，排序后仍保持原来的相对顺序。

### 11. 二分查找

二分需要一个能安全排除半边的规则。对升序数组而言，与中间元素比较即可决定方向。

#### 11.1 普通二分：找任意一个目标

**原题链接**：[LeetCode 704 · 二分查找](https://leetcode.cn/problems/binary-search/description/)

使用闭区间 `[left, right]`，所以循环条件是 `left <= right`。当只剩一个位置时也要检查。

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

时间 `O(log n)`，空间 `O(1)`；空数组循环不执行，返回 `-1`。

#### 11.2 例题：在排序数组中查找元素的第一个和最后一个位置

**原题链接**：[LeetCode 34 · 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

**题意**：给定非递减数组和目标值，返回目标的首尾下标；不存在则返回 `[-1,-1]`，要求对数时间。

示例：`[5,7,7,8,8,10]`，目标 `8`，返回 `[3,4]`。

**与普通二分的差别**：遇到相等也不能立即返回，因为可能还有更靠左或更靠右的同值元素。

分别进行两次边界查找：

| 搜索目标 | 判断条件 | 条件满足时 | 最后得到什么 |
| --- | --- | --- | --- |
| 第一个 `>= target` 的位置 | `nums[mid] >= target` | `right = mid-1` | `left` 是左边界候选 |
| 第一个 `> target` 的位置 | `nums[mid] > target` | `right = mid-1` | `left-1` 是最后一个目标的位置（目标存在时） |

```python
def searchRange(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    # 第一次：找第一个 >= target 的位置
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    first = left
    if first == n or nums[first] != target:
        return [-1, -1]

    left, right = 0, n - 1

    # 第二次：找第一个 > target 的位置
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return [first, left - 1]
```

相关说明可以参考
[https://app.notion.com/p/fikry102/labuladong-Hot100-3c5ecda0f71f80fbb916d541f13db55f?source=copy_link#3dbecda0f71f80468d97f31a7c1121f9](https://app.notion.com/p/labuladong-Hot100-3c5ecda0f71f80fbb916d541f13db55f?pvs=21)

设 $N=\mathrm{len}(nums)$，定义哨兵 $nums[-1]=-\infty,\ nums[N]=+\infty$。整个二分过程中，始终有：$l$ 左侧元素均满足 $nums[i]<target$，$r$ 右侧元素均满足 $nums[i]\ge target$。

第一次二分始终保持：`left` 左侧都 `< target`，`right` 右侧都 `>= target`。循环结束时 `left = right + 1`，因此 `right` 正好位于 `left` 左边一位，有 `nums[right] < target <= nums[left]`，所以 `left` 是第一个 `>= target` 的位置；若 `target` 存在，就是第一个 `target`。

第二次二分始终保持：`left` 左侧都 `<= target`，`right` 右侧都 `> target`。循环结束时同样有 `left = right + 1`，因此有 `nums[right] <= target < nums[left]`，所以 `left` 是第一个 `> target` 的位置，而 `left - 1 = right` 就是最后一个 `<= target` 的位置；由于已经确认 `target` 存在，因此它就是最后一个 `target`。

以 `[5,7,7,8,8,10]`、目标 `8` 为例：

| 查找 | `(left,right,mid)` 的过程 | 结束时 |
| --- | --- | --- |
| 第一个 `>=8` | `(0,5,2)`，`(3,5,4)`，`(3,3,3)` | `left=3` |
| 第一个 `>8` | `(0,5,2)`，`(3,5,4)`，`(5,5,5)` | `left=5`，右边界是 `4` |

两次都是 `O(log n)`，合起来仍是 `O(log n)`，空间 `O(1)`。

熟悉原理后，也可以用标准库：

```python
from bisect import bisect_left, bisect_right

def searchRange_bisect(nums, target):
    first = bisect_left(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, bisect_right(nums, target) - 1]
```

`bisect_left` 找左侧插入位置，也就是第一个 `>=target`；`bisect_right` 找右侧插入位置，也就是第一个 `>target`。两者都不修改数组。
**注意**：`bisect_left` 只保证找到第一个 `>= target` 的位置；如果位置已经越界，**或**该位置不是 `target`，就说明 `target` 不存在。

### 12. 单调栈与单调队列

「单调」不是把整个数组排序，而是边遍历边维护一个有顺序的候选集合，及时移除不再需要的元素。通常存的是**下标**，这样既能找到原来的值，也能定位答案或判断元素是否过期。

#### 12.1 单调栈：下一个更大元素

**原题链接**：[LeetCode 503 · 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)（循环数组版本）。

**题意**：对数组中的每个位置，找沿右侧方向遇到的第一个严格大于它的数；这里是循环数组，到末尾后还可以从开头继续找。找不到则为 `-1`。

示例：`[1, 2, 1]` 返回 `[2, -1, 2]`。最后一个 `1` 可以绕到开头，再找到 `2`。

**思路先用普通数组理解**：栈里放着「还没等到更大值」的下标。遇到新数时，只要它比栈顶对应的数大，就可以给栈顶位置填写答案，并弹出栈顶；继续检查新的栈顶。

以 `[2, 1, 3]` 为例，表中为方便理解显示栈内的值，实际代码保存下标：

| 新来的数 | 操作 | 栈中等待的值（左为栈底） |
| --- | --- | --- |
| `2` | 没有人等待，直接入栈 | `[2]` |
| `1` | 比 `2` 小，不能替 `2` 找到答案，入栈 | `[2, 1]` |
| `3` | 先给 `1` 填答案 `3`，再给 `2` 填答案 `3`，最后入栈 | `[3]` |

为什么它是「第一个」更大的数？因为扫描方向是从左到右；若此前已出现更大的数，该位置早就被弹出并填好答案了，不会继续留在栈里等待。

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(2*n):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                t = stack.pop() #之前入栈的元素的下标
                res[t] = nums[index]
            if i < n:
                stack.append(i) #入栈下标
        return res
```

**几个容易混淆的点**：

- `stack[-1]` 是下标，`nums[stack[-1]]` 才是数值。
- 使用 `while` 而不是 `if`，因为一个新数可能同时解决多个位置的答案。
- 相等不算「更大」，所以用 `>`；相等的值可以一起留在栈中，此处准确地说是「非递增」。
- `i % n` 产生 `0,1,...,n-1,0,1,...,n-1` 的下标序列，不需要真的复制数组。
- 每个下标只在第一轮入栈；第二轮扫描只为尚未找到答案的位置补答案。

虽然有两层循环，但每个下标最多入栈一次、出栈一次，总时间 `O(n)`，空间 `O(n)`。

#### 12.2 单调队列：滑动窗口最大值

**原题链接**：[LeetCode 239 · 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)（与[题 6](https://app.notion.com/p/LeetCode-python-6c6ecda0f71f8222a06f019fc4c3a836?pvs=21) 相同，这里练习单调队列解法）。

**题意**：窗口长度固定为 `k`，每次向右移动一格，返回每个窗口的最大值。约定 `1 <= k <= len(nums)`。

示例：`nums = [1, 3, -1, -3, 5, 3, 6, 7]`，`k = 3`，返回 `[3, 3, 5, 5, 6, 7]`。

普通做法每个窗口重新求最大值，需要 `O(nk)`。单调队列只留下**未来仍有可能成为窗口最大值**的候选。

**为什么新来的较大值能淘汰旧的小值？**

例如队尾是旧的 `3`，新来的是 `5`：只要未来的窗口还包含这个旧 `3`，就一定也包含更新的 `5`；`5` 更大，并且更晚离开窗口。因此旧 `3` 不可能再成为必须保留的最大值候选，可以永久从候选中移除。

```python
from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()  # 下标递增，对应数值从队首到队尾严格递减
    answer = []

    for i, num in enumerate(nums):
        # 当前窗口的下标范围是 [i-k+1, i]
        # 小于左边界的旧下标，从队首移除
        while q and q[0] <= i - k:
            q.popleft()

        # 新数更大或相等：旧的队尾候选不再需要
        while q and nums[q[-1]] <= num:
            q.pop()

        q.append(i)

        # 凑够 k 个元素，才开始记录完整窗口的答案
        if i >= k - 1:
            answer.append(nums[q[0]])

    return answer
```

队列中的元素不一定是窗口的全部元素，而是筛选后的候选；**队首对应的值就是当前最大值**。

以 `[1, 3, -1, -3, 5]`、`k=3` 为例：

| `i` | 当前处理 | 候选队列中的值 | 本次记录 |
| --- | --- | --- | --- |
| `0` | 加入 `1` | `[1]` | 窗口未满 |
| `1` | `3` 淘汰队尾 `1` | `[3]` | 窗口未满 |
| `2` | 加入 `-1` | `[3, -1]` | `3` |
| `3` | 加入 `-3` | `[3, -1, -3]` | `3` |
| `4` | 旧 `3` 过期；`5` 淘汰 `-3`、`-1` | `[5]` | `5` |

维护队尾时使用 `<` 会保留相等的值，此时队列对应值非递增，也能得到正确答案。使用 `<=` 则删除旧的相等值：新值一样大、过期更晚，保留新值即可。

每个下标入队一次，最多从队首或队尾移除一次，因此总时间 `O(n)`，队列空间 `O(k)`。这也是题 6 比堆解法更优的写法。

#### 12.3 放在一起记

| 对比 | 单调栈 | 单调队列 |
| --- | --- | --- |
| 常见问题 | 下一个更大/更小元素 | 滑动窗口最大/最小值 |
| 保存什么 | 等待答案的下标 | 可能成为窗口最值的下标 |
| 为什么弹出 | 当前新数让旧位置找到了答案 | 旧元素过期，或被更有优势的新元素淘汰 |
| 从哪里移除 | 栈顶 | 队首移除过期元素，队尾淘汰劣势候选 |
| 答案怎么产生 | 弹出旧位置时给它填答案 | 窗口完整时读取队首 |
| Python 容器 | `list` 的 `append/pop` | `deque` 的 `append/pop/popleft` |

一句话记忆：**单调栈让旧元素「等到答案就出栈」；单调队列让窗口「只留下可能成为最值的候选」。**