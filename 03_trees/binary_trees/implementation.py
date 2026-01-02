"""
Binary Trees - Implementation & Core Operations
Complete implementations with traversals and common problems
"""

from typing import Optional, List
from collections import deque


# ============================================================
# TREE NODE CLASS
# ============================================================

class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


# ============================================================
# TREE TRAVERSALS
# ============================================================

class TreeTraversal:
    """All tree traversal methods"""
    
    @staticmethod
    def inorder(root: Optional[TreeNode]) -> List[int]:
        """
        Inorder: Left → Root → Right
        For BST: gives sorted order
        Time: O(n), Space: O(h) - h = height
        """
        result = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)      # Left
            result.append(node.val)  # Root
            traverse(node.right)     # Right
        
        traverse(root)
        return result
    
    @staticmethod
    def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
        """
        Inorder iterative using stack
        Time: O(n), Space: O(h)
        """
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Go to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process node
            curr = stack.pop()
            result.append(curr.val)
            
            # Go to right
            curr = curr.right
        
        return result
    
    @staticmethod
    def preorder(root: Optional[TreeNode]) -> List[int]:
        """
        Preorder: Root → Left → Right
        Use for: copying tree, prefix expression
        Time: O(n), Space: O(h)
        """
        result = []
        
        def traverse(node):
            if not node:
                return
            result.append(node.val)  # Root
            traverse(node.left)      # Left
            traverse(node.right)     # Right
        
        traverse(root)
        return result
    
    @staticmethod
    def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
        """
        Preorder iterative using stack
        Time: O(n), Space: O(h)
        """
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push right first (so left is processed first)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
    
    @staticmethod
    def postorder(root: Optional[TreeNode]) -> List[int]:
        """
        Postorder: Left → Right → Root
        Use for: deleting tree, postfix expression
        Time: O(n), Space: O(h)
        """
        result = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)      # Left
            traverse(node.right)     # Right
            result.append(node.val)  # Root
        
        traverse(root)
        return result
    
    @staticmethod
    def levelorder(root: Optional[TreeNode]) -> List[List[int]]:
        """
        Level Order (BFS): Process level by level
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


# ============================================================
# TREE PROPERTIES
# ============================================================

class TreeProperties:
    """Calculate tree properties"""
    
    @staticmethod
    def height(root: Optional[TreeNode]) -> int:
        """
        Calculate height of tree
        Height = longest path from root to leaf
        Time: O(n), Space: O(h)
        """
        if not root:
            return 0
        
        left_height = TreeProperties.height(root.left)
        right_height = TreeProperties.height(root.right)
        
        return 1 + max(left_height, right_height)
    
    @staticmethod
    def size(root: Optional[TreeNode]) -> int:
        """
        Count total nodes in tree
        Time: O(n), Space: O(h)
        """
        if not root:
            return 0
        
        return 1 + TreeProperties.size(root.left) + TreeProperties.size(root.right)
    
    @staticmethod
    def is_balanced(root: Optional[TreeNode]) -> bool:
        """
        Check if tree is height-balanced
        Balanced: |height(left) - height(right)| <= 1 for all nodes
        Time: O(n), Space: O(h)
        """
        def check_height(node):
            if not node:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree unbalanced
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree unbalanced
            
            # Check current node balance
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return check_height(root) != -1
    
    @staticmethod
    def diameter(root: Optional[TreeNode]) -> int:
        """
        Find diameter (longest path between any 2 nodes)
        Time: O(n), Space: O(h)
        """
        diameter = [0]  # Use list to modify in nested function
        
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
    
    @staticmethod
    def max_path_sum(root: Optional[TreeNode]) -> int:
        """
        Find maximum path sum (can start/end anywhere)
        Time: O(n), Space: O(h)
        """
        max_sum = [float('-inf')]
        
        def max_gain(node):
            if not node:
                return 0
            
            # Max sum on left and right (take 0 if negative)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price to start new path including current node
            price_newpath = node.val + left_gain + right_gain
            max_sum[0] = max(max_sum[0], price_newpath)
            
            # Return max gain if continue path with this node
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return max_sum[0]


# ============================================================
# TREE CONSTRUCTION
# ============================================================

class TreeConstruction:
    """Build trees from traversals"""
    
    @staticmethod
    def from_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build tree from preorder and inorder traversals
        Time: O(n), Space: O(n)
        """
        if not preorder or not inorder:
            return None
        
        # First element in preorder is root
        root = TreeNode(preorder[0])
        
        # Find root in inorder
        mid = inorder.index(preorder[0])
        
        # Recursively build left and right subtrees
        root.left = TreeConstruction.from_preorder_inorder(
            preorder[1:mid+1], inorder[:mid]
        )
        root.right = TreeConstruction.from_preorder_inorder(
            preorder[mid+1:], inorder[mid+1:]
        )
        
        return root
    
    @staticmethod
    def from_inorder_postorder(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Build tree from inorder and postorder traversals
        Time: O(n), Space: O(n)
        """
        if not inorder or not postorder:
            return None
        
        # Last element in postorder is root
        root = TreeNode(postorder[-1])
        
        # Find root in inorder
        mid = inorder.index(postorder[-1])
        
        # Recursively build left and right subtrees
        root.left = TreeConstruction.from_inorder_postorder(
            inorder[:mid], postorder[:mid]
        )
        root.right = TreeConstruction.from_inorder_postorder(
            inorder[mid+1:], postorder[mid:-1]
        )
        
        return root


# ============================================================
# TREE COMPARISONS
# ============================================================

class TreeComparison:
    """Compare trees"""
    
    @staticmethod
    def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two trees are identical
        Time: O(n), Space: O(h)
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return (p.val == q.val and 
                TreeComparison.is_same_tree(p.left, q.left) and
                TreeComparison.is_same_tree(p.right, q.right))
    
    @staticmethod
    def is_symmetric(root: Optional[TreeNode]) -> bool:
        """
        Check if tree is mirror of itself (symmetric)
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
    
    @staticmethod
    def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if subRoot is subtree of root
        Time: O(m * n), Space: O(h)
        """
        if not root:
            return False
        
        if TreeComparison.is_same_tree(root, subRoot):
            return True
        
        return (TreeComparison.is_subtree(root.left, subRoot) or
                TreeComparison.is_subtree(root.right, subRoot))


# ============================================================
# TREE VIEWS
# ============================================================

class TreeViews:
    """Different views of tree"""
    
    @staticmethod
    def right_side_view(root: Optional[TreeNode]) -> List[int]:
        """
        Right side view (rightmost node at each level)
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
    
    @staticmethod
    def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
        """
        Zigzag level order traversal
        Time: O(n), Space: O(w)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add to current level based on direction
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(current_level))
            left_to_right = not left_to_right
        
        return result


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build tree from level-order list representation
    None represents missing node
    
    Example: [1,2,3,None,None,4,5] creates:
           1
          / \
         2   3
            / \
           4   5
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def print_tree(root: Optional[TreeNode], level=0, prefix="Root: "):
    """
    Print tree structure visually
    """
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":
    # Create sample tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = build_tree_from_list([1, 2, 3, 4, 5])
    
    print("Tree Structure:")
    print_tree(root)
    print()
    
    # Test traversals
    print("Inorder:", TreeTraversal.inorder(root))
    print("Preorder:", TreeTraversal.preorder(root))
    print("Postorder:", TreeTraversal.postorder(root))
    print("Level Order:", TreeTraversal.levelorder(root))
    print()
    
    # Test properties
    print("Height:", TreeProperties.height(root))
    print("Size:", TreeProperties.size(root))
    print("Is Balanced:", TreeProperties.is_balanced(root))
    print("Diameter:", TreeProperties.diameter(root))
    print()
    
    # Test views
    print("Right Side View:", TreeViews.right_side_view(root))
    print()
    
    print("✅ All tests completed!")
