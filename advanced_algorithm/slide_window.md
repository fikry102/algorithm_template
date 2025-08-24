# 滑动窗口

## 模板

```cpp
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0;
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
```

需要变化的地方

- 1、右指针右移之后窗口数据更新
- 2、判断窗口是否要收缩
- 3、左指针右移之后窗口数据更新
- 4、根据题意计算结果

## 示例

### [minimum-window-substring](https://leetcode-cn.com/problems/minimum-window-substring/)

> 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串

```Python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = collections.defaultdict(int)
        window = collections.defaultdict(int)
        
        for c in t:
            target[c] += 1
            
        min_size = len(s) + 1
        min_str = ''
        
        l, r, count, num_char = 0, 0, 0, len(target)
        
        while r < len(s):
            c = s[r]
            r += 1

            if c in target:
                window[c] += 1
                
                if window[c] == target[c]:
                    count += 1
                    
                    if count == num_char:
                        while l < r and count == num_char:
                            c = s[l]
                            l += 1
                            
                            if c in target:
                                window[c] -= 1
                                
                                if window[c] == target[c] - 1:
                                    count -= 1
                                    
                        if min_size > r - l + 1:
                            min_size = r - l + 1
                            min_str = s[l - 1:r]
        
        return min_str
```

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
