# 684 Redundant Connection





## 0X00 题目





https://leetcode.com/problems/redundant-connection/description/





## 0X01 题解



不是最优解（python）



```python
class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.ranks = [1 for i in range(n + 1)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        
        if self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        elif self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        else:        
            self.parents[py] = px
            self.ranks[px] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if edges is None or len(edges) == 0 : return []
        us = UnionFindSet(len(edges))
        for x, y in edges:
            # 如果 x, y 在同一个 set 里面则就会出现环
            if us.union(x, y):
                continue
            else:
                return [x, y]
        return []
```

