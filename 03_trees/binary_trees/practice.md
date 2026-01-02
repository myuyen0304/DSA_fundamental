# 🌳 Binary Trees - Practice Problems

## 📚 Learning Objectives

After completing these problems, you should be able to:
- ✅ Implement all tree traversals (Inorder, Preorder, Postorder, Level Order)
- ✅ Calculate tree properties (height, diameter, balance)
- ✅ Solve path and view problems
- ✅ Handle tree construction and comparison

---

## 🎯 Problem Categories

### **Category 1: Tree Traversals** (Easy)
### **Category 2: Tree Properties** (Easy-Medium)
### **Category 3: Path Problems** (Medium)
### **Category 4: Tree Construction** (Medium)
### **Category 5: Tree Views** (Medium)

---

## 📝 Problems

### **Category 1: Tree Traversals**

#### Problem 1: Binary Tree Inorder Traversal ⭐
**Difficulty**: Easy | **Pattern**: DFS Recursive/Iterative

**Problem**: Return inorder traversal of binary tree.

**Example**:
```
Input:    1
           \
            2
           /
          3
Output: [1,3,2]
```

**Hints**:
- Left → Root → Right
- Try both recursive and iterative approaches

<details>
<summary>Solution 1: Recursive</summary>

```python
def inorderTraversal(root):
    """
    Time: O(n), Space: O(h)
    """
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return result
```
</details>

<details>
<summary>Solution 2: Iterative with Stack</summary>

```python
def inorderTraversal(root):
    """
    Time: O(n), Space: O(h)
    """
    result = []
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    
    return result
```
</details>

---

#### Problem 2: Binary Tree Level Order Traversal ⭐⭐
**Difficulty**: Medium | **Pattern**: BFS

**Problem**: Return level order traversal (level by level, left to right).

**Example**:
```
Input:    3
         / \
        9  20
          /  \
         15   7
Output: [[3],[9,20],[15,7]]
```

**Hints**:
- Use queue for BFS
- Process one level at a time

<details>
<summary>Solution</summary>

```python
from collections import deque

def levelOrder(root):
    """
    Time: O(n), Space: O(w) - w = max width
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```
</details>

---

### **Category 2: Tree Properties**

#### Problem 3: Maximum Depth of Binary Tree ⭐
**Difficulty**: Easy | **Pattern**: DFS/BFS

**Problem**: Find maximum depth (number of nodes along longest path from root to leaf).

**Example**:
```
Input:    3
         / \
        9  20
          /  \
         15   7
Output: 3
```

**Hints**:
- Depth = 1 + max(left_depth, right_depth)

<details>
<summary>Solution 1: Recursive DFS</summary>

```python
def maxDepth(root):
    """
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)
```
</details>

<details>
<summary>Solution 2: BFS Level Order</summary>

```python
from collections import deque

def maxDepth(root):
    """
    Time: O(n), Space: O(w)
    """
    if not root:
        return 0
    
    depth = 0
    queue = deque([root])
    
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth
```
</details>

---

#### Problem 4: Balanced Binary Tree ⭐⭐
**Difficulty**: Easy | **Pattern**: DFS with Height Check

**Problem**: Check if tree is height-balanced (left and right subtrees differ by at most 1 in height).

**Example**:
```
Input:    3
         / \
        9  20
          /  \
         15   7
Output: true
```

**Hints**:
- Calculate height while checking balance
- Return -1 if unbalanced

<details>
<summary>Solution</summary>

```python
def isBalanced(root):
    """
    Time: O(n), Space: O(h)
    """
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1
```
</details>

---

#### Problem 5: Diameter of Binary Tree ⭐⭐⭐
**Difficulty**: Easy-Medium | **Pattern**: DFS

**Problem**: Find diameter (length of longest path between any two nodes).

**Example**:
```
Input:    1
         / \
        2   3
       / \
      4   5
Output: 3  (path: 4→2→1→3 or 5→2→1→3)
```

**Hints**:
- Diameter through node = left_height + right_height
- Calculate height while tracking max diameter

<details>
<summary>Solution</summary>

```python
def diameterOfBinaryTree(root):
    """
    Time: O(n), Space: O(h)
    """
    diameter = [0]
    
    def height(node):
        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)
        
        # Update diameter
        diameter[0] = max(diameter[0], left + right)
        
        return 1 + max(left, right)
    
    height(root)
    return diameter[0]
```
</details>

---

### **Category 3: Path Problems**

#### Problem 6: Path Sum ⭐⭐
**Difficulty**: Easy | **Pattern**: DFS

**Problem**: Check if tree has root-to-leaf path with given sum.

