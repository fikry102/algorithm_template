[https://leetcode.cn/problem-list/2cktkvj/](https://leetcode.cn/problem-list/2cktkvj/)


### 1. [160. 相交链表 - 力扣（LeetCode）](https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=problem-list-v2&envId=2cktkvj)

一种自然的思路，遍历两个链表，分别存到两个列表中，然后从末尾往前找出相交部分的首个节点。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        a_list=[]
        while a:
            a_list.append(a)
            a=a.next
        b=headB
        b_list=[]
        while b:
            b_list.append(b)
            b=b.next
        num=0
        m=len(a_list)-1
        n=len(b_list)-1
        while num<=m and num<=n:
            if a_list[m-num]!=b_list[n-num]:
                break
            num+=1
    
        if num==0:
            return None
        else:
            return a_list[m-num+1]
```



双指针相遇法： 只要你和我没有相遇（指向同一个节点），我们就继续走。

> 我住长江头，君住长江尾，日夜思君不见君，共饮一江水。
> 君奔长江头，我赴长江尾，辗转轮回未谋面，邂逅时好美！

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        you = headA
        me = headB
        while you is not me:
            you = you.next if you else headB
            me = me.next if me else headA
        return you
```



### 2. [236. 二叉树的最近公共祖先 - 力扣（LeetCode）](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/?envType=problem-list-v2&envId=2cktkvj)

可以bfs遍历一下，并且用一个字典parent记录一下父节点是啥，用另一个字典order记录一下加入到字典的顺序

然后呢，对p和q两个节点，先确定谁出现的顺序更靠后，让靠后的那个节点变成它的父节点

以此类推，每一次都让出现顺序靠后的节点变成它的父节点，直到两个节点相同为止（至少有一个共同祖先是根节点）

tips: 节点可以作为key，

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent={}
        order={}
        num=1
        queue=deque()
        queue.append(root)
        while queue:
            r=queue.popleft()
            order[r]=num
            num+=1
            if r.left:
                queue.append(r.left)
                parent[r.left]=r
                order[r.left]=num
                num+=1
            if r.right:
                queue.append(r.right)
                parent[r.right]=r
                order[r.right]=num
                num+=1
        while p!=q:
            if order[p]>order[q]:
                p=parent[p]
            if order[p]<order[q]:
                q=parent[q]
        return p
```



<h3 id="NlbfV"></h3>

### 3. [234. 回文链表 - 力扣（LeetCode）](https://leetcode.cn/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=2cktkvj)

一种简单的思路，就是遍历一下存到list，然后判断反转的list和原始list是否相等

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head:
            a.append(head.val)
            head = head.next
        return a[::-1]==a
```


> 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

双指针解法：

先用快慢指针fast和slow，找到中点，分成总共有奇数和偶数个节点

然后呢，使用链表反转技巧，将后半段反转；

和head指向的前半段进行比较。



关于链表反转技巧：

用prev指向已反转部分的头节点，然后就是四步走策略：

**保存后继，反转指针，当前节点并入反转部分，处理下一个**

1：slow会指向1

1 2 1： slow最终会指向2

1 2 2 1：slow最终会指向第2个2

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        fast = fast.next
        while fast and slow: #slow走一步，fast走两步
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        #这个时候，肯定是fast为None了，slow指向链表的右边一半的开头结点
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #比较两个链表
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

```



### 4. [739. 每日温度 - 力扣（LeetCode）](https://leetcode.cn/problems/daily-temperatures/?envType=problem-list-v2&envId=2cktkvj)
题目中给了个提示 1：

If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.



思考了下，觉得说可以用一个字典来存储每种温度出现的下标，然后遍历列表，对当前的温度，通过字典查找比它大的温度的下标的最小值

根据上面的思路，可以写出来一份代码，3个测试用例通过了；但是`for candidate in d[c]:`这部分其实很耗时，所以提交的时候超时了

```python
from collections import defaultdict
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d=defaultdict(list)
        for i,t in enumerate(temperatures):
            d[t].append(i)
        res = []
        for i,t in enumerate(temperatures):
            min_i=1000000
            for c in range(t+1,101):
                if c in d.keys():
                    for candidate in d[c]:
                        if candidate > i:
                            min_i =min(min_i,candidate-i)
                            break
            if min_i !=1000000:
                res.append(min_i)
            else:
                res.append(0)
        return res
```



不过有个值得注意的点，d[c]是按顺序添加的下标，所以可以引入二分查找来优化下时间复杂度, 好像过了

```python
from collections import defaultdict
import bisect
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d=defaultdict(list)
        for i,t in enumerate(temperatures):
            d[t].append(i)
        res = []
        for i,t in enumerate(temperatures):
            min_i=1000000
            for c in range(t+1,101):
                if c in d.keys():
                    lst=d[c]
                    pos = bisect.bisect_right(lst,i)
                    if pos < len(lst):
                        min_i =min(min_i,lst[pos]-i)
            if min_i !=1000000:
                res.append(min_i)
            else:
                res.append(0)
        return res




        
```



这道题其实可以用单调栈来进行更加高效求解：

栈里永远只保留那些**至今还没找到“下一个更大元素”的人**。而且，这些人在栈里是**从底到顶严格递减**的

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i, t in enumerate(temperatures):
            if stack and t>temperatures[stack[-1]]:
                index = stack.pop()
                res[index]=i-index
            else:
                stack.append(i)
        return res
```

一开始实现的时候写成了上面的版本，其中的问题在于：只 pop 一次不够：当前温度可能同时比栈里多个下标对应的温度都高，需要一直弹到不满足为止。 结论：**应该用 while而不是if**

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                index = stack.pop()
                res[index]=i-index
            else:
                stack.append(i)
        return res
```

上面这个版本跑通了，但实际上有个小小的问题，就是else:这部分其实没必要，好在while else这种语法也是有的，才能跑通。

**while-else** 语法的规则是：

- else 会在 **while 循环“正常结束”** 时执行（也就是条件变成 False 退出）。
- 如果 while 里发生了 break，则 **不会执行** else。



可以简化一下形成最终的版本：先 while 弹栈更新答案，最后无条件 append(i), **因为当前的i不管怎样都是需要入栈以便后续进行处理的**

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                index = stack.pop()
                res[index]=i-index
            stack.append(i)
        return res
```



### 5. [226. 翻转二叉树 - 力扣（LeetCode）](https://leetcode.cn/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=2cktkvj)

递归调用，交换左子树和右子树就行

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            root.left, root.right=root.right, root.left
            if root.left:
                invert(root.left)
            if root.right:
                invert(root.right)
        if root:
            invert(root)
        return root
```

### 6. [221. 最大正方形 - 力扣（LeetCode）](https://leetcode.cn/problems/maximal-square/?envType=problem-list-v2&envId=2cktkvj)

使用动态规划来求解：

对于每个位置 (i,j)，检查在矩阵中该位置的值：

如果该位置的值是 0，则 `dp[i][j]`=0，因为当前位置不可能在由 1 组成的正方形中；

如果该位置的值是 1，则 `dp[i][j]` 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定。具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 1，状态转移方程：`dp[i][j]=min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])+1`



```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #使用dp来求解,dp[i][j]用来表示以(i,j)作为右下角点能构成的最大正方形的边长
        #dp[i][j]=min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])+1
        rows,cols=len(matrix), len(matrix[0])
        dp=[[0]*cols for _ in range(rows+1)]
        ans=0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    ans=max(dp[i][j],ans)
        return ans*ans                 
