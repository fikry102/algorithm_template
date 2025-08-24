# 二叉搜索树

## 定义

- 每个节点中的值必须大于（或等于）存储在其左侧子树中的任何值。
- 每个节点中的值必须小于（或等于）存储在其右子树中的任何值。

## 应用

### [validate-binary-search-tree](https://leetcode-cn.com/problems/validate-binary-search-tree/)

> 验证二叉搜索树

```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        s = [(root, float('-inf'), float('inf'))]
        while len(s) > 0:
            node, low, up = s.pop()
            if node.left is not None:
                if node.left.val <= low or node.left.val >= node.val:
                    return False
                s.append((node.left, low, node.val))
            if node.right is not None:
                if node.right.val <= node.val or node.right.val >= up:
                    return False
                s.append((node.right, node.val, up))
        return True
```

### [insert-into-a-binary-search-tree](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)

> 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。

```Python
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
```

### [delete-node-in-a-bst](https://leetcode-cn.com/problems/delete-node-in-a-bst/)

> 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的  key  对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

```Python
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # try to find the node
        dummy = TreeNode(left=root)
        parent, node = dummy, root
        isleft = True
        while node is not None and node.val != key:
            parent = node
            isleft = key < node.val
            node = node.left if isleft else node.right 
        
        # if found
        if node is not None:
            if node.right is None:
                if isleft:
                    parent.left = node.left
                else:
                    parent.right = node.left
            elif node.left is None:
                if isleft:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else: 
                p, n = node, node.left
                while n.right is not None:
                    p, n = n, n.right
                if p != node:
                    p.right = n.left
                else:
                    p.left = n.left
                n.left, n.right = node.left, node.right
                if isleft:
                    parent.left = n
                else:
                    parent.right = n
        
        return dummy.left   
```

### [balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree/)

> 给定一个二叉树，判断它是否是高度平衡的二叉树。

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # post-order iterative
        
        s = [[TreeNode(), -1, -1]]
        node, last = root, None
        while len(s) > 1 or node is not None:
            if node is not None:
                s.append([node, -1, -1])
                node = node.left
                if node is None:
                    s[-1][1] = 0
            else:
                peek = s[-1][0]
                if peek.right is not None and last != peek.right:
                    node = peek.right
                else:
                    if peek.right is None:
                        s[-1][2] = 0
                    last, dl, dr = s.pop()
                    if abs(dl - dr) > 1:
                        return False
                    d = max(dl, dr) + 1
                    if s[-1][1] == -1:
                        s[-1][1] = d
                    else:
                        s[-1][2] = d
        
        return True
```

### [valid-bfs-of-bst](./bst_bfs.py)

> 给定一个整数数组，求问此数组是不是一个 BST 的 BFS 顺序。

此题是面试真题，但是没有在 leetcode 上找到原题。由于做法比较有趣也很有 BST 的特点，补充在这供参考。

```Python
import collections

def bst_bfs(A):

    N = len(A)
    interval = collections.deque([(float('-inf'), A[0]), (A[0], float('inf'))])

    for i in range(1, N):
        while interval:
            lower, upper = interval.popleft()
            if lower < A[i] < upper:
                interval.append((lower, A[i]))
                interval.append((A[i], upper))
                break
        
        if not interval:
            return False
    
    return True

if __name__ == "__main__":
    A = [10, 8, 11, 1, 9, 0, 5, 3, 6, 4, 12]
    print(bst_bfs(A))
    A = [10, 8, 11, 1, 9, 0, 5, 3, 6, 4, 7]
    print(bst_bfs(A))
```

## 练习

- [ ] [validate-binary-search-tree](https://leetcode-cn.com/problems/validate-binary-search-tree/)
- [ ] [insert-into-a-binary-search-tree](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)
- [ ] [delete-node-in-a-bst](https://leetcode-cn.com/problems/delete-node-in-a-bst/)
- [ ] [balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree/)
