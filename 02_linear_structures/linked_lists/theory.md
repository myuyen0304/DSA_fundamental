# 🔗 Linked Lists - Danh sách liên kết

## 📖 Linked List là gì?

**Linked List** là cấu trúc dữ liệu tuyến tính trong đó các elements (nodes) được lưu trữ ở **các vị trí bộ nhớ không liên tiếp**. Mỗi node chứa:

- **Data**: Giá trị của node
- **Pointer(s)**: Reference đến node khác

### So sánh với Array:

| Feature             | Array                             | Linked List                    |
| ------------------- | --------------------------------- | ------------------------------ |
| **Memory**          | Contiguous (liền kề)              | Non-contiguous (rời rạc)       |
| **Access**          | O(1) by index                     | O(n) - phải traverse           |
| **Insert at start** | O(n) - shift elements             | O(1) - chỉ cần update pointers |
| **Insert at end**   | O(1)\* amortized                  | O(1) nếu có tail pointer       |
| **Delete**          | O(n) - shift elements             | O(1) nếu có pointer to node    |
| **Size**            | Fixed (static) hoặc resize costly | Dynamic, grow dễ dàng          |
| **Memory overhead** | Minimal                           | Extra space cho pointers       |

---

## 🎨 Types of Linked Lists

### 1️⃣ Singly Linked List

Mỗi node trỏ đến node **tiếp theo**.

```
HEAD → [1|●] → [2|●] → [3|●] → [4|None]
       data next
```

**Structure**:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

**Ưu điểm**:

- Simple implementation
- Memory efficient (1 pointer/node)

**Nhược điểm**:

- Chỉ traverse forward
- Không thể access previous node

---

### 2️⃣ Doubly Linked List

Mỗi node trỏ đến **cả previous và next** node.

```
       ┌──────┬───────┬──────┐     ┌──────┬───────┬──────┐
HEAD → │ None │   1   │   ●──┼────→│  ●   │   2   │   ●──┼→...
       └──────┴───────┴──────┘     └──┬───┴───────┴──────┘
         prev   data    next           │
                 ▲                      │
                 └──────────────────────┘
```

**Structure**:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

**Ưu điểm**:

- Traverse both directions
- Delete node dễ hơn (có prev pointer)

**Nhược điểm**:

- More memory (2 pointers/node)
- More complex operations

---

### 3️⃣ Circular Linked List

Node cuối trỏ về **HEAD** (tạo thành vòng tròn).

```
       ┌──────────────────────────────┐
       │                              │
       ▼                              │
HEAD → [1|●] → [2|●] → [3|●] → [4|●]─┘
```

**Use cases**:

- Round-robin scheduling
- Music playlists (loop)
- Browser circular history

---

## ⚡ Operations & Complexity

| Operation                | Singly LL      | Doubly LL | Notes                         |
| ------------------------ | -------------- | --------- | ----------------------------- |
| **Access**               | O(n)           | O(n)      | Must traverse from head       |
| **Search**               | O(n)           | O(n)      | Linear search                 |
| **Insert at head**       | O(1)           | O(1)      | Update head pointer           |
| **Insert at tail**       | O(n) or O(1)\* | O(1)\*    | \*If have tail pointer        |
| **Insert at middle**     | O(n)           | O(n)      | Find position + insert        |
| **Delete at head**       | O(1)           | O(1)      | Update head pointer           |
| **Delete at tail**       | O(n)           | O(1)\*    | \*If have tail pointer        |
| **Delete with node ref** | O(1)\*\*       | O(1)      | \*\*Singly LL needs prev node |
| **Reverse**              | O(n)           | O(n)      | Change all pointers           |

---

## 🎯 Khi nào dùng Linked Lists?

### ✅ Nên dùng khi:

1. **Frequent insertions/deletions** ở đầu/giữa
2. **Unknown size** và cần grow dynamically
3. **Implement stacks, queues, graphs**
4. **Memory fragmentation** - không cần contiguous memory

### ❌ Không nên dùng khi:

1. **Cần random access** - phải dùng index
2. **Memory overhead** là vấn đề
3. **Cache performance** quan trọng
4. **Frequent search operations**

---

## 🛠️ Basic Operations

### 1. Traverse (Duyệt qua List)

```python
def traverse(head):
    """Print all nodes"""
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

# Time: O(n)
# Space: O(1)
```

---

### 2. Insert at Head

```python
def insert_at_head(head, data):
    """Insert node at beginning"""
    new_node = Node(data)
    new_node.next = head
    return new_node  # New head

# Time: O(1)
# Space: O(1)
```

**Visual**:

```
Before: HEAD → [2] → [3] → None
Insert 1:
Step 1: new_node = [1|None]
Step 2: new_node.next = HEAD → [1|●] → [2] → [3] → None
Step 3: HEAD = new_node
After:  HEAD → [1] → [2] → [3] → None
```

---

### 3. Insert at Tail

```python
def insert_at_tail(head, data):
    """Insert node at end"""
    new_node = Node(data)

    if not head:
        return new_node

    current = head
    while current.next:  # O(n) - find last node
        current = current.next

    current.next = new_node
    return head

# Time: O(n) - must traverse to end
# Space: O(1)

# Optimization: Keep tail pointer → O(1)
```

---

### 4. Insert at Position

```python
def insert_at_position(head, data, position):
    """Insert at specific position (0-indexed)"""
    new_node = Node(data)

    # Insert at head
    if position == 0:
        new_node.next = head
        return new_node

    # Find node at position-1
    current = head
    for _ in range(position - 1):
        if not current:
            return head  # Invalid position
        current = current.next

    # Insert after current
    new_node.next = current.next
    current.next = new_node

    return head

# Time: O(n)
# Space: O(1)
```

