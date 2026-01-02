# 📚 Stacks - Ngăn xếp

## 📖 Stack là gì?

**Stack** là cấu trúc dữ liệu tuyến tính theo nguyên tắc **LIFO** (Last In, First Out):

- **Last In**: Element được thêm vào cuối cùng
- **First Out**: Sẽ được lấy ra đầu tiên

**Ví dụ thực tế**:

- Chồng đĩa 🍽️: Lấy đĩa ở trên cùng (added last)
- Undo trong editor: Undo thao tác cuối cùng
- Back button trong browser
- Function call stack

### Visual:

```
        TOP
         ↓
      ┌─────┐
      │  3  │  ← Push/Pop từ đây
      ├─────┤
      │  2  │
      ├─────┤
      │  1  │  ← Bottom (added first)
      └─────┘
```

---

## ⚡ Operations & Complexity

| Operation              | Time | Description                      |
| ---------------------- | ---- | -------------------------------- |
| **push(x)**            | O(1) | Thêm element lên top             |
| **pop()**              | O(1) | Remove và return element ở top   |
| **peek()** / **top()** | O(1) | Xem element ở top (không remove) |
| **isEmpty()**          | O(1) | Check if stack empty             |
| **size()**             | O(1) | Return số elements               |

---

## 🛠️ Implementation

