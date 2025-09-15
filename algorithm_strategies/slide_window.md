# 滑动窗口

## 模板

```python
from collections import Counter, defaultdict

def sliding_window(s: str, t: str):
    """
    在 s 上维护一个可伸缩窗口，使其满足关于 t 的某种条件（如覆盖、异位词等）。
    你只需要在标注的四处填入题目相关逻辑即可。
    """
    need = Counter(t)            # 需要满足的字符频次
    window = defaultdict(int)    # 当前窗口内的字符频次
    valid = 0                    # 满足 need[c] 的字符种类数（窗口内恰好达到要求就 +1）

    left = 0
    right = 0

    # —— 可选：用于返回答案的变量（示例为最小覆盖子串）——
    start, min_len = 0, float('inf')  # ④ 题意相关：如何记录或更新答案

    while right < len(s):
        # 右侧字符入窗
        c = s[right]
        right += 1

        # ① 右指针右移之后，窗口数据更新
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # —— debug 输出：Python 习惯用半开区间 [left, right) —— 
        # print(f"window: [{left}, {right}) -> {s[left:right]}")

        # ② 判断窗口是否需要收缩（条件因题而异）
        # 例如“窗口已经覆盖所有所需字符”：
        while valid == len(need):
            # ④ 根据题意计算结果（例如更新最小区间）
            if right - left < min_len:
                start, min_len = left, right - left

            # 左侧字符出窗
            d = s[left]
            left += 1

            # ③ 左指针右移之后，窗口数据更新
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    # ④ 返回题意需要的结果（此处示例为最小覆盖子串；其他题可改为计数/布尔/列表等）
    return "" if min_len == float('inf') else s[start:start + min_len]

```

## 使用说明（如何“套模板”）

- ① 右移 `right` 后更新窗口：通常是 `window[c] += 1`，并在“恰好达到需求”时 `valid += 1`。
- ② 什么时候收缩：按题意决定。
  - 最小覆盖类：当 `valid == len(need)` 时收缩。
  - 无重复字符最长子串：当出现重复（如 `window[c] > 1`）时收缩。
- ③ 左移 `left` 后更新窗口：通常是把 `window[d] -= 1`，并在从“满足”变为“不满足”时 `valid -= 1`。
- ④ 如何计算结果：
  - 返回最小窗口：维护 `start, min_len`。
  - 返回是否存在：满足条件时可直接 `return True`。
  - 返回所有起点：满足条件时收集索引。
  - 返回最大长度：维护 `ans = max(ans, right-left)`。



## 示例

### [minimum-window-substring](https://leetcode-cn.com/problems/minimum-window-substring/)

> 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
> 注意：
> -对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
> -如果 s 中存在这样的子串，我们保证它是唯一的答案

```Python
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        valid = 0

        left = 0
        right = 0
        start, min_len = 0, float('inf')

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < min_len:
                    start, min_len = left, right - left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_len == float('inf') else s[start:start + min_len]
```

当然，上面的写法有点冗长了，一种更加基础的写法是下面这样的：
```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        left = 0
        right = 0
        start, min_len = 0, float('inf')

        while right < len(s):
            window[s[right]] += 1
            right += 1

            while window >= need:  # 直接通过 Counter 比较
                if right - left < min_len:
                    start, min_len = left, right - left

                window[s[left]] -= 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
```
对于这段代码的分析：

1. **去除 `valid` 计数器**：
   - 通过直接比较 `window >= need`，我们不再需要使用 `valid` 来追踪符合条件的字符种类数。代码更简洁，不需要额外的变量来进行管理。

2. **简化窗口更新**：
   - 在更新窗口时，使用 `window[s[right]] += 1` 和 `window[s[left]] -= 1` 来更新窗口中的字符频次。这避免了手动管理字符计数，代码变得更加直观。

