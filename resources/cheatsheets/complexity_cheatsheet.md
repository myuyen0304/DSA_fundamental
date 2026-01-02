# ⚡ Big O Complexity Cheat Sheet

## 📊 Complexity Rankings (Best → Worst)

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### Performance Comparison (n = 1,000,000)

| Complexity     | Operations        | Approx Time\* | Scalability          |
| -------------- | ----------------- | ------------- | -------------------- |
| **O(1)**       | 1                 | Instant       | ⭐⭐⭐⭐⭐ Excellent |
| **O(log n)**   | ~20               | Instant       | ⭐⭐⭐⭐⭐ Excellent |
| **O(n)**       | 1,000,000         | 1 ms          | ⭐⭐⭐⭐ Good        |
| **O(n log n)** | ~20,000,000       | 20 ms         | ⭐⭐⭐ Acceptable    |
| **O(n²)**      | 1,000,000,000,000 | 17 mins       | ⭐ Poor              |
| **O(2ⁿ)**      | 2^n               | Universe age  | ❌ Impractical       |
| **O(n!)**      | n!                | ∞             | ❌ Impractical       |

\*Assuming 1 operation = 1 nanosecond

---

## 🎯 Common Complexities by Operation

### Data Structure Operations

| Data Structure         | Access       | Search       | Insert       | Delete       | Space  |
| ---------------------- | ------------ | ------------ | ------------ | ------------ | ------ |
| **Array**              | O(1)         | O(n)         | O(n)         | O(n)         | O(n)   |
| **Array (sorted)**     | O(1)         | O(log n)     | O(n)         | O(n)         | O(n)   |
| **Linked List**        | O(n)         | O(n)         | O(1)\*       | O(1)\*       | O(n)   |
| **Stack**              | O(n)         | O(n)         | O(1)         | O(1)         | O(n)   |
| **Queue**              | O(n)         | O(n)         | O(1)         | O(1)         | O(n)   |
| **Hash Table**         | N/A          | O(1)\*\*     | O(1)\*\*     | O(1)\*\*     | O(n)   |
| **Binary Search Tree** | O(log n)\*\* | O(log n)\*\* | O(log n)\*\* | O(log n)\*\* | O(n)   |
| **AVL Tree**           | O(log n)     | O(log n)     | O(log n)     | O(log n)     | O(n)   |
| **Binary Heap**        | N/A          | O(n)         | O(log n)     | O(log n)     | O(n)   |
| **Trie**               | N/A          | O(k)         | O(k)         | O(k)         | O(n×k) |

\*If you have reference to the node
\*\*Average case; worst case can be O(n)
k = length of string

---

## 🔍 Algorithm Complexities

### Sorting Algorithms

| Algorithm          | Best       | Average    | Worst      | Space    | Stable |
| ------------------ | ---------- | ---------- | ---------- | -------- | ------ |
| **Bubble Sort**    | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| **Selection Sort** | O(n²)      | O(n²)      | O(n²)      | O(1)     | No     |
| **Insertion Sort** | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| **Merge Sort**     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
| **Quick Sort**     | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
| **Heap Sort**      | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
| **Counting Sort**  | O(n+k)     | O(n+k)     | O(n+k)     | O(k)     | Yes    |
| **Radix Sort**     | O(nk)      | O(nk)      | O(nk)      | O(n+k)   | Yes    |
| **Bucket Sort**    | O(n+k)     | O(n+k)     | O(n²)      | O(n)     | Yes    |

k = range of input

### Searching Algorithms

| Algorithm         | Best           | Average        | Worst          | Space  | Notes        |
| ----------------- | -------------- | -------------- | -------------- | ------ | ------------ |
| **Linear Search** | O(1)           | O(n)           | O(n)           | O(1)   | Unsorted     |
| **Binary Search** | O(1)           | O(log n)       | O(log n)       | O(1)   | Sorted array |
| **DFS (Graph)**   | O(V+E)         | O(V+E)         | O(V+E)         | O(V)   |              |
| **BFS (Graph)**   | O(V+E)         | O(V+E)         | O(V+E)         | O(V)   |              |
| **Dijkstra**      | O((V+E) log V) | O((V+E) log V) | O((V+E) log V) | O(V)   | Weighted     |
| **A\* Search**    | O(E)           | O(E)           | O(b^d)         | O(b^d) | Heuristic    |

V = vertices, E = edges, b = branching factor, d = depth

---

## 🎨 Common Patterns & Their Complexities

### Array/String Patterns

| Pattern                  | Time                   | Space | Use Case                        |
| ------------------------ | ---------------------- | ----- | ------------------------------- |
| **Two Pointers**         | O(n)                   | O(1)  | Sorted array, pairs, palindrome |
| **Sliding Window**       | O(n)                   | O(1)  | Subarray/substring problems     |
| **Prefix Sum**           | O(n) build, O(1) query | O(n)  | Range sum queries               |
| **Kadane's Algorithm**   | O(n)                   | O(1)  | Maximum subarray sum            |
| **Dutch National Flag**  | O(n)                   | O(1)  | 3-way partitioning              |
| **Fast & Slow Pointers** | O(n)                   | O(1)  | Cycle detection, middle element |

### Tree Patterns

| Pattern                 | Time         | Space | Use Case                     |
| ----------------------- | ------------ | ----- | ---------------------------- |
| **DFS (Recursive)**     | O(n)         | O(h)  | Tree traversal               |
| **BFS (Level Order)**   | O(n)         | O(w)  | Level-wise processing        |
| **Binary Search (BST)** | O(log n) avg | O(1)  | Search in BST                |
| **Morris Traversal**    | O(n)         | O(1)  | Tree traversal without stack |