**Example**:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true  (path: 5→4→11→2)
```

**Hints**:
- Subtract node value from target
- Check if leaf and sum equals target

<details>
<summary>Solution</summary>

```python
def hasPathSum(root, targetSum):
    """
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    # Leaf node
    if not root.left and not root.right:
        return root.val == targetSum
    
    # Check left and right subtrees
    return (hasPathSum(root.left, targetSum - root.val) or
            hasPathSum(root.right, targetSum - root.val))
```
</details>

---

#### Problem 7: Binary Tree Maximum Path Sum ⭐⭐⭐⭐⭐
**Difficulty**: Hard | **Pattern**: DFS with Global Max

**Problem**: Find maximum path sum between any two nodes.

**Example**:
```
Input:   -10
         /  \
        9   20
           /  \
          15   7
Output: 42  (path: 15→20→7)
```

**Hints**:
- At each node, consider: node only, node + left, node + right, or all three
- Track global maximum

<details>
<summary>Solution</summary>

```python
def maxPathSum(root):
    """
    Time: O(n), Space: O(h)
    """
    max_sum = [float('-inf')]
    
    def max_gain(node):
        if not node:
            return 0
        
        # Max sum from left and right (ignore if negative)
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Path through current node
        path_sum = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], path_sum)
        
        # Return max gain if continuing path
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum[0]
```
</details>

---

### **Category 4: Tree Construction**

#### Problem 8: Construct Binary Tree from Preorder and Inorder ⭐⭐⭐
**Difficulty**: Medium | **Pattern**: Divide & Conquer

**Problem**: Build tree from preorder and inorder traversal arrays.

**Example**:
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output:    3
          / \
         9  20
           /  \
          15   7
```

**Hints**:
- First element in preorder is root
- Find root in inorder to split left/right subtrees

<details>
<summary>Solution</summary>

```python
def buildTree(preorder, inorder):
    """
    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None
    
    # First element in preorder is root
    root = TreeNode(preorder[0])
    
    # Find root in inorder to split
    mid = inorder.index(preorder[0])
    
    # Build recursively
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    
    return root
```
</details>

---

#### Problem 9: Serialize and Deserialize Binary Tree ⭐⭐⭐⭐
**Difficulty**: Hard | **Pattern**: DFS/BFS Encoding

**Problem**: Convert tree to string and back.

**Example**:
```
Input:    1
         / \
        2   3
           / \
          4   5
Output: "1,2,None,None,3,4,None,None,5,None,None"
```

<details>
<summary>Solution</summary>

```python
class Codec:
    def serialize(self, root):
        """Encode tree to string"""
        def helper(node):
            if not node:
                return "None,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)
        return helper(root)
    
    def deserialize(self, data):
        """Decode string to tree"""
        def helper(nodes):
            val = next(nodes)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = helper(nodes)
            node.right = helper(nodes)
            return node
        
        return helper(iter(data.split(',')))
```
</details>

---

### **Category 5: Tree Views & Comparisons**

#### Problem 10: Same Tree ⭐
**Difficulty**: Easy | **Pattern**: DFS Comparison

**Problem**: Check if two trees are identical.

**Hints**:
- Compare values and recursively check subtrees

<details>
<summary>Solution</summary>

```python
def isSameTree(p, q):
    """
    Time: O(n), Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))
```
</details>

---

#### Problem 11: Symmetric Tree ⭐⭐
**Difficulty**: Easy | **Pattern**: DFS Mirror Check

**Problem**: Check if tree is mirror of itself.

**Example**:
```
Input:    1
         / \
        2   2
       / \ / \
      3  4 4  3
Output: true
```

<details>
<summary>Solution</summary>

```python
def isSymmetric(root):
    """
    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root)
```
</details>

---

#### Problem 12: Binary Tree Right Side View ⭐⭐
**Difficulty**: Medium | **Pattern**: BFS/DFS

**Problem**: Return values of rightmost node at each level.

**Example**:
```
Input:    1
         / \
        2   3
         \   \
          5   4
Output: [1,3,4]
```

<details>
<summary>Solution</summary>

```python
from collections import deque

def rightSideView(root):
    """
    Time: O(n), Space: O(w)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Last node in level
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result
```
</details>

---

## 🎯 More Practice Problems

### **Easy Problems**:
13. Invert Binary Tree
14. Minimum Depth of Binary Tree
15. Subtree of Another Tree
16. Count Complete Tree Nodes

### **Medium Problems**:
17. Lowest Common Ancestor of Binary Tree
18. Validate Binary Search Tree
19. Binary Tree Zigzag Level Order Traversal
20. Kth Smallest Element in BST
21. Flatten Binary Tree to Linked List
22. Populating Next Right Pointers

### **Hard Problems**:
23. Binary Tree Maximum Path Sum
24. Recover Binary Search Tree
25. Count of Smaller Numbers After Self

---

## 📊 Key Patterns Summary

### **1. DFS Traversal Template**
```python
def dfs(node):
    if not node:
        return
    
    # Preorder: process here
    dfs(node.left)
    # Inorder: process here
    dfs(node.right)
    # Postorder: process here
```

### **2. BFS Level Order Template**
```python
from collections import deque

queue = deque([root])
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        # Process node
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

### **3. Height Calculation**
```python
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

### **4. Path Sum Pattern**
```python
def hasPath(node, target):
    if not node:
        return False
    if not node.left and not node.right:  # Leaf
        return node.val == target
    return (hasPath(node.left, target - node.val) or
            hasPath(node.right, target - node.val))
```

---

## 🚀 Next Steps

After mastering binary trees:
1. ✅ Move to [Binary Search Trees](../bst/theory.md)
2. ✅ Practice on [LeetCode Tree Problems](https://leetcode.com/tag/tree/)
3. ✅ Review [Tree Patterns](../../resources/patterns/common_patterns.md)

**Good luck! 🌳**
