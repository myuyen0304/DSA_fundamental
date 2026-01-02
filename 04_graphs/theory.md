# 📊 Graphs - Đồ thị

## 📖 Graph là gì?

**Graph** là cấu trúc dữ liệu phi tuyến (non-linear) bao gồm:
- **Vertices (Nodes)**: Các đỉnh
- **Edges**: Các cạnh nối giữa các đỉnh

Graph được sử dụng để biểu diễn mạng lưới, quan hệ, và kết nối.

### Visual:

```
    A --- B
    |     |
    |     |
    C --- D
```

---

## 🎨 Types of Graphs

### 1️⃣ **Undirected Graph**
Edges không có hướng (bidirectional).

```
A --- B
|     |
C --- D
```
Edge A-B có thể đi cả hai chiều.

### 2️⃣ **Directed Graph (Digraph)**
Edges có hướng cụ thể.

```
A → B
↑   ↓
C ← D
```

### 3️⃣ **Weighted Graph**
Mỗi edge có weight (cost/distance).

```
    5
A ----- B
|   3   |
|       | 2
C ----- D
    4
```

### 4️⃣ **Unweighted Graph**
Tất cả edges đều có weight bằng nhau (thường là 1).

---

## 📊 Graph Representations

### **1. Adjacency Matrix**

Matrix 2D: `adj[i][j] = 1` nếu có edge từ i đến j.

**Example**:
```
Graph:    0 → 1
          ↓   ↓
          2 → 3

Matrix:
    0  1  2  3
0 [[0, 1, 1, 0],
1  [0, 0, 0, 1],
2  [0, 0, 0, 1],
3  [0, 0, 0, 0]]
```

**Properties**:
- **Space**: O(V²)
- **Check edge**: O(1)
- **Find neighbors**: O(V)
- **Add vertex**: O(V²) - need to resize matrix
- **Good for**: Dense graphs, quick edge lookup

**Implementation**:
```python
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v):
        self.adj[u][v] = 1
    
    def has_edge(self, u, v):
        return self.adj[u][v] == 1
```

---

### **2. Adjacency List**

Array/dict of lists: `adj[i]` = list of neighbors of vertex i.

**Example**:
```
Graph:    0 → 1
          ↓   ↓
          2 → 3

List:
0 → [1, 2]
1 → [3]
2 → [3]
3 → []
```

**Properties**:
- **Space**: O(V + E)
- **Check edge**: O(degree)
- **Find neighbors**: O(1)
- **Add vertex**: O(1)
- **Good for**: Sparse graphs (most real-world graphs)

**Implementation**:
```python
from collections import defaultdict

class GraphList:
    def __init__(self):
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
    
    def neighbors(self, u):
        return self.adj[u]
```

---

### **3. Edge List**

List of all edges as pairs/tuples.

**Example**:
```
Graph:    0 → 1
          ↓   ↓
          2 → 3

Edge List: [(0,1), (0,2), (1,3), (2,3)]
```

