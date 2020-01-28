# 图（Graph）





## 0X00 什么是图——感性理解



![](./graph.png)



**如上图所示，图就是一种记录点和点（边）之间关系的数据结构**，没什么特别的地方





与之相对应算法才是更重要的知识点：



+ 如何遍历整张图？
+ 如何找到任意两个节点之间的路径？
+ 如果边有权重，如何选择两个节点的之间的最短路径？
+ ...



## 0X01 图常见的算法实现



针对上面的问题，有多种算法，下面介绍并实现这些算法



首先我们先来实现最简单的两种算法：DFS 和 BFS（对于这两种算法比较陌生的同学可以看下面的视频）



+ [BFS和DFS算法（第1讲）](https://www.bilibili.com/video/av25761720)
+ [BFS和DFS算法（第2讲）](https://www.bilibili.com/video/av25763384)
+ [BFS和DFS算法（第3讲）](https://www.bilibili.com/video/av25829980)



`接下来我们来实现`



### DFS



+ 递归实现



```python
def dfs(graph, start, visited=None):
    """
    深度优先遍历图递归实现
    1. 开始遍历时初始化一个 set：visited
    2. 向 visited 中添加当前正在遍历的节点
    3. 递归遍历所有子节点
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
```



+ 非递归实现



```python
def dfs(graph, start):
    """
    深度优先遍历图非递归实现
    1. 开始遍历时初始化一个 set：visited 和一个有着初始节点的 stack
    2. 进入循环
    3. pop 出栈顶部节点
    4. 如果这个节点没有被遍历
    	1. 将这个节点加入 visited 中
    	2. 将这个节点的所有相连节点压入栈中（下次 pop 出来的还是它的相连节点，达到深度优先的目的）
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
```





### BFS



+ 非递归实现



```python
def bfs(graph, start):
    """
    广度优先遍历图非递归实现
    1. 开始遍历时初始化一个 set：visited 和一个有着初始节点的 queue
    2. 进入循环
    3. pop 出 queue 中的第一个节点
    4. 如果这个节点没有被遍历
    	1. 将这个节点加入 visited 中
    	2. 将这个节点的所有相连节点压入 queue 中（下次 pop 出来的是它的兄弟节点而不一定是相连接点，达到广度优先的目的）
    """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

```





待续。。。







## 0X02 参考



+ https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

  