---

### 5. Delete Node

```python
def delete_node(head, key):
    """Delete first node with given key"""
    # Delete head
    if head and head.data == key:
        return head.next

    # Find node before target
    current = head
    while current and current.next:
        if current.next.data == key:
            current.next = current.next.next
            return head
        current = current.next

    return head

# Time: O(n)
# Space: O(1)
```

---

### 6. Search

```python
def search(head, key):
    """Find node with given key"""
    current = head
    position = 0

    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1

    return -1

# Time: O(n)
# Space: O(1)
```

---

## 🎓 Important Techniques & Patterns

### 1️⃣ **Fast & Slow Pointers (Floyd's Algorithm)**

Technique để detect cycles, find middle, etc.

```python
def find_middle(head):
    """Find middle node"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps

    return slow  # Middle node

# Time: O(n)
# Space: O(1)
```

**Visual**:

```
1 → 2 → 3 → 4 → 5 → None
S,F

1 → 2 → 3 → 4 → 5 → None
    S       F

1 → 2 → 3 → 4 → 5 → None
        S           F (None)

Middle = 3 ✓
```

---

### 2️⃣ **Reverse Linked List**

One of the most important operations!

```python
def reverse(head):
    """Reverse linked list in-place"""
    prev = None
    current = head

    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev  # New head

# Time: O(n)
# Space: O(1)
```

**Visual**:

```
Initial: None ← prev  current → next
              [1] → [2] → [3] → None

Step 1: None ← [1]  [2] → [3] → None
              prev  curr

Step 2: None ← [1] ← [2]  [3] → None
                    prev  curr

Step 3: None ← [1] ← [2] ← [3]  None
                          prev  curr

Result: [3] → [2] → [1] → None
```

---

### 3️⃣ **Detect Cycle**

```python
def has_cycle(head):
    """Detect if linked list has cycle"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Time: O(n)
# Space: O(1)
```

**Why it works**:

- If có cycle, fast sẽ lap slow
- Giống như đường đua: người chạy nhanh sẽ gặp lại người chạy chậm

---

### 4️⃣ **Remove Nth Node from End**

```python
def remove_nth_from_end(head, n):
    """Remove nth node from end"""
    dummy = Node(0)
    dummy.next = head

    # Move fast pointer n steps ahead
    fast = dummy
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next

# Time: O(n)
# Space: O(1)
```

---

### 5️⃣ **Merge Two Sorted Lists**

```python
def merge_two_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append remaining
    current.next = l1 if l1 else l2

    return dummy.next

# Time: O(n + m)
# Space: O(1)
```

---

### 6️⃣ **Palindrome Check**

```python
def is_palindrome(head):
    """Check if linked list is palindrome"""
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse(slow)

    # Compare both halves
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# Time: O(n)
# Space: O(1)
```

---

## 🎨 Common Patterns

### Pattern 1: Dummy Node

Simplify edge cases (empty list, head changes).

```python
dummy = Node(0)
dummy.next = head
# Work with dummy
return dummy.next
```

### Pattern 2: Two Pointers (Different Speeds)

- Fast & Slow (2x speed)
- Use for: cycle detection, middle, nth from end

### Pattern 3: Runner Technique

- Two pointers, different starting positions
- Example: Remove nth from end

### Pattern 4: In-place Reversal

- Reverse pointers while traversing
- Space: O(1)

---

## ⚠️ Common Pitfalls

### 1. Forgetting to Update Head

```python
# Wrong
def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    # Forgot to return new_node!

# Correct
def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # Return new head
```

### 2. Losing Reference

```python
# Wrong - loses rest of list
current.next = new_node

# Correct - save reference first
new_node.next = current.next
current.next = new_node
```

### 3. Not Handling Empty List

```python
# Wrong
def some_operation(head):
    # Crash if head is None
    return head.data

# Correct
def some_operation(head):
    if not head:
        return None
    return head.data
```

### 4. Infinite Loop in Cycle

```python
# Wrong - infinite loop if cycle exists
while current.next:
    current = current.next

# Correct - use Floyd's algorithm
```

---

## 📊 Complexity Summary

| Operation            | Array  | Linked List | Winner |
| -------------------- | ------ | ----------- | ------ |
| **Access by index**  | O(1)   | O(n)        | Array  |
| **Search**           | O(n)   | O(n)        | Tie    |
| **Insert at start**  | O(n)   | O(1)        | LL     |
| **Insert at end**    | O(1)\* | O(1)\*      | Tie    |
| **Insert at middle** | O(n)   | O(n)        | Tie    |
| **Delete**           | O(n)   | O(1)\*\*    | LL     |
| **Memory**           | Fixed  | Dynamic     | LL     |

\*Amortized for array
\*\*If have reference to node

---

## 🎯 Key Takeaways

1. **Linked Lists excel at insertions/deletions**
2. **Arrays excel at random access**
3. **Fast & Slow Pointers** là technique cực kỳ quan trọng
4. **Always check for null** (empty list, end of list)
5. **Dummy nodes** simplify code
6. **Reverse in-place** với O(1) space
7. **Draw diagrams** khi debug!

---

## ➡️ Next Steps

- 💻 Xem [Implementation Code](implementation.py)
- 📝 Làm [15 Practice Problems](practice.md)
- ✅ Master Fast & Slow Pointers technique
- 📖 Đọc tiếp [Stacks & Queues](../stacks/theory.md)

**Practice makes perfect! Linked Lists cần vẽ diagram nhiều lần để hiểu! 🚀**
