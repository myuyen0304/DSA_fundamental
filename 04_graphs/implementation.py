"""
Graph - Implementation & Common Algorithms
Includes representations, traversals, and core algorithms
"""

from collections import defaultdict, deque
from typing import List, Set, Dict, Optional
import heapq


# ============================================================
# GRAPH REPRESENTATIONS
# ============================================================

class GraphAdjacencyList:
    """Graph using Adjacency List (most common)"""
    
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        """Add edge from u to v"""
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))
    
    def remove_edge(self, u, v):
        """Remove edge from u to v"""
        self.adj[u] = [(node, w) for node, w in self.adj[u] if node != v]
        if not self.directed:
            self.adj[v] = [(node, w) for node, w in self.adj[v] if node != u]
    
    def neighbors(self, u):
        """Get neighbors of u"""
        return self.adj[u]
    
    def has_edge(self, u, v):
        """Check if edge exists"""
        return any(node == v for node, _ in self.adj[u])
    
    def vertices(self):
        """Get all vertices"""
        return set(self.adj.keys())
    
    def edges(self):
        """Get all edges"""
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                if self.directed or u <= v:  # Avoid duplicates in undirected
                    edges.append((u, v, w))
        return edges


class GraphAdjacencyMatrix:
    """Graph using Adjacency Matrix (for dense graphs)"""
    
    def __init__(self, vertices: int, directed=False):
        self.V = vertices
        self.directed = directed
        self.matrix = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        """Add edge from u to v"""
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight
    
    def remove_edge(self, u, v):
        """Remove edge"""
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0
    
    def has_edge(self, u, v):
        """Check if edge exists"""
        return self.matrix[u][v] != 0
    
    def neighbors(self, u):
        """Get neighbors of u"""
        return [(v, self.matrix[u][v]) for v in range(self.V) if self.matrix[u][v] != 0]


# ============================================================
# GRAPH TRAVERSALS
# ============================================================

