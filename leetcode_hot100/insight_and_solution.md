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