### Method 1: Using Python List

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top - O(1)"""
        self.items.append(item)

    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.items) == 0

    def size(self):
        """Return size - O(1)"""
        return len(self.items)
```

### Method 2: Using Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        """Add item to top - O(1)"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
```

---

## 🎯 Applications of Stack

### 1️⃣ **Balanced Parentheses**

Check if brackets are properly matched.

```python
def is_balanced(expression):
    """
    Check if parentheses are balanced

    Example: "({[]})" → True
             "({[}])" → False
    """
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Time: O(n)
# Space: O(n)
```

### 2️⃣ **Evaluate Postfix Expression**

```python
def evaluate_postfix(expression):
    """
    Evaluate postfix notation

    Example: "2 3 1 * + 9 -" → ((2 + (3 * 1)) - 9) = -4
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+': result = a + b
            elif token == '-': result = a - b
            elif token == '*': result = a * b
            elif token == '/': result = a // b

            stack.append(result)

    return stack[0]

# Time: O(n)
# Space: O(n)
```

### 3️⃣ **Next Greater Element**

```python
def next_greater_element(arr):
    """
    Find next greater element for each element

    Example: [4, 5, 2, 10, 8]
    Result:  [5, 10, 10, -1, -1]
    """
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        # Pop smaller elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # Top is next greater (if exists)
        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result

# Time: O(n)
# Space: O(n)
```

### 4️⃣ **Monotonic Stack**

Stack that maintains elements in increasing/decreasing order.

```python
def largest_rectangle_histogram(heights):
    """
    Find largest rectangle in histogram

    Uses monotonic increasing stack
    """
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# Time: O(n)
# Space: O(n)
```

---

# 📥 Queues - Hàng đợi

## 📖 Queue là gì?

**Queue** là cấu trúc dữ liệu tuyến tính theo nguyên tắc **FIFO** (First In, First Out):

- **First In**: Element được thêm vào đầu tiên
- **First Out**: Sẽ được lấy ra đầu tiên

**Ví dụ thực tế**:

- Hàng chờ mua vé 🎫
- Print queue
- BFS trong graphs
- Task scheduling

### Visual:

```
REAR → [4] [3] [2] [1] ← FRONT
        ↑           ↑
      Enqueue    Dequeue
```

---

## ⚡ Operations & Complexity

| Operation                | Time | Description               |
| ------------------------ | ---- | ------------------------- |
| **enqueue(x)**           | O(1) | Add element to rear       |
| **dequeue()**            | O(1) | Remove element from front |
| **front()** / **peek()** | O(1) | View front element        |
| **isEmpty()**            | O(1) | Check if empty            |
| **size()**               | O(1) | Return số elements        |

---

## 🛠️ Implementation

### Method 1: Using List (Naive - Inefficient)

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # O(n) - BAD!

    def is_empty(self):
        return len(self.items) == 0

# Problem: dequeue() is O(n) due to list shifting
```

### Method 2: Using collections.deque (Recommended)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add to rear - O(1)"""
        self.items.append(item)

    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        """View front - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# All operations O(1) ✓
```

### Method 3: Circular Queue (Fixed Size)

```python
class CircularQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0
```

---

## 🎯 Applications of Queue

### 1️⃣ **BFS (Breadth-First Search)**

```python
from collections import deque

def bfs(graph, start):
    """
    BFS traversal using queue
    """
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Time: O(V + E)
# Space: O(V)
```

### 2️⃣ **Sliding Window Maximum**

```python
from collections import deque

def max_sliding_window(arr, k):
    """
    Find maximum in each window of size k
    Uses deque to maintain decreasing order

    Example: [1,3,-1,-3,5,3,6,7], k=3
    Result: [3,3,5,5,6,7]
    """
    dq = deque()  # Store indices
    result = []

    for i in range(len(arr)):
        # Remove indices outside window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements (maintain decreasing order)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # Add to result after first window
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Time: O(n)
# Space: O(k)
```

---

## 🔄 Deque (Double-Ended Queue)

Queue cho phép insert/delete từ **cả hai đầu**.

```python
from collections import deque

dq = deque()

# Add elements
dq.append(1)        # Add to right: [1]
dq.appendleft(2)    # Add to left: [2, 1]
dq.extend([3, 4])   # [2, 1, 3, 4]

# Remove elements
dq.pop()            # Remove from right → 4
dq.popleft()        # Remove from left → 2

# Result: [1, 3]
```

### Operations:

| Operation       | Time | Description       |
| --------------- | ---- | ----------------- |
| `append(x)`     | O(1) | Add to right      |
| `appendleft(x)` | O(1) | Add to left       |
| `pop()`         | O(1) | Remove from right |
| `popleft()`     | O(1) | Remove from left  |

---

## 📊 Comparison: Stack vs Queue vs Deque

| Feature       | Stack                      | Queue             | Deque                      |
| ------------- | -------------------------- | ----------------- | -------------------------- |
| **Order**     | LIFO                       | FIFO              | Both ends                  |
| **Add**       | push (top)                 | enqueue (rear)    | Both ends                  |
| **Remove**    | pop (top)                  | dequeue (front)   | Both ends                  |
| **Use Cases** | Undo, DFS, Expression eval | BFS, Task queue   | Sliding window, Palindrome |
| **Python**    | list                       | collections.deque | collections.deque          |

---

## 🎓 Key Takeaways

### Stacks:

1. **LIFO** - Last In, First Out
2. **All operations O(1)**
3. **Use for**: Undo, DFS, Expression evaluation, Parentheses matching
4. **Monotonic Stack**: Powerful technique for "next greater/smaller" problems

### Queues:

1. **FIFO** - First In, First Out
2. **Use collections.deque** in Python (not list!)
3. **Use for**: BFS, Task scheduling, Sliding window
4. **Circular Queue**: Fixed size, efficient memory

### Deque:

1. **Best of both** - Can act as stack OR queue
2. **All operations O(1) at both ends**
3. **Most versatile** - use as default choice

---

## 💡 Common Patterns

### Pattern 1: Monotonic Stack

Maintain increasing/decreasing order for "next greater/smaller" problems.

### Pattern 2: Stack for Matching

Parentheses, HTML tags, etc.

### Pattern 3: Queue for Level-Order

BFS in trees/graphs.

### Pattern 4: Deque for Sliding Window

Maintain max/min in window.

---

## ➡️ Next Steps

- 💻 Xem [Implementation Code](implementation.py)
- 📝 Làm [Practice Problems](practice.md)
- 📖 Đọc tiếp [Trees](../../03_trees/binary_trees/theory.md)

**Master these - they're fundamental for many algorithms! 🚀**