class GraphTraversal:
    """DFS and BFS implementations"""
    
    @staticmethod
    def dfs_recursive(graph: Dict, start, visited=None):
        """
        DFS Recursive - Depth First Search
        Time: O(V + E), Space: O(V)
        """
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor, _ in graph[start]:
            if neighbor not in visited:
                result.extend(GraphTraversal.dfs_recursive(graph, neighbor, visited))
        
        return result
    
    @staticmethod
    def dfs_iterative(graph: Dict, start):
        """
        DFS Iterative using stack
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                result.append(node)
                
                # Add neighbors in reverse order (to match recursive DFS)
                for neighbor, _ in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    @staticmethod
    def bfs(graph: Dict, start):
        """
        BFS - Breadth First Search
        Time: O(V + E), Space: O(V)
        """
        visited = set([start])
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    @staticmethod
    def bfs_level_order(graph: Dict, start):
        """
        BFS with level tracking
        Returns list of levels: [[level0], [level1], ...]
        """
        visited = set([start])
        queue = deque([start])
        levels = []
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                
                for neighbor, _ in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            levels.append(current_level)
        
        return levels


# ============================================================
# CYCLE DETECTION
# ============================================================

class CycleDetection:
    """Detect cycles in graphs"""
    
    @staticmethod
    def has_cycle_undirected(graph: Dict, n_vertices: int) -> bool:
        """
        Detect cycle in undirected graph using DFS
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True  # Back edge found
            
            return False
        
        # Check all components
        for vertex in range(n_vertices):
            if vertex not in visited:
                if dfs(vertex, -1):
                    return True
        
        return False
    
    @staticmethod
    def has_cycle_directed(graph: Dict, n_vertices: int) -> bool:
        """
        Detect cycle in directed graph using DFS
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        rec_stack = set()
        
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True  # Back edge in recursion stack
            
            rec_stack.remove(node)
            return False
        
        # Check all components
        for vertex in range(n_vertices):
            if vertex not in visited:
                if dfs(vertex):
                    return True
        
        return False


# ============================================================
# SHORTEST PATH ALGORITHMS
# ============================================================

class ShortestPath:
    """Shortest path algorithms"""
    
    @staticmethod
    def bfs_shortest_path(graph: Dict, start, end):
        """
        BFS for shortest path in unweighted graph
        Time: O(V + E), Space: O(V)
        """
        if start == end:
            return 0, [start]
        
        visited = {start}
        queue = deque([(start, 0, [start])])  # (node, distance, path)
        
        while queue:
            node, dist, path = queue.popleft()
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    
                    if neighbor == end:
                        return dist + 1, new_path
                    
                    queue.append((neighbor, dist + 1, new_path))
        
        return -1, []  # No path found
    
    @staticmethod
    def dijkstra(graph: Dict, start, end=None):
        """
        Dijkstra's algorithm for weighted graphs (non-negative weights)
        Time: O((V + E) log V), Space: O(V)
        Returns: distances dict and previous node dict
        """
        distances = {start: 0}
        previous = {}
        pq = [(0, start)]  # (distance, node)
        visited = set()
        
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if end and node == end:
                break
            
            for neighbor, weight in graph[node]:
                distance = curr_dist + weight
                
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = node
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, previous
    
    @staticmethod
    def reconstruct_path(previous: Dict, start, end):
        """Reconstruct path from previous dict"""
        path = []
        current = end
        
        while current != start:
            path.append(current)
            if current not in previous:
                return []  # No path exists
            current = previous[current]
        
        path.append(start)
        return path[::-1]


# ============================================================
# CONNECTED COMPONENTS
# ============================================================

class ConnectedComponents:
    """Find connected components"""
    
    @staticmethod
    def count_components(graph: Dict, n_vertices: int) -> int:
        """
        Count number of connected components
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for vertex in range(n_vertices):
            if vertex not in visited:
                dfs(vertex)
                count += 1
        
        return count
    
    @staticmethod
    def find_components(graph: Dict, n_vertices: int) -> List[List[int]]:
        """
        Find all connected components
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        components = []
        
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        for vertex in range(n_vertices):
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)
        
        return components


# ============================================================
# TOPOLOGICAL SORT
# ============================================================

class TopologicalSort:
    """Topological sort for DAG"""
    
    @staticmethod
    def kahn_algorithm(graph: Dict, n_vertices: int) -> List[int]:
        """
        Kahn's algorithm using BFS (removes nodes with indegree 0)
        Time: O(V + E), Space: O(V)
        """
        # Calculate in-degrees
        in_degree = [0] * n_vertices
        for u in graph:
            for v, _ in graph[u]:
                in_degree[v] += 1
        
        # Queue of nodes with no incoming edges
        queue = deque([i for i in range(n_vertices) if in_degree[i] == 0])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor, _ in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all nodes processed (no cycle)
        if len(result) != n_vertices:
            return []  # Cycle detected
        
        return result
    
    @staticmethod
    def dfs_based(graph: Dict, n_vertices: int) -> List[int]:
        """
        DFS-based topological sort
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        stack = []
        
        def dfs(node):
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)  # Add after visiting all descendants
        
        for vertex in range(n_vertices):
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]  # Reverse to get topological order


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":
    print("=== Graph Implementations Testing ===\n")
    
    # Create sample graph
    g = GraphAdjacencyList(directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    
    print("Graph edges:", g.edges())
    print()
    
    # Test DFS
    print("DFS (recursive):", GraphTraversal.dfs_recursive(g.adj, 0))
    print("DFS (iterative):", GraphTraversal.dfs_iterative(g.adj, 0))
    print()
    
    # Test BFS
    print("BFS:", GraphTraversal.bfs(g.adj, 0))
    print("BFS Level Order:", GraphTraversal.bfs_level_order(g.adj, 0))
    print()
    
    # Test shortest path
    dist, path = ShortestPath.bfs_shortest_path(g.adj, 0, 4)
    print(f"Shortest path from 0 to 4: distance={dist}, path={path}")
    print()
    
    # Test Dijkstra
    distances, previous = ShortestPath.dijkstra(g.adj, 0)
    print("Dijkstra distances from 0:", distances)
    path = ShortestPath.reconstruct_path(previous, 0, 4)
    print("Path from 0 to 4:", path)
    print()
    
    print("✅ All graph tests completed!")
