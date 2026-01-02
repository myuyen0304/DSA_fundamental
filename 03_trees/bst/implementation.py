"""
BINARY SEARCH TREE (BST) - IMPLEMENTATION
==========================================

Module này implement Binary Search Tree với các operations:
1. BST Node và Tree class
2. Search, Insert, Delete
3. Min, Max, Successor, Predecessor
4. Validation và conversion utilities
5. Common BST problems

Time Complexity Summary:
- Search, Insert, Delete: O(h) where h = height
- Balanced BST: O(log n)
- Skewed BST: O(n)

Author: DSA Learning
"""

from typing import Optional, List
from collections import deque


# ============================================================================
# TREE NODE CLASS
# ============================================================================

class TreeNode:
    """
    Node cho Binary Search Tree
    """
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


# ============================================================================
# BINARY SEARCH TREE CLASS
# ============================================================================

class BST:
    """
    Binary Search Tree with all standard operations
    
    Properties:
        - Left subtree values < node value
        - Right subtree values > node value
        - No duplicates (by convention)
    """
    
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root
    
    # ========================================================================
    # CORE OPERATIONS
    # ========================================================================
    
    def search(self, val: int) -> Optional[TreeNode]:
        """
        Search for value in BST
        
        Time: O(h), Space: O(1)
        
        Args:
            val: Value to search for
            
        Returns:
            Node with value, or None if not found
            
        Example:
            BST: 8, 3, 10, 1, 6, 14
            search(6) → TreeNode(6)
            search(5) → None
        """
        curr = self.root
        
        while curr:
            if val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        return None
    
    def search_recursive(self, val: int, node: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """
        Search recursively
        Time: O(h), Space: O(h) due to recursion stack
        """
        if node is None:
            node = self.root
        
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self.search_recursive(val, node.left)
        else:
            return self.search_recursive(val, node.right)
    
    def insert(self, val: int) -> TreeNode:
        """
        Insert value into BST (iterative)
        
        Time: O(h), Space: O(1)
        
        Args:
            val: Value to insert
            
        Returns:
            Root of BST
            
        Example:
            BST: 8, 3, 10
            insert(6)
            Result: 8, 3, 10, 6
        """
        if not self.root:
            self.root = TreeNode(val)
            return self.root
        
        curr = self.root
        
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            elif val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
            else:
                # Duplicate value - skip
                break
        
        return self.root
    
    def insert_recursive(self, val: int, node: Optional[TreeNode] = None) -> TreeNode:
        """
        Insert recursively
        Time: O(h), Space: O(h)
        """
        if node is None:
            if self.root is None:
                self.root = TreeNode(val)
                return self.root
            node = self.root
        
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self.insert_recursive(val, node.left)
        elif val > node.val:
            node.right = self.insert_recursive(val, node.right)
        
        return node
    
    def delete(self, val: int) -> Optional[TreeNode]:
        """
        Delete value from BST
        
        Time: O(h), Space: O(h) for recursion
        
        3 Cases:
            1. Node is leaf → simply remove
            2. Node has 1 child → replace with child
            3. Node has 2 children → replace with successor
            
        Args:
            val: Value to delete
            
        Returns:
            Root of BST after deletion
            
        Example:
            BST: 8, 3, 10, 1, 6, 14
            delete(3)
            Result: 8, 6, 10, 1, 14 (successor 6 replaces 3)
        """
        self.root = self._delete_helper(self.root, val)
        return self.root
    
    def _delete_helper(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Helper function for delete"""
        if not node:
            return None
        
        # Find node to delete
        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        else:
            # Found node to delete
            
            # Case 1: Leaf node or Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Case 3: Two children
            # Find successor (minimum in right subtree)
            successor = self._find_min(node.right)
            node.val = successor.val
            # Delete successor from right subtree
            node.right = self._delete_helper(node.right, successor.val)
        
        return node
    
    # ========================================================================
    # MIN, MAX, SUCCESSOR, PREDECESSOR
    # ========================================================================
    
    def find_min(self) -> Optional[TreeNode]:
        """
        Find minimum value node (leftmost)
        Time: O(h), Space: O(1)
        """
        return self._find_min(self.root)
    
    def _find_min(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """Helper: find min starting from given node"""
        if not node:
            return None
        
        while node.left:
            node = node.left
        return node
    
    def find_max(self) -> Optional[TreeNode]:
        """
        Find maximum value node (rightmost)
        Time: O(h), Space: O(1)
        """
        if not self.root:
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr
    
    def find_successor(self, node: TreeNode) -> Optional[TreeNode]:
        """
        Find inorder successor of node
        Successor = next larger value
        
        Time: O(h), Space: O(1)
        
        Cases:
            1. Node has right child → successor = min(right subtree)
            2. No right child → successor = lowest ancestor where node is in left subtree
        """
        # Case 1: Has right subtree
        if node.right:
            return self._find_min(node.right)
        
        # Case 2: Go up to find ancestor
        # Need parent pointers (not implemented in basic BST)
        # Alternative: store path during search
        return None
    
    def find_predecessor(self, node: TreeNode) -> Optional[TreeNode]:
        """
        Find inorder predecessor of node
        Predecessor = previous smaller value
        
        Time: O(h), Space: O(1)
        """
        # Has left subtree → predecessor = max(left subtree)
        if node.left:
            curr = node.left
            while curr.right:
                curr = curr.right
            return curr
        
        # Need parent pointers for full implementation
        return None
    
    # ========================================================================
    # VALIDATION & PROPERTIES
    # ========================================================================
    
    def is_valid_bst(self) -> bool:
        """
        Validate if tree is valid BST
        
        Time: O(n), Space: O(h)
        
        Common mistake: Only checking node.left < node < node.right
        Correct: Check entire subtree ranges
        
        Example (Invalid):
                5
               / \
              3   7
                 / \
                4   8    ← 4 < 5 but in right subtree!
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
            
            # Check current node value
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Check subtrees with updated ranges
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(self.root, float('-inf'), float('inf'))
    
    def is_valid_bst_inorder(self) -> bool:
        """
        Alternative validation using inorder traversal
        Inorder of BST must be strictly increasing
        
        Time: O(n), Space: O(h)
        """
        prev = [float('-inf')]
        
        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            
            # Check if increasing
            if node.val <= prev[0]:
                return False
            prev[0] = node.val
            
            return inorder(node.right)
        
        return inorder(self.root)
    
    def height(self) -> int:
        """
        Calculate height of BST
        Time: O(n), Space: O(h)
        """
        def calc_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(calc_height(node.left), calc_height(node.right))
        
        return calc_height(self.root)
    
    def size(self) -> int:
        """
        Count total nodes
        Time: O(n), Space: O(h)
        """
        def count(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)
        
        return count(self.root)
    
    # ========================================================================
    # TRAVERSALS
    # ========================================================================
    
    def inorder(self) -> List[int]:
        """
        Inorder traversal (Left → Root → Right)
        For BST: Returns SORTED values
        
        Time: O(n), Space: O(h)
        """
        result = []
        
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        
        traverse(self.root)
        return result
    
    def preorder(self) -> List[int]:
        """Preorder traversal (Root → Left → Right)"""
        result = []
        
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(self.root)
        return result
    
    def level_order(self) -> List[List[int]]:
        """Level order traversal (BFS)"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
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
    
    # ========================================================================
    # RANGE QUERIES
    # ========================================================================
    
    def range_search(self, low: int, high: int) -> List[int]:
        """
        Find all values in range [low, high]
        
        Time: O(h + k) where k = number of results
        Space: O(h)
        
        Optimization: Skip subtrees outside range
        """
        result = []
        
        def search_range(node: Optional[TreeNode]):
            if not node:
                return
            
            # If current node too small, skip left subtree
            if node.val > low:
                search_range(node.left)
            
            # If in range, add to result
            if low <= node.val <= high:
                result.append(node.val)
            
            # If current node too large, skip right subtree
            if node.val < high:
                search_range(node.right)
        
        search_range(self.root)
        return result
    
    # ========================================================================
    # COMMON BST PROBLEMS
    # ========================================================================
    
    def kth_smallest(self, k: int) -> Optional[int]:
        """
        Find kth smallest element (1-indexed)
        
        Time: O(h + k), Space: O(h)
        
        Strategy: Inorder traversal (gives sorted order), stop at kth
        """
        count = [0]
        result = [None]
        
        def inorder(node: Optional[TreeNode]):
            if not node or result[0] is not None:
                return
            
            inorder(node.left)
            
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            
            inorder(node.right)
        
        inorder(self.root)
        return result[0]
    
    def kth_largest(self, k: int) -> Optional[int]:
        """
        Find kth largest element
        
        Time: O(h + k), Space: O(h)
        
        Strategy: Reverse inorder (Right → Root → Left)
        """
        count = [0]
        result = [None]
        
        def reverse_inorder(node: Optional[TreeNode]):
            if not node or result[0] is not None:
                return
            
            reverse_inorder(node.right)  # Largest first
            
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            
            reverse_inorder(node.left)
        
        reverse_inorder(self.root)
        return result[0]
    
    def lowest_common_ancestor(self, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Find LCA of two nodes in BST
        
        Time: O(h), Space: O(1) iterative
        
        BST optimization: Use value comparison!
        - Both < node → LCA in left
        - Both > node → LCA in right
        - Otherwise → node is LCA
        """
        curr = self.root
        
        while curr:
            # Both in left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Both in right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Split point - found LCA
            else:
                return curr
        
        return None
    
    # ========================================================================
    # CONSTRUCTION & CONVERSION
    # ========================================================================
    
    def from_sorted_array(self, nums: List[int]) -> TreeNode:
        """
        Build balanced BST from sorted array
        
        Time: O(n), Space: O(log n)
        
        Strategy: Middle element = root, recursively build left/right
        """
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            
            return node
        
        self.root = build(0, len(nums) - 1)
        return self.root
    
    def to_sorted_array(self) -> List[int]:
        """
        Convert BST to sorted array
        Simply inorder traversal
        
        Time: O(n), Space: O(n)
        """
        return self.inorder()
    
    # ========================================================================
    # UTILITY FUNCTIONS
    # ========================================================================
    
    def print_tree(self, node: Optional[TreeNode] = None, level: int = 0, prefix: str = "Root: "):
        """Print tree structure visually"""
        if node is None:
            node = self.root
        
        if node:
            print(" " * (level * 4) + prefix + str(node.val))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# ============================================================================
# EXAMPLES & TESTING
# ============================================================================

def example_basic_operations():
    """Example: Basic BST operations"""
    print("=" * 60)
    print("EXAMPLE 1: BASIC OPERATIONS")
    print("=" * 60)
    
    bst = BST()
    
    # Insert values
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print(f"\nInserting values: {values}")
    
    for val in values:
        bst.insert(val)
    
    print("\nBST Structure:")
    bst.print_tree()
    
    # Traversals
    print(f"\nInorder (sorted): {bst.inorder()}")
    print(f"Preorder: {bst.preorder()}")
    print(f"Level Order: {bst.level_order()}")
    
    # Search
    print("\n" + "-" * 60)
    print("Search Operations:")
    print(f"Search 6: {bst.search(6)}")
    print(f"Search 5: {bst.search(5)}")
    
    # Min/Max
    print(f"\nMin value: {bst.find_min().val}")
    print(f"Max value: {bst.find_max().val}")
    
    # Properties
    print(f"\nHeight: {bst.height()}")
    print(f"Size: {bst.size()}")
    print(f"Is Valid BST: {bst.is_valid_bst()}")


def example_delete_operations():
    """Example: Delete operations"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: DELETE OPERATIONS")
    print("=" * 60)
    
    bst = BST()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        bst.insert(val)
    
    print("\nOriginal BST:")
    bst.print_tree()
    print(f"Inorder: {bst.inorder()}")
    
    # Delete leaf
    print("\n" + "-" * 60)
    print("Delete 1 (leaf node):")
    bst.delete(1)
    bst.print_tree()
    print(f"Inorder: {bst.inorder()}")
    
    # Delete node with one child
    print("\n" + "-" * 60)
    print("Delete 14 (one child):")
    bst.delete(14)
    bst.print_tree()
    print(f"Inorder: {bst.inorder()}")
    
    # Delete node with two children
    print("\n" + "-" * 60)
    print("Delete 3 (two children):")
    bst.delete(3)
    bst.print_tree()
    print(f"Inorder: {bst.inorder()}")


def example_kth_and_lca():
    """Example: Kth smallest/largest and LCA"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: KTH ELEMENT & LCA")
    print("=" * 60)
    
    bst = BST()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        bst.insert(val)
    
    print(f"\nBST values (sorted): {bst.inorder()}")
    
    # Kth smallest/largest
    print("\nKth Smallest:")
    for k in [1, 3, 5]:
        print(f"  {k}th smallest: {bst.kth_smallest(k)}")
    
    print("\nKth Largest:")
    for k in [1, 3, 5]:
        print(f"  {k}th largest: {bst.kth_largest(k)}")
    
    # LCA
    print("\n" + "-" * 60)
    print("Lowest Common Ancestor:")
    node1 = bst.search(1)
    node4 = bst.search(4)
    node13 = bst.search(13)
    
    lca = bst.lowest_common_ancestor(node1, node4)
    print(f"  LCA(1, 4) = {lca.val if lca else None}")
    
    lca = bst.lowest_common_ancestor(node1, node13)
    print(f"  LCA(1, 13) = {lca.val if lca else None}")


def example_range_and_conversion():
    """Example: Range search and array conversion"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: RANGE SEARCH & CONVERSION")
    print("=" * 60)
    
    # Build from sorted array
    sorted_array = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print(f"\nBuild BST from sorted array: {sorted_array}")
    
    bst = BST()
    bst.from_sorted_array(sorted_array)
    
    print("\nBalanced BST structure:")
    bst.print_tree()
    
    # Range search
    print("\n" + "-" * 60)
    print("Range Search:")
    print(f"  Range [4, 10]: {bst.range_search(4, 10)}")
    print(f"  Range [1, 5]: {bst.range_search(1, 5)}")
    print(f"  Range [10, 20]: {bst.range_search(10, 20)}")
    
    # Convert back to sorted array
    print(f"\nConvert to sorted array: {bst.to_sorted_array()}")


def run_all_examples():
    """Run all examples"""
    example_basic_operations()
    example_delete_operations()
    example_kth_and_lca()
    example_range_and_conversion()
    
    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_examples()
