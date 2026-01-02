# 🌳 Binary Trees - Cây nhị phân

## 📖 Binary Tree là gì?

**Binary Tree** là cấu trúc dữ liệu phi tuyến (non-linear) trong đó:

- Mỗi node có **tối đa 2 children** (left & right)
- Có **1 root node** duy nhất
- Không có cycles

### Visual:

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

### Node Structure:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    # Left child
        self.right = right  # Right child
```

---

## 📊 Types of Binary Trees

### 1️⃣ **Full Binary Tree**

Mỗi node có **0 hoặc 2 children** (không có node với 1 child).

```
       1
      / \
     2   3
    / \
   4   5
```

### 2️⃣ **Complete Binary Tree**

Tất cả levels đầy **except possibly last level**, và last level filled **left to right**.

```
       1
      / \
     2   3
    / \  /
   4  5 6
```

✅ Used in: **Heaps**

### 3️⃣ **Perfect Binary Tree**

Tất cả **internal nodes có 2 children** và **all leaves ở cùng level**.

```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```

Properties:

- Nodes = 2^h - 1 (h = height)
- Leaves = 2^(h-1)

### 4️⃣ **Balanced Binary Tree**

Height của left và right subtrees differs by **at most 1**, and **both subtrees balanced**.

```
       1
      / \
     2   3
    / \
   4   5
```

✅ AVL Trees, Red-Black Trees

### 5️⃣ **Degenerate Tree** (Skewed)

Mỗi node chỉ có **1 child** → giống Linked List.

```
   1
    \
     2
      \
       3
```

❌ Worst case → O(n) operations

---

## ⚡ Binary Tree Properties

| Property                    | Formula/Value |
| --------------------------- | ------------- |
| **Max nodes at level L**    | 2^L           |
| **Max nodes with height h** | 2^h - 1       |
| **Min height** (n nodes)    | log₂(n+1)     |
| **Max height** (n nodes)    | n             |
| **Leaves in full tree**     | (n+1)/2       |

**Height vs Depth**:

- **Height**: Distance from node to deepest leaf (bottom-up)
- **Depth**: Distance from root to node (top-down)

```
       1  ← depth=0, height=2
      / \
     2   3  ← depth=1, height=1
    /
   4  ← depth=2, height=0
```

---

## 🚶 Tree Traversals

### Depth-First Search (DFS)

#### 1️⃣ **Inorder** (Left → Root → Right)

```
       1
      / \
     2   3
    / \
   4   5

Inorder: 4, 2, 5, 1, 3
```

**Use**: BST → sorted order

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

#### 2️⃣ **Preorder** (Root → Left → Right)

```
Preorder: 1, 2, 4, 5, 3
```

**Use**: Copy tree, prefix expression

```python
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
```

#### 3️⃣ **Postorder** (Left → Right → Root)

```
Postorder: 4, 5, 2, 3, 1
```

**Use**: Delete tree, postfix expression

```python
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

**Memory**: All DFS → **O(h) space** (recursion stack)

---

### Breadth-First Search (BFS)

#### **Level Order** (Level by Level)

```
       1
      / \
     2   3
    / \
   4   5

Level Order: 1, 2, 3, 4, 5
```

**Use**: Shortest path, level-wise processing

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
```

**Memory**: **O(w) space** where w = max width

---

## 🔄 DFS: Recursion vs Iteration

### Recursive (Clean & Simple)

```python
def inorder_recursive(root, result):
    if not root:
        return
    inorder_recursive(root.left, result)
    result.append(root.val)
    inorder_recursive(root.right, result)
```

### Iterative (Using Stack)

```python
def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        # Go to leftmost
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Go to right
        current = current.right

    return result
```

**When to use**:

- **Recursive**: Cleaner, easier to understand
- **Iterative**: Avoid stack overflow for deep trees

---

## 🎯 Common Patterns

### Pattern 1: Recursion with Return Value

**Template**:

```python
def solve(root):
    # Base case
    if not root:
        return base_value

    # Recursive calls
    left_result = solve(root.left)
    right_result = solve(root.right)

    # Combine results
    return combine(left_result, right_result, root.val)