3. **使用 `window >= need`**：
   - `Counter` 对象支持直接比较，使用 `window >= need` 来判断窗口是否包含 `t` 中所有字符的要求。这使得频次的判断更加简洁，无需手动逐个检查每个字符的频次。

- 注意：复杂度变化
虽然通过使用 `Counter` 比较，使代码变得简洁，但 **时间复杂度** 反而有所增加。每次窗口更新时，`window >= need` 的比较需要 **O(∣Σ∣)** 的时间，其中 `∣Σ∣` 为字符集大小（对于英文字母，通常为 26 或 52）。因此，最坏情况下 **时间复杂度** 会变为 `O(∣Σ∣ * m+n)`，其中 `m` 是字符串 `s` 的长度,`n`是字符串`t`的长度。

相对于原来的 `valid` 计数器方案（通过手动管理字符频次），这会导致更高的时间复杂度。虽然代码变得更简洁，但效率会下降，尤其是在字符集非常大的情况下。


### [permutation-in-string](https://leetcode-cn.com/problems/permutation-in-string/)

> 给定两个字符串  **s1**  和  **s2**，写一个函数来判断  **s2**  是否包含  **s1 **的排列。

```Python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target = collections.defaultdict(int)
        
        for c in s1:
            target[c] += 1
        
        r, num_char = 0, len(target)

        while r < len(s2):
            if s2[r] in target:
                l, count = r, 0
                window = collections.defaultdict(int)
                while r < len(s2):
                    c = s2[r]
                    if c not in target:
                        break
                    window[c] += 1
                    if window[c] == target[c]:
                        count += 1
                        if count == num_char:
                            return True
                    while window[c] > target[c]:
                        window[s2[l]] -= 1
                        if window[s2[l]] == target[s2[l]] - 1:
                            count -= 1
                        l += 1
                    r += 1
            else:
                r += 1
        
        return False
```

### [find-all-anagrams-in-a-string](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

> 给定一个字符串  **s **和一个非空字符串  **p**，找到  **s **中所有是  **p **的字母异位词的子串，返回这些子串的起始索引。

```Python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        target = collections.defaultdict(int)
        
        for c in p:
            target[c] += 1
        
        r, num_char = 0, len(target)
        
        results = []
        while r < len(s):
            if s[r] in target:
                l, count = r, 0
                window = collections.defaultdict(int)
                while r < len(s):
                    c = s[r]
                    if c not in target:
                        break
                    window[c] += 1
                    if window[c] == target[c]:
                        count += 1
                        if count == num_char:
                            results.append(l)
                            window[s[l]] -= 1
                            count -= 1
                            l += 1
                    while window[c] > target[c]:
                        window[s[l]] -= 1
                        if window[s[l]] == target[s[l]] - 1:
                            count -= 1
                        l += 1
                    r += 1
            else:
                r += 1
        
        return results
```

### [longest-substring-without-repeating-characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

> 给定一个字符串，请你找出其中不含有重复字符的   最长子串   的长度。
> 示例  1:
>
> 输入: "abcabcbb"
> 输出: 3
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_idx = {}
        
        l, max_length = 0, 0
        for r, c in enumerate(s):
            if c in last_idx and last_idx[c] >= l:
                max_length = max(max_length, r - l)
                l = last_idx[c] + 1
            last_idx[c] = r
        
        return max(max_length, len(s) - l) # note that the last substring is not judged in the loop
```

## 总结

- 和双指针题目类似，更像双指针的升级版，滑动窗口核心点是维护一个窗口集，根据窗口集来进行处理
- 核心步骤
  - right 右移
  - 收缩
  - left 右移
  - 求结果

## 练习

- [ ] [minimum-window-substring](https://leetcode-cn.com/problems/minimum-window-substring/)
- [ ] [permutation-in-string](https://leetcode-cn.com/problems/permutation-in-string/)
- [ ] [find-all-anagrams-in-a-string](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)
- [ ] [longest-substring-without-repeating-characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
