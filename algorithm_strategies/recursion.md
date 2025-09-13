# 递归 recursion

## 介绍

将大问题转化为小问题，通过递归依次解决各个小问题

## 示例

### [reverse-string](https://leetcode-cn.com/problems/reverse-string/)

> 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
> 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

```Python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def _swap(i,j):
            if i>=j:
                return
            s[i],s[j]=s[j],s[i]
            _swap(i+1,j-1)
        _swap(0,len(s)-1)
```
这里面我们只是练习递归策略，解释器在每次递归调用时，会在调用栈里保存函数的上下文（参数、局部变量、返回点等），导致空间复杂度是O(n);
当然，这道题其实用双指针来做，空间复杂度更好，为O(1),代码如下。

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right=0, len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1    
        return
```



### [swap-nodes-in-pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

> 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
> **你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

```Python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is not None and head.next is not None:
            head_next_pair = self.swapPairs(head.next.next)
            p = head.next
            head.next = head_next_pair
            p.next = head
            head = p
        
        return head
```

### [unique-binary-search-trees-ii](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)

> 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

注意：此题用来训练递归思维有理论意义，但是实际上算法返回的树并不是 deep copy，多个树之间会共享子树。

```Python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generateTrees_rec(i, j):
            
            if i > j:
                return [None]
            
            result = []
            for m in range(i, j + 1):
                left = generateTrees_rec(i, m - 1)
                right = generateTrees_rec(m + 1, j)
                
                for l in left:
                    for r in right:
                        result.append(TreeNode(m, l, r))
            
            return result
        
        return generateTrees_rec(1, n) if n > 0 else []
```

## 递归 + 备忘录 (recursion with memorization, top-down DP)

### [fibonacci-number](https://leetcode-cn.com/problems/fibonacci-number/)

> 斐波那契数，通常用  F(n) 表示，形成的序列称为斐波那契数列。该数列由  0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
> F(0) = 0,   F(1) = 1
> F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
> 给定  N，计算  F(N)。

```Python
class Solution:
    def fib(self, N: int) -> int:
        
        mem = [-1] * (N + 2)
        
        mem[0], mem[1] = 0, 1
        
        def fib_rec(n):
            if mem[n] == -1:
                mem[n] = fib_rec(n - 1) + fib_rec(n - 2)
            return mem[n]
        
        return fib_rec(N)
```

## 练习

- [ ] [reverse-string](https://leetcode-cn.com/problems/reverse-string/)
- [ ] [swap-nodes-in-pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
- [ ] [unique-binary-search-trees-ii](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)
- [ ] [fibonacci-number](https://leetcode-cn.com/problems/fibonacci-number/)

