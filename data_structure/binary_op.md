# 二进制

## 常见二进制操作

### 基本操作

a=0^a=a^0

0=a^a

由上面两个推导出：a=a^b^b

### 交换两个数

a=a^b

b=a^b

a=a^b

### 移除最后一个 1

a=n&(n-1)

### 获取最后一个 1

diff=(n&(n-1))^n

## 常见题目

### [single-number](https://leetcode-cn.com/problems/single-number/)

> 给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        out = 0
        for num in nums:
            out ^= num
        
        return out
```

### [single-number-ii](https://leetcode-cn.com/problems/single-number-ii/)

> 给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
```

### [single-number-iii](https://leetcode-cn.com/problems/single-number-iii/)

> 给定一个整数数组  `nums`，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

```Python
class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]
```

### [number-of-1-bits](https://leetcode-cn.com/problems/number-of-1-bits/)

> 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’  的个数（也被称为[汉明重量](https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F)）。

```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        while n > 0:
            num_ones += 1
            n &= n - 1
        return num_ones
```

### [counting-bits](https://leetcode-cn.com/problems/counting-bits/)

> 给定一个非负整数  **num**。对于  0 ≤ i ≤ num  范围中的每个数字  i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

- 思路：利用上一题的解法容易想到 O(nk) 的解法，k 为位数。但是实际上可以利用动态规划将复杂度降到 O(n)，想法其实也很简单，即当前数的 1 个数等于比它少一个 1 的数的结果加 1。下面给出三种 DP 解法

```Python
# x <- x // 2
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        num_ones = [0] * (num + 1)
        
        for i in range(1, num + 1):
            num_ones[i] = num_ones[i >> 1] + (i & 1) # 注意位运算的优先级
        
        return num_ones
```

```Python
# x <- x minus right most 1
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        num_ones = [0] * (num + 1)
        
        for i in range(1, num + 1):
            num_ones[i] = num_ones[i & (i - 1)] + 1
        
        return num_ones
```

```Python
# x <- x minus left most 1
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        num_ones = [0] * (num + 1)
        
        left_most = 1
        
        while left_most <= num:
            for i in range(left_most):
                if i + left_most > num:
                    break
                num_ones[i + left_most] = num_ones[i] + 1
            left_most <<= 1
        
        return num_ones
```

### [reverse-bits](https://leetcode-cn.com/problems/reverse-bits/)

> 颠倒给定的 32 位无符号整数的二进制位。

思路：简单想法依次颠倒即可。更高级的想法是考虑到处理超长比特串时可能出现重复的pattern，此时如果使用 cache 记录出现过的 pattern 并在重复出现时直接调用结果可以节约时间复杂度，具体可以参考 leetcode 给出的解法。

```Python
import functools

class Solution:
    def reverseBits(self, n):
        ret, power = 0, 24
        while n:
            ret += self.reverseByte(n & 0xff) << power
            n = n >> 8
            power -= 8
        return ret

    # memoization with decorator
    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023
```

### [bitwise-and-of-numbers-range](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/)

> 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

思路：直接从 m 到 n 遍历一遍显然不是最优。一个性质，如果 m 不等于 n，则结果第一位一定是 0 （中间必定包含一个偶数）。利用这个性质，类似的将 m 和 n 右移后我们也可以判断第三位、第四位等等，免去了遍历的时间复杂度。

```Python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        shift = 0
        while m < n:
            shift += 1
            m >>= 1
            n >>= 1
        
        return m << shift
```

## 练习

- [ ] [single-number](https://leetcode-cn.com/problems/single-number/)
- [ ] [single-number-ii](https://leetcode-cn.com/problems/single-number-ii/)
- [ ] [single-number-iii](https://leetcode-cn.com/problems/single-number-iii/)
- [ ] [number-of-1-bits](https://leetcode-cn.com/problems/number-of-1-bits/)
- [ ] [counting-bits](https://leetcode-cn.com/problems/counting-bits/)
- [ ] [reverse-bits](https://leetcode-cn.com/problems/reverse-bits/)