```

**Examples**:

- Max depth
- Diameter
- Path sum

### Pattern 2: Recursion with Global Variable

**Template**:

```python
def solve(root):
    result = [initial_value]  # Mutable to modify in nested function

    def dfs(node):
        if not node:
            return

        # Update result
        result[0] = update(result[0], node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result[0]
```

**Examples**:

- Maximum path sum
- Count nodes

### Pattern 3: Level-by-Level Processing

**Template**:

```python
def level_process(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level_result = []

        for _ in range(level_size):
            node = queue.popleft()
            level_result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_result)

    return result
```

**Examples**:

- Level order traversal
- Zigzag traversal
- Right side view

### Pattern 4: Path Tracking

**Template**:

```python
def find_paths(root, target):
    def dfs(node, path, paths):
        if not node:
            return

        path.append(node.val)

        # Check if leaf and target reached
        if not node.left and not node.right and sum(path) == target:
            paths.append(path[:])  # Copy path

        dfs(node.left, path, paths)
        dfs(node.right, path, paths)

        path.pop()  # Backtrack

    paths = []
    dfs(root, [], paths)
    return paths
```

**Examples**:

- Root to leaf paths
- Path sum II
- Binary tree paths

---

## 💡 Common Problems & Solutions

### Problem 1: Maximum Depth

```python
def max_depth(root):
    """
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)
```

### Problem 2: Invert Binary Tree

```python
def invert_tree(root):
    """
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root
```

### Problem 3: Diameter of Tree

```python
def diameter(root):
    """
    Longest path between any two nodes
    Time: O(n)
    Space: O(h)
    """
    diameter = [0]

    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        # Update diameter
        diameter[0] = max(diameter[0], left_h + right_h)

        return 1 + max(left_h, right_h)

    height(root)
    return diameter[0]
```

### Problem 4: Balanced Binary Tree

```python
def is_balanced(root):
    """
    Check if height-balanced
    Time: O(n)
    Space: O(h)
    """
    def check(node):
        if not node:
            return 0

        left_h = check(node.left)
        if left_h == -1:
            return -1

        right_h = check(node.right)
        if right_h == -1:
            return -1

        # Check balance condition
        if abs(left_h - right_h) > 1:
            return -1

        return 1 + max(left_h, right_h)

    return check(root) != -1
```

### Problem 5: Same Tree

```python
def is_same_tree(p, q):
    """
    Check if two trees are identical
    Time: O(n)
    Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))
```

### Problem 6: Symmetric Tree

```python
def is_symmetric(root):
    """
    Check if tree is mirror of itself
    Time: O(n)
    Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right) if root else True
```

### Problem 7: Path Sum

```python
def has_path_sum(root, target_sum):
    """
    Check if root-to-leaf path sums to target
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return False

    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum

    # Recurse with remaining sum
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))
```

### Problem 8: Lowest Common Ancestor

```python
def lowest_common_ancestor(root, p, q):
    """
    Find LCA of two nodes
    Time: O(n)
    Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both sides found, root is LCA
    if left and right:
        return root

    # Return whichever is not None
    return left if left else right
```

---

## 📊 Time & Space Complexity Summary

| Operation         | Average    | Worst | Space |
| ----------------- | ---------- | ----- | ----- |
| **DFS Traversal** | O(n)       | O(n)  | O(h)  |
| **BFS Traversal** | O(n)       | O(n)  | O(w)  |
| **Search**        | O(n)       | O(n)  | O(h)  |
| **Insert**        | O(log n)\* | O(n)  | O(1)  |
| **Delete**        | O(log n)\* | O(n)  | O(1)  |

\*For balanced trees. Unbalanced → O(n)

**h = height, w = width, n = nodes**

---

## 🎓 Key Takeaways

### 1. Traversals:

- **Inorder**: Left → Root → Right (BST sorted)
- **Preorder**: Root → Left → Right (copy tree)
- **Postorder**: Left → Right → Root (delete tree)
- **Level Order**: BFS with queue

### 2. Complexity:

- **DFS**: O(h) space (recursion stack)
- **BFS**: O(w) space (queue width)
- All traversals: **O(n) time**

### 3. Common Patterns:

- Recursion with return value
- Recursion with global variable
- Level-by-level processing
- Path tracking with backtracking

### 4. When to Use:

- **Recursion**: Clean, natural for trees
- **Iteration**: Avoid stack overflow
- **BFS**: Level-wise, shortest path
- **DFS**: Path finding, subtree problems

---

## ⚠️ Common Pitfalls

1. **Forgetting null checks**

   ```python
   # ❌ BAD
   if root.left:
       process(root.left.val)

   # ✅ GOOD
   if root and root.left:
       process(root.left.val)
   ```

2. **Not handling single node**

   ```python
   # ❌ BAD - assumes children exist
   return max(left, right)

   # ✅ GOOD - handle None
   return max(left or 0, right or 0)
   ```

3. **Path tracking without backtracking**

   ```python
   # ❌ BAD
   path.append(node.val)
   dfs(node.left)
   dfs(node.right)
   # Forgot to remove!

   # ✅ GOOD
   path.append(node.val)
   dfs(node.left)
   dfs(node.right)
   path.pop()  # Backtrack
   ```

4. **Copying vs Referencing**

   ```python
   # ❌ BAD - all refer to same list
   paths.append(path)

   # ✅ GOOD - append copy
   paths.append(path[:])
   ```

---

## ➡️ Next Steps

- 💻 Xem [Implementation Code](implementation.py)
- 📝 Làm [Practice Problems](practice.md)
- 📖 Đọc tiếp [Binary Search Trees](../bst/theory.md)

**Trees are fundamental - master them! 🚀**
