# 二叉树





## 0X00 二叉树的遍历（非递归实现）



### 前序



```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while len(stack) > 0:
            cur = stack.pop()
            if cur is None: continue
            ans.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        
        return ans
```





### 中序

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        ans = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans
```




### 后序



```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        cur = root
        ans = []
        stack = []
        visited = set()
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            temp = stack[-1]
            if temp in visited: 
                node = stack.pop()
                ans.append(node.val)
                continue
            visited.add(temp)
            cur = temp.right
        return ans
```



