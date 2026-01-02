# BINARY SEARCH TREE (BST)

## 📖 MỤC LỤC

1. [Giới thiệu](#giới-thiệu)
2. [BST Properties](#bst-properties)
3. [Operations & Time Complexity](#operations--time-complexity)
4. [Khi nào dùng BST](#khi-nào-dùng-bst)
5. [BST vs Binary Tree](#bst-vs-binary-tree)
6. [Common Problems](#common-problems)

---

## GIỚI THIỆU

**Binary Search Tree (BST)** là binary tree đặc biệt có thêm constraint về thứ tự:

```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
```

### **BST Property**

Với mỗi node trong BST:

- **Left subtree**: chỉ chứa nodes với values **< node's value**
- **Right subtree**: chỉ chứa nodes với values **> node's value**
- **Không có duplicate values** (convention phổ biến)
- **Left và right subtrees** cũng phải là BST

### **Tại sao BST quan trọng?**

✅ **Tìm kiếm nhanh**: O(log n) trong balanced BST  
✅ **Inorder traversal = Sorted order**: dễ dàng lấy elements sorted  
✅ **Dynamic data structure**: insert/delete hiệu quả  
✅ **Foundation cho advanced structures**: AVL, Red-Black Tree, B-Tree

---

## BST PROPERTIES

### **1. Inorder Traversal = Sorted Sequence**

Inorder traversal của BST cho ra **sorted ascending order**:

```python
def inorder(node):
    if node:
        inorder(node.left)   # Smaller values
        print(node.val)       # Current value
        inorder(node.right)   # Larger values

# BST:     5          Inorder: [1, 3, 4, 5, 6, 7, 8]
#         / \
#        3   7
#       / \ / \
#      1  4 6  8
```

**Ứng dụng**: Kiểm tra valid BST, tìm kth smallest/largest element.

---

### **2. Search Property**

Tìm kiếm trong BST giống **Binary Search**:

```
Tìm 6 trong BST:
        8              Compare with 8: 6 < 8 → go left
       / \
      3   10           Compare with 3: 6 > 3 → go right
     / \    \
    1   6   14         Found 6! ✓
       / \   /
      4   7 13
```

**Time Complexity**: O(h) - h là height của tree

- **Balanced BST**: O(log n)
- **Skewed BST**: O(n)

---

### **3. Min & Max Elements**

```
Min element:  Leftmost node (1)
Max element:  Rightmost node (14)

        8
       / \
      3   10
     / \    \
   →1   6   14←
       / \   /
      4   7 13
```

**Time Complexity**: O(h)

---

### **4. Successor & Predecessor**

**Successor** của node N = node nhỏ nhất lớn hơn N
**Predecessor** của node N = node lớn nhất nhỏ hơn N

```
BST:  1, 3, 4, 5, 6, 7, 8

Successor của 5 = 6
Predecessor của 5 = 4
```

**Tìm Successor**:

1. Nếu node có **right child** → Successor = min(right subtree)
2. Nếu không → Successor = ancestor đầu tiên mà node ở left subtree của nó

---

## OPERATIONS & TIME COMPLEXITY

| Operation                 | Average  | Worst Case | Note                     |
| ------------------------- | -------- | ---------- | ------------------------ |
| **Search**                | O(log n) | O(n)       | Binary search pattern    |
| **Insert**                | O(log n) | O(n)       | Find position + add node |
| **Delete**                | O(log n) | O(n)       | Find + restructure       |
| **Min/Max**               | O(log n) | O(n)       | Go left/right to end     |
| **Successor/Predecessor** | O(log n) | O(n)       | Navigate tree            |
| **Inorder (Sorted)**      | O(n)     | O(n)       | Visit all nodes          |

**Note**: Worst case O(n) xảy ra khi tree **skewed** (dạng linked list)

---

### **1. SEARCH**

```python
def search(root, target):
    """
    Time: O(h), Space: O(1) iterative / O(h) recursive
    """
    if not root or root.val == target:
        return root

    if target < root.val:
        return search(root.left, target)
    else:
        return search(root.right, target)
```

**Iterative** (preferred):

```python
def search_iterative(root, target):
    while root and root.val != target:
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return root
```

---

### **2. INSERT**

Luôn insert ở **leaf position** để maintain BST property:

```
Insert 5 vào BST:
        8              Step 1: 5 < 8 → go left
       / \
      3   10           Step 2: 5 > 3 → go right
     / \    \
    1   6   14         Step 3: 5 < 6 → go left
       / \   /         Step 4: left is null → insert here
      4   7 13
     /
   →5  ← New node
```

```python
def insert(root, val):
    """
    Time: O(h), Space: O(h) recursive
    """
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    # else: value already exists (skip duplicates)

    return root
```

**Iterative**:

```python
def insert_iterative(root, val):
    if not root:
        return TreeNode(val)

    curr = root
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
            break  # Duplicate

    return root
```

---

### **3. DELETE**

Phức tạp nhất! **3 cases**:

#### **Case 1: Node là leaf (no children)**

→ Simply remove it

```
Delete 1:
        8
       / \
      3   10
     / \    \
    1   6   14  →  Remove node 1
   (X)
```

#### **Case 2: Node có 1 child**

→ Replace node với child của nó

```
Delete 10 (có 1 child 14):
        8                      8
       / \                    / \
      3   10      →          3   14
     / \    \               / \   /
    1   6   14             1   6 13
           /
          13
```

#### **Case 3: Node có 2 children**

→ Replace với **successor** (hoặc predecessor)

```
Delete 3 (có 2 children):

Step 1: Find successor của 3 = min(right subtree) = 4
Step 2: Copy successor value to node 3
Step 3: Delete successor từ right subtree

        8                      8
       / \                    / \
      3   10      →          4   10
     / \    \               / \    \
    1   6   14             1   6   14
       / \   /                  \   /
      4   7 13                   7 13
```

```python
def delete(root, val):
    """
    Time: O(h), Space: O(h)
    """
    if not root:
        return None

    # Find node to delete
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Found node to delete

        # Case 1: Leaf or Case 2: One child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Two children
        # Find successor (min in right subtree)
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)

    return root


def find_min(node):
    """Find minimum value node (leftmost)"""
    while node.left:
        node = node.left
    return node
```

---

## KHI NÀO DÙNG BST

### ✅ **Nên dùng BST khi**:

1. **Cần search, insert, delete nhanh**

   - Average O(log n) tốt hơn array O(n)

2. **Cần dữ liệu sorted động**

   - Inorder traversal cho sorted order
   - Dễ tìm min, max, kth element

3. **Range queries**

   - Tìm tất cả elements trong [a, b]
   - BST cho phép skip subtrees không cần thiết

4. **Predecessor/Successor queries**
   - BST structure giúp tìm nhanh

### ❌ **Không nên dùng BST khi**:

1. **Dữ liệu không thay đổi (static)**

   - Sorted array + binary search tốt hơn

2. **Cần truy cập random bằng index**

   - Array O(1), BST O(log n)

3. **Dữ liệu có patterns tạo skewed tree**

   - Sorted input → skewed BST O(n)
   - Dùng self-balancing trees (AVL, Red-Black)

4. **Memory constraints nghiêm ngặt**
   - BST cần pointers, overhead cao

---

## BST VS BINARY TREE

| Feature      | Binary Tree                | Binary Search Tree                 |
| ------------ | -------------------------- | ---------------------------------- |
| **Property** | Mỗi node tối đa 2 children | BST property (left < root < right) |
| **Inorder**  | Random order               | **Sorted order**                   |
| **Search**   | O(n) phải duyệt hết        | **O(log n)** average               |
| **Insert**   | Anywhere                   | At correct position (O(log n))     |
| **Delete**   | Simple                     | Complex (3 cases)                  |
| **Use case** | Expression trees, heap     | **Search, sorted data**            |

### **Example**:

**Binary Tree (NOT BST)**:

```
     5
    / \
   7   3    ← 7 > 5 nhưng ở left (violates BST)
  / \
 2   6
```

**Binary Search Tree**:

```
     5
    / \
   3   7    ← Left < Root < Right ✓
  / \
 2   4
```

---

## COMMON PROBLEMS

### **1. Validate BST**

```python
def isValidBST(root):
    """Check if tree is valid BST"""
    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
```

**Lỗi thường gặp**: Chỉ check `node.left.val < node.val < node.right.val`  
→ Sai! Phải check với **entire subtree range**.

---

### **2. Kth Smallest Element**

```python
def kthSmallest(root, k):
    """
    Inorder traversal (sorted) → lấy phần tử thứ k
    Time: O(h + k), Space: O(h)
    """
    stack = []
    curr = root
    count = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        count += 1

        if count == k:
            return curr.val

        curr = curr.right

    return -1
```

---

### **3. Lowest Common Ancestor (LCA)**

```python
def lowestCommonAncestor(root, p, q):
    """
    Tận dụng BST property!
    Time: O(h), Space: O(1)
    """
    while root:
        # Both in left subtree
        if p.val < root.val and q.val < root.val:
            root = root.left
        # Both in right subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right
        # Split point found
        else:
            return root

    return None
```

---

### **4. Convert Sorted Array to BST**

```python
def sortedArrayToBST(nums):
    """
    Build balanced BST from sorted array
    Time: O(n), Space: O(log n)
    """
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root
```

---

## BALANCED VS SKEWED BST

### **Balanced BST** (Ideal)

```
Height = O(log n)

       4
      / \
     2   6
    / \ / \
   1  3 5  7
```

- **Search/Insert/Delete**: O(log n)
- **Shape**: Gần complete binary tree

### **Skewed BST** (Worst Case)

```
Height = O(n)

1
 \
  2        ← Like linked list!
   \
    3
     \
      4
       \
        5
```

- **Search/Insert/Delete**: O(n)
- **Xảy ra khi**: Insert sorted data (1,2,3,4,5)

### **Solution**: Self-Balancing Trees

- **AVL Tree**: Strict balance (height difference ≤ 1)
- **Red-Black Tree**: Looser balance (used in C++ std::map)
- **Maintain**: O(log n) worst case

---

## TÓM TẮT

### **Key Points**

✅ **BST Property**: Left < Root < Right (recursively)  
✅ **Inorder = Sorted**: Powerful property  
✅ **Operations**: O(log n) average, O(n) worst case  
✅ **Search pattern**: Like binary search  
✅ **Delete**: 3 cases (0, 1, 2 children)

### **When to use BST**

| Scenario                      | Use BST?                 |
| ----------------------------- | ------------------------ |
| Dynamic sorted data           | ✅ Yes                   |
| Frequent search/insert/delete | ✅ Yes                   |
| Range queries                 | ✅ Yes                   |
| Static data                   | ❌ No (use sorted array) |
| Need index access             | ❌ No (use array)        |
| Sorted input                  | ❌ No (use balanced BST) |

### **Common Pitfalls**

❌ Chỉ check local property (parent vs immediate children)  
❌ Quên handle duplicate values  
❌ Không consider skewed case  
❌ Sử dụng cho sorted input → degrades to O(n)

### **Next Steps**

1. ✅ Practice BST operations implementation
2. ➡️ Learn self-balancing trees (AVL, Red-Black)
3. ➡️ Study advanced BST problems
4. ➡️ Understand when NOT to use BST

**Remember**: BST là foundation, nhưng production thường dùng **balanced BST** variants! 🌳