h = height, w = max width

### Graph Patterns

| Pattern              | Time           | Space | Use Case                      |
| -------------------- | -------------- | ----- | ----------------------------- |
| **DFS**              | O(V+E)         | O(V)  | Connectivity, cycle detection |
| **BFS**              | O(V+E)         | O(V)  | Shortest path (unweighted)    |
| **Dijkstra**         | O((V+E) log V) | O(V)  | Shortest path (weighted)      |
| **Bellman-Ford**     | O(VE)          | O(V)  | Negative weights              |
| **Floyd-Warshall**   | O(V³)          | O(V²) | All pairs shortest path       |
| **Topological Sort** | O(V+E)         | O(V)  | DAG ordering                  |
| **Union Find**       | O(α(n))\*      | O(n)  | Connected components          |

\*α(n) ≈ O(1) - inverse Ackermann function

---

## 💡 Quick Recognition Guide

### O(1) - Constant

```python
# Array access
value = arr[5]

# Hash table lookup
value = hash_map[key]

# Basic arithmetic
result = a + b
```

### O(log n) - Logarithmic

```python
# Binary search
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    # ...

# Balanced tree operations
# Divide by 2 each iteration
```

### O(n) - Linear

```python
# Single loop
for i in range(n):
    process(arr[i])

# Multiple sequential loops
for x in arr:
    # ...
for y in arr:
    # ...
# O(n) + O(n) = O(n)
```

### O(n log n) - Linearithmic

```python
# Merge sort, quick sort, heap sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # log n levels
    right = merge_sort(arr[mid:])
    return merge(left, right)      # O(n) per level

# Sorting + iteration
arr.sort()  # O(n log n)
for x in arr:  # O(n)
    # ...
# Total: O(n log n)
```

### O(n²) - Quadratic

```python
# Nested loops (same array)
for i in range(n):
    for j in range(n):
        process(arr[i], arr[j])

# Bubble sort, selection sort
```

### O(2ⁿ) - Exponential

```python
# Recursive Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # 2 recursive calls

# Generate all subsets
# Each element: include or exclude
```

---

## ⚖️ Space Complexity Checklist

### O(1) Space - Constant

- ✅ Fixed number of variables
- ✅ In-place array modifications
- ✅ Iterative algorithms with constant temp storage

### O(log n) Space

- ✅ Binary search (recursive) - call stack
- ✅ Balanced tree recursion

### O(n) Space - Linear

- ✅ Hash tables
- ✅ Arrays/lists of size n
- ✅ Recursion depth n
- ✅ Queue/Stack for BFS/DFS

### O(n²) Space

- ✅ 2D matrices
- ✅ Adjacency matrix for graphs

---

## 🎯 Optimization Strategies

### From O(n²) to O(n)

```python
# ❌ O(n²) - Nested loops
for i in range(n):
    for j in range(n):
        if arr[i] + arr[j] == target:
            return [i, j]

# ✅ O(n) - Hash table
seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i
```

### From O(n²) to O(n log n)

```python
# ❌ O(n²) - Find all pairs
for i in range(n):
    for j in range(i+1, n):
        # process pair

# ✅ O(n log n) - Sort first
arr.sort()  # O(n log n)
left, right = 0, n-1
while left < right:  # O(n)
    # process with two pointers
```

### From O(2ⁿ) to O(n)

```python
# ❌ O(2ⁿ) - Naive recursion
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# ✅ O(n) - Memoization
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# ✅ O(n) - Iterative (O(1) space)
def fib(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
```

---

## 🧠 Rules of Thumb

### 1. Drop Constants

```
O(2n) → O(n)
O(n/2) → O(n)
O(100) → O(1)
```

### 2. Drop Non-Dominant Terms

```
O(n² + n) → O(n²)
O(n + log n) → O(n)
O(n! + 2ⁿ) → O(n!)
```

### 3. Different Variables

```python
# Two different arrays
for i in arr1:  # O(n)
    for j in arr2:  # O(m)
        # ...
# Time: O(n × m), NOT O(n²)!
```

### 4. Amortized vs Worst Case

```python
# Python list append
arr.append(x)  # O(1) amortized, O(n) worst case
# Most of the time O(1), occasionally O(n) for resizing
```

---

## 📏 Input Size vs Acceptable Complexity

| Input Size (n) | Max Acceptable Complexity | Example             |
| -------------- | ------------------------- | ------------------- |
| n ≤ 10         | O(n!)                     | Permutations        |
| n ≤ 20         | O(2ⁿ)                     | Subset generation   |
| n ≤ 100        | O(n⁴)                     | Four nested loops   |
| n ≤ 1,000      | O(n²)                     | Bubble sort         |
| n ≤ 100,000    | O(n log n)                | Merge sort          |
| n ≤ 1,000,000  | O(n)                      | Linear scan         |
| n > 1,000,000  | O(log n) or O(1)          | Binary search, hash |

**Rule**: ~10⁸ operations per second

---

## 🎓 Quick Reference

### When to use what?

| Need            | Use              | Complexity            |
| --------------- | ---------------- | --------------------- |
| Fast lookup     | Hash Table       | O(1)                  |
| Sorted data     | Binary Search    | O(log n)              |
| Process all     | Loop             | O(n)                  |
| Find pairs      | Two Pointers     | O(n)                  |
| Subarray        | Sliding Window   | O(n)                  |
| Range queries   | Prefix Sum       | O(1) per query        |
| Best sorting    | Merge/Quick Sort | O(n log n)            |
| Graph traversal | DFS/BFS          | O(V+E)                |
| Dynamic problem | DP/Memo          | Usually O(n²) or less |

---

**Print this and keep it handy while solving problems!** 📌