```



### 7. [215. 数组中的第K个最大元素 - 力扣（LeetCode）](https://leetcode.cn/problems/kth-largest-element-in-an-array/?envType=problem-list-v2&envId=2cktkvj)

1.只找第k大    →  利用快排的partition方法进行快速选择，只递归target所在的那一侧 

2.有序数组退化  →  随机选取pivot 

3.重复元素退化  →  三路划分 



```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target=len(nums)- k 
        def solve(left, right):
            if left==right:
                return nums[left]

            low,mid,high =left,left,right  #we move mid to achieve partition
            pivot=nums[random.randint(left,right)]
            while mid <= high: #[mid,high]内的元素有待和pivot进行比较
                if nums[mid]<pivot:
                    nums[low],nums[mid]=nums[mid],nums[low]
                    low+=1
                    mid+=1
                elif nums[mid]==pivot:
                    mid+=1
                else:
                    nums[high],nums[mid]=nums[mid],nums[high] 
                    high-=1
            #mid 现在指向的位置，是之前遇到 > pivot 不断把 high 左移后留下的边界；
            # 即 [mid, right] 全是 > pivot 的元素
            #[left,low):<pivot, [low,mid):==pivot, [mid, right]:>pivot
            if low<=target<mid:
                return pivot
            elif target<low:
                return solve(left,low-1)
            else:
                return solve(high+1,right)
               
        return solve(0,len(nums)-1)
```



### 8. [208. 实现 Trie (前缀树) - 力扣（LeetCode）](https://leetcode.cn/problems/implement-trie-prefix-tree/?envType=problem-list-v2&envId=2cktkvj)
“用嵌套字典存前缀”：
	•	根就是一个容器（开始时通常是空的 {}），里面按字符开分支。
	•	插入：对单词每个字符，如果当前层没有这个字符就新建一个空分支，然后进入下一层；单词结束处放一个“结束标记”。
	•	search：按字符一路走，走不通就不存在；走完还得有“结束标记”才算这个词被插入过。
	•	startsWith：只要前缀这条路走得通就行，不看结束标记。





```python
class Trie:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            node.setdefault(ch,{})
            node=node[ch]
        node['#']=True

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node:
                return False
            node=node[ch]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```



### 9. [207. 课程表 - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule/?envType=problem-list-v2&envId=2cktkvj)

使用bfs进行广度优先搜索，把所有入度为0的节点入栈，然后 不断出栈，看下最终是否所有节点的入度都为0

```python
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses

        #用一个字典记录一下所有的pairs
        d=defaultdict(list)
        for t,s in prerequisites:
            d[s].append(t)
            indegree[t]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            k = q.popleft()
            for v in d[k]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        
        for num in indegree:
            if num!=0:
                return False
        return True

            
```



### 10. [206. 反转链表 - 力扣（LeetCode）](https://leetcode.cn/problems/reverse-linked-list/?envType=problem-list-v2&envId=2cktkvj)



