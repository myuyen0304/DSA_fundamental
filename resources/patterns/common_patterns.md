# 🎯 Common DSA Patterns & When to Use Them

## 📚 Table of Contents

1. [Frequency Counter / Hash Map](#1-frequency-counter--hash-map)
2. [Two Pointers](#2-two-pointers)
3. [Sliding Window](#3-sliding-window)
4. [Fast & Slow Pointers](#4-fast--slow-pointers)
5. [Merge Intervals](#5-merge-intervals)
6. [Cyclic Sort](#6-cyclic-sort)
7. [In-place Reversal of LinkedList](#7-in-place-reversal-of-linkedlist)
8. [Tree BFS](#8-tree-bfs)
9. [Tree DFS](#9-tree-dfs)
10. [Two Heaps](#10-two-heaps)
11. [Subsets](#11-subsets)
12. [Modified Binary Search](#12-modified-binary-search)
13. [Top K Elements](#13-top-k-elements)
14. [K-way Merge](#14-k-way-merge)
15. [Topological Sort](#15-topological-sort)

---

## 1. Frequency Counter / Hash Map

### 🎯 When to use:

- Count occurrences of elements
- Check if anagrams
- Find duplicates
- Group items
- O(n²) → O(n) optimization

### 🔑 Key Characteristics:

- Need fast lookup (O(1))
- Trade space for time
- Usually reduces from O(n²) to O(n)

### 📝 Template:

```python
def pattern(arr):
    freq_map = {}  # or Counter from collections

    # Build frequency map
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1

    # Process using map
    for key, count in freq_map.items():
        # Use frequency information
        pass
```

### 💡 Example Problems:

1. **Two Sum** - Find pair with target sum
2. **Anagram Check** - Check if two strings are anagrams
3. **First Non-Repeating Character**
4. **Group Anagrams**
5. **Contains Duplicate**

### 🔍 Example Solution: Two Sum

```python
def two_sum(arr, target):
    seen = {}  # value: index
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
# Time: O(n), Space: O(n)
```

---

## 2. Two Pointers

### 🎯 When to use:

- Array is **sorted** (usually)
- Find pairs/triplets with specific sum
- Remove duplicates
- Reverse
- Compare strings/arrays

### 🔑 Key Characteristics:

- Move pointers based on condition
- Usually O(n) time, O(1) space
- Alternative to nested loops

### 📝 Template:

```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Process current pair
        if condition:
            # Found answer or move both
            left += 1
            right -= 1
        elif need_larger:
            left += 1
        else:
            right -= 1
```

### 💡 Example Problems:

1. **Two Sum II** (sorted array)
2. **3Sum**
3. **Container With Most Water**
4. **Remove Duplicates**
5. **Valid Palindrome**

### 🔍 Example: 3Sum

```python
def three_sum(arr):
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i-1]:
            continue

        # Two pointers for remaining
        left, right = i + 1, len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])
                # Skip duplicates
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
# Time: O(n²), Space: O(1)
```

---

## 3. Sliding Window

### 🎯 When to use:

- Subarray/substring problems
- Find max/min in subarrays
- Contiguous sequence of elements
- "K" size constraint

### 🔑 Key Characteristics:

- Maintain window with specific property
- Expand and shrink window
- O(n) instead of O(n²) nested loops

### 📝 Template (Fixed Size):

```python
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])  # First window
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Slide: add new, remove old
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### 📝 Template (Variable Size):

```python
def sliding_window_variable(arr, target):
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(arr)):
        # Expand window
        window_sum += arr[right]

        # Shrink window if needed
        while window_sum > target:
            window_sum -= arr[left]
            left += 1

        # Update result
        max_length = max(max_length, right - left + 1)

    return max_length
```

### 💡 Example Problems:

1. **Maximum Sum Subarray of Size K**
2. **Longest Substring with K Distinct Characters**
3. **Minimum Window Substring**
4. **Longest Substring Without Repeating Characters**
5. **Max Consecutive Ones III**

---

## 4. Fast & Slow Pointers

### 🎯 When to use:

- Linked list problems
- Detect cycles
- Find middle element
- Find nth element from end

### 🔑 Key Characteristics:

- Two pointers move at different speeds
- Usually slow moves 1 step, fast moves 2 steps
- Meet at cycle or specific position

### 📝 Template:

```python
def fast_slow_pointers(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps

        if slow == fast:
            # Cycle detected or specific condition
            return True

    return False
```

### 💡 Example Problems:

1. **Linked List Cycle**
2. **Middle of Linked List**
3. **Happy Number**
4. **Palindrome Linked List**
5. **Find Duplicate Number**

---

## 5. Merge Intervals

### 🎯 When to use:

- Overlapping intervals
- Schedule conflicts
- Range problems
- Meeting rooms

### 🔑 Key Characteristics:

- Sort intervals first (usually by start)
- Merge overlapping intervals
- Compare current with last merged

### 📝 Template:

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # Check overlap
        if current[0] <= last[1]:
            # Merge
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)

    return merged
```

### 💡 Example Problems:

1. **Merge Intervals**
2. **Insert Interval**
3. **Meeting Rooms**
4. **Meeting Rooms II**
5. **Employee Free Time**

---

## 6. Cyclic Sort

### 🎯 When to use:

- Array contains numbers in range [1, n]
- Find missing/duplicate numbers
- O(n) time, O(1) space required

### 🔑 Key Characteristics:

- Place each number at its correct index
- Index as hash key
- Number i should be at index i-1

### 📝 Template:

```python
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct_idx = arr[i] - 1

        # If not in correct position
        if arr[i] != arr[correct_idx]:
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        else:
            i += 1

    return arr
```

### 💡 Example Problems:

1. **Find Missing Number**
2. **Find All Duplicates**
3. **Find All Missing Numbers**
4. **Find Duplicate Number**
5. **First Missing Positive**

---

## 7. In-place Reversal of LinkedList

### 🎯 When to use:

- Reverse linked list
- Reverse in groups
- K-group reversal

### 🔑 Key Characteristics:

- Change pointers, not values
- Keep track of prev, current, next
- O(n) time, O(1) space

### 📝 Template:

```python
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev  # New head
```

### 💡 Example Problems:

1. **Reverse Linked List**
2. **Reverse Linked List II**
3. **Reverse Nodes in k-Group**
4. **Reverse Alternate K Nodes**
5. **Rotate List**

---

## 8. Tree BFS

### 🎯 When to use:

- Level-order traversal
- Find level of node
- Zigzag traversal
- Connect level nodes

### 🔑 Key Characteristics:

- Use queue
- Process level by level
- Track level size

### 📝 Template:

```python
from collections import deque

def tree_bfs(root):
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

### 💡 Example Problems:

1. **Binary Tree Level Order Traversal**
2. **Zigzag Level Order**
3. **Average of Levels**
4. **Minimum Depth**
5. **Connect Level Order Siblings**

---

## 9. Tree DFS

### 🎯 When to use:

- Path problems
- Tree properties (height, diameter)
- Subtree problems
- Preorder/Inorder/Postorder

### 🔑 Key Characteristics:

- Use recursion (or stack)
- Go deep before going wide
- Track path/state through recursion

### 📝 Template:

```python
def tree_dfs(root):
    def dfs(node, path):
        if not node:
            return

        # Preorder: process here
        path.append(node.val)

        # If leaf node
        if not node.left and not node.right:
            # Process leaf
            pass

        # Recurse
        dfs(node.left, path)
        dfs(node.right, path)

        # Postorder: process here
        path.pop()  # Backtrack

    dfs(root, [])
```

### 💡 Example Problems:

1. **Path Sum**
2. **All Paths for Sum**
3. **Sum Root to Leaf Numbers**
4. **Path with Max Sum**
5. **Count Paths for Sum**

---

## 10. Two Heaps

### 🎯 When to use:

- Find median
- Smallest/largest element from stream
- Maintain two groups

### 🔑 Key Characteristics:

- Max heap for smaller half
- Min heap for larger half
- Balance heaps

### 📝 Template:

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (invert)
        self.large = []  # Min heap

    def add_num(self, num):
        heapq.heappush(self.small, -num)

        # Balance
        if self.small and self.large and \
           -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance size
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

### 💡 Example Problems:

1. **Find Median from Data Stream**
2. **Sliding Window Median**
3. **IPO**
4. **Next Interval**

---

## 11. Subsets

### 🎯 When to use:

- All combinations
- All permutations
- All subsets
- Backtracking problems

### 🔑 Key Characteristics:

- Recursive approach
- Build solution incrementally
- Backtrack when needed

### 📝 Template:

```python
def subsets(arr):
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()  # Backtrack

    backtrack(0, [])
    return result
```

### 💡 Example Problems:

1. **Subsets**
2. **Subsets II** (with duplicates)
3. **Permutations**
4. **Combinations**
5. **Letter Combinations of Phone**

---

## 12. Modified Binary Search

### 🎯 When to use:

- Sorted/rotated array
- Find boundary
- Search in infinite array
- Peak finding

### 🔑 Key Characteristics:

- Divide search space
- Determine which half to search
- O(log n) time

### 📝 Template:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Determine which half
        if condition:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### 💡 Example Problems:

1. **Binary Search**
2. **Search in Rotated Array**
3. **Find Peak Element**
4. **Search in Infinite Array**
5. **Find First and Last Position**

---

## 13. Top K Elements

### 🎯 When to use:

- Find K largest/smallest
- K most frequent
- Kth element

### 🔑 Key Characteristics:

- Use heap (priority queue)
- Maintain heap of size K
- O(n log K) time

### 📝 Template:

```python
import heapq

def top_k_elements(arr, k):
    # Min heap of size K
    heap = []

    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap  # K largest elements
```

### 💡 Example Problems:

1. **Kth Largest Element**
2. **Top K Frequent Elements**
3. **K Closest Points to Origin**
4. **Find K Pairs with Smallest Sums**

---

## 14. K-way Merge

### 🎯 When to use:

- Merge K sorted arrays/lists
- Smallest range in K lists

### 🔑 Key Characteristics:

- Use min heap
- Track elements from each list
- O(N log K) where N = total elements

### 📝 Template:

```python
import heapq

def merge_k_sorted(lists):
    heap = []
    result = []

    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

### 💡 Example Problems:

1. **Merge K Sorted Lists**
2. **Kth Smallest in M Sorted Lists**
3. **Smallest Range Covering Elements**

---

## 15. Topological Sort

### 🎯 When to use:

- DAG (Directed Acyclic Graph)
- Course schedule
- Task dependencies
- Build order

### 🔑 Key Characteristics:

- Use in-degree count
- BFS or DFS
- Detect cycles

### 📝 Template:

```python
from collections import deque, defaultdict

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(vertices)}

    # Build graph
    for parent, child in edges:
        graph[parent].append(child)
        in_degree[child] += 1

    # Start with nodes with 0 in-degree
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        # Reduce in-degree of neighbors
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if cycle exists
    if len(result) != vertices:
        return []  # Cycle exists

    return result
```

### 💡 Example Problems:

1. **Course Schedule**
2. **Course Schedule II**
3. **Alien Dictionary**
4. **Sequence Reconstruction**

---

## 🎯 Pattern Recognition Flowchart

```
Problem → Check characteristics

Is it sorted array?
  Yes → Binary Search or Two Pointers

Is it about subarrays/substrings?
  Yes → Sliding Window

Need to count/group elements?
  Yes → Hash Map

Linked List problem?
  Yes → Fast & Slow Pointers

Tree problem?
  Level-wise? → BFS
  Path-related? → DFS

Need K largest/smallest?
  Yes → Heap / Top K Pattern

Graph with dependencies?
  Yes → Topological Sort

All combinations/permutations?
  Yes → Backtracking / Subsets
```

---

**Practice recognizing patterns, and problems become easier!** 🚀