**Properties**:
- **Space**: O(E)
- **Check edge**: O(E)
- **Find neighbors**: O(E)
- **Good for**: Algorithms that process all edges (Kruskal's MST)

---

## 📈 Comparison of Representations

| Operation           | Adjacency Matrix | Adjacency List | Edge List |
|---------------------|------------------|----------------|-----------|
| **Space**           | O(V²)            | O(V + E)       | O(E)      |
| **Add Vertex**      | O(V²)            | O(1)           | O(1)      |
| **Add Edge**        | O(1)             | O(1)           | O(1)      |
| **Remove Edge**     | O(1)             | O(V)           | O(E)      |
| **Check Edge**      | O(1)             | O(degree)      | O(E)      |
| **Find Neighbors**  | O(V)             | O(1)           | O(E)      |

**Recommendation**: Use **Adjacency List** for most problems!

---

## 🔍 Graph Traversals

### **1. Depth-First Search (DFS)**

Explore as far as possible along each branch before backtracking.

**Visual**:
```
    1
   / \
  2   3
 /   / \
4   5   6

DFS Order: 1 → 2 → 4 → 3 → 5 → 6
```

**Template**:
```python
def dfs(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    print(node)  # Process node
    
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```

**Properties**:
- **Time**: O(V + E)
- **Space**: O(V) - visited set + recursion stack
- **Use for**: 
  - Cycle detection
  - Path finding
  - Topological sort
  - Connected components

---

### **2. Breadth-First Search (BFS)**

Explore all neighbors at current depth before moving deeper.

**Visual**:
```
    1
   / \
  2   3
 /   / \
4   5   6

BFS Order: 1 → 2 → 3 → 4 → 5 → 6
```

**Template**:
```python
from collections import deque

def bfs(start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print(node)  # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Properties**:
- **Time**: O(V + E)
- **Space**: O(V) - queue
- **Use for**:
  - Shortest path (unweighted)
  - Level-order traversal
  - Minimum steps problems

---

## 🎯 Common Graph Problems

### **1. Connected Components**
Find number of separate connected subgraphs.

**Approach**: Run DFS/BFS from each unvisited node.

```python
def count_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    count = 0
    
    for node in range(n):
        if node not in visited:
            dfs(node, graph, visited)
            count += 1
    
    return count
```

---

### **2. Cycle Detection**

**Undirected Graph**: Use DFS with parent tracking.
```python
def has_cycle(node, parent, visited):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(neighbor, node, visited):
                return True
        elif neighbor != parent:
            return True  # Back edge found
    
    return False
```

**Directed Graph**: Use DFS with recursion stack.
```python
def has_cycle_directed(node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle_directed(neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True  # Back edge in recursion stack
    
    rec_stack.remove(node)
    return False
```

---

### **3. Shortest Path (Unweighted)**
Use BFS to find shortest path.

```python
def shortest_path_bfs(start, end):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}
    
    while queue:
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    
    return -1  # No path found
```

---

## 🌟 Graph Terminology

### **Basic Terms**:
- **Degree**: Number of edges connected to a vertex
  - **In-degree**: Incoming edges (directed)
  - **Out-degree**: Outgoing edges (directed)
- **Path**: Sequence of vertices connected by edges
- **Cycle**: Path that starts and ends at same vertex
- **Connected Graph**: Path exists between any two vertices
- **Complete Graph**: Edge between every pair of vertices

### **Special Graphs**:
- **Tree**: Connected acyclic graph with V-1 edges
- **DAG**: Directed Acyclic Graph
- **Bipartite**: Vertices can be divided into 2 sets with edges only between sets

---

## 📊 Complexity Cheat Sheet

| Algorithm            | Time Complexity | Space     |
|----------------------|-----------------|-----------|
| **DFS**              | O(V + E)        | O(V)      |
| **BFS**              | O(V + E)        | O(V)      |
| **Dijkstra**         | O((V+E) log V)  | O(V)      |
| **Bellman-Ford**     | O(V × E)        | O(V)      |
| **Floyd-Warshall**   | O(V³)           | O(V²)     |
| **Kruskal's MST**    | O(E log E)      | O(V)      |
| **Prim's MST**       | O(E log V)      | O(V)      |
| **Topological Sort** | O(V + E)        | O(V)      |

---

## 🎯 When to Use DFS vs BFS

### **Use DFS when**:
- Finding path (any path, not shortest)
- Detecting cycles
- Topological sorting
- Backtracking problems
- Tree traversals (inorder, preorder, postorder)

### **Use BFS when**:
- Finding shortest path (unweighted)
- Level-order processing
- Finding minimum steps/distance
- Spreading/propagation problems

---

## 🚀 Next Steps

1. **Read**: [Graph Traversal Implementation](traversal/implementation.py)
2. **Practice**: [DFS & BFS Problems](traversal/practice.md)
3. **Study**: [Shortest Path Algorithms](shortest_path/theory.md)

**Master graphs = Master coding interviews! 📊**
