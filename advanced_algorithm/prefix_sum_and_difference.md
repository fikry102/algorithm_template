# 前缀和 & 差分数组

## 简介

- **前缀和**：通过预处理累计和，快速计算区间和。常用于区间和查询、统计子数组和。  
- **差分数组**：用来高效维护区间增减操作，最终通过前缀和还原结果。

---

## 前缀和

### 模板

```python
# 构建前缀和数组 pre，其中 pre[0] = 0
pre = [0]
for x in nums:
    pre.append(pre[-1] + x)

# 区间 [l, r] 的和
res = pre[r + 1] - pre[l]
```

### 经典题目

#### [560. Subarray Sum Equals K](https://leetcode-cn.com/problems/subarray-sum-equals-k/)

> 给定一个整数数组和一个整数 k，找到数组中和为 k 的连续子数组的个数。

思路：用哈希表记录某个前缀和出现次数。

```python
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        from collections import defaultdict
        pre = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        for x in nums:
            pre += x
            ans += cnt[pre - k]
            cnt[pre] += 1
        return ans
```

#### [974. Subarray Sums Divisible by K](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/)

> 判断子数组和是否能被 k 整除，或统计这样的子数组数量。

思路：余数相同的两个前缀和之差可以被 k 整除。

```python
class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        from collections import defaultdict
        pre = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        for x in nums:
            pre += x
            r = pre % k
            ans += cnt[r]
            cnt[r] += 1
        return ans
```

---

## 差分数组

### 模板

```python
diff = [0] * (n + 1)

# 对区间 [l, r] 增加 val
diff[l] += val
diff[r + 1] -= val

# 还原数组
res = [0] * n
cur = 0
for i in range(n):
    cur += diff[i]
    res[i] = cur
```

### 经典题目

#### [1109. Corporate Flight Bookings](https://leetcode-cn.com/problems/corporate-flight-bookings/)

```python
class Solution:
    def corpFlightBookings(self, bookings, n: int):
        diff = [0] * (n + 1)
        for l, r, seats in bookings:
            diff[l - 1] += seats
            diff[r] -= seats
        res = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            res[i] = cur
        return res
```

#### [1094. Car Pooling](https://leetcode-cn.com/problems/car-pooling/)

```python
class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        MAX = 1001
        diff = [0] * (MAX + 1)
        for num, s, e in trips:
            diff[s] += num
            diff[e] -= num
        cur = 0
        for x in diff:
            cur += x
            if cur > capacity:
                return False
        return True
```

---

## 小结

- 前缀和适合快速区间和、统计子数组问题。  
- 差分数组适合频繁区间修改的场景。

## 练习

- [560. Subarray Sum Equals K](https://leetcode-cn.com/problems/subarray-sum-equals-k/)  
- [974. Subarray Sums Divisible by K](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/)  
- [1109. Corporate Flight Bookings](https://leetcode-cn.com/problems/corporate-flight-bookings/)  
- [1094. Car Pooling](https://leetcode-cn.com/problems/car-pooling/)
