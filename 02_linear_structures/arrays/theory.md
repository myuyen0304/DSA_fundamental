# 📊 Arrays - Mảng

## 📖 Array là gì?

**Array** là cấu trúc dữ liệu lưu trữ tập hợp các elements **cùng kiểu** trong **bộ nhớ liên tiếp**.

### Đặc điểm quan trọng:

- ✅ **Contiguous memory**: Elements được lưu liền kề nhau
- ✅ **Fixed size**: Size xác định khi khởi tạo (trong hầu hết ngôn ngữ)
- ✅ **Index-based access**: Truy cập O(1) qua index
- ✅ **Same data type**: Tất cả elements cùng type

### Visual Representation:

```
Array: [10, 20, 30, 40, 50]

Memory:
┌─────┬─────┬─────┬─────┬─────┐
│ 10  │ 20  │ 30  │ 40  │ 50  │
└─────┴─────┴─────┴─────┴─────┘
  [0]   [1]   [2]   [3]   [4]  ← indices
```

---

## ⚡ Time Complexity

| Operation                      | Time     | Giải thích                        |
| ------------------------------ | -------- | --------------------------------- |
| **Access** `arr[i]`            | O(1)     | Direct memory address calculation |
| **Search** (unsorted)          | O(n)     | Phải duyệt qua tất cả elements    |
| **Search** (sorted)            | O(log n) | Binary search                     |
| **Insert** at end              | O(1)\*   | Thêm vào cuối (nếu còn space)     |
| **Insert** at beginning/middle | O(n)     | Phải shift elements               |
| **Delete** at end              | O(1)     | Xóa element cuối                  |
| **Delete** at beginning/middle | O(n)     | Phải shift elements               |
| **Update** `arr[i] = x`        | O(1)     | Direct access                     |

\*O(1) amortized nếu dynamic array (Python list, Java ArrayList)

---

## 🎯 Khi nào dùng Arrays?

### ✅ Nên dùng Arrays khi:

1. **Biết trước số lượng elements** hoặc limit rõ ràng
2. **Cần random access** - truy cập element bất kỳ nhanh
3. **Iterate qua tất cả elements** nhiều lần
4. **Memory efficiency** - không cần overhead của linked list
5. **Cache-friendly** - data locality tốt

### ❌ Không nên dùng Arrays khi:

1. **Frequent insertions/deletions** ở giữa array
2. **Unknown size** và cần grow/shrink thường xuyên
3. **Cần maintain sorted order** với many inserts

---

## 🔍 Array vs Python List

### Python List (Dynamic Array)

Python's `list` là **dynamic array**, không phải array truyền thống:

```python
# Python list tự động resize
arr = []           # Empty list
arr.append(1)      # [1]
arr.append(2)      # [1, 2]
arr.append(3)      # [1, 2, 3] - auto grows
```

### Key Differences:

| Feature    | Static Array                      | Python List                        |
| ---------- | --------------------------------- | ---------------------------------- |
| **Size**   | Fixed                             | Dynamic (auto-resize)              |
| **Memory** | Contiguous, exact                 | Contiguous, but với extra capacity |
| **Append** | O(1) nếu có space, else không thể | O(1) amortized                     |
| **Type**   | Homogeneous (cùng type)           | Heterogeneous (mixed types)        |

### Python List Internals:

```python
# Python list maintains:
# 1. Size (số elements hiện tại)
# 2. Capacity (tổng space allocated)

arr = [1, 2, 3]
# Actual memory: [1, 2, 3, _, _, _]
#                 ^size=3  ^unused capacity
```

**Resizing**:

- Khi full, Python tạo array MỚI với capacity lớn hơn (~1.5x - 2x)
- Copy tất cả elements sang array mới
- Free old array
- Amortized O(1) cho append

---

## 🛠️ Common Operations

### 1. Traversal (Duyệt qua Array)

```python
# Forward traversal
for i in range(len(arr)):
    print(arr[i])

# Better: Direct iteration
for element in arr:
    print(element)

# With index
for i, element in enumerate(arr):
    print(f"Index {i}: {element}")

# Reverse traversal
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])
```

### 2. Search

#### Linear Search - O(n)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

#### Binary Search - O(log n) [Sorted array only]

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### 3. Insertion

```python
# At end - O(1)
arr.append(element)

# At specific index - O(n)
arr.insert(index, element)  # Shifts elements

# At beginning - O(n)
arr.insert(0, element)
```

### 4. Deletion

```python
# Remove by value - O(n)
arr.remove(element)  # Removes first occurrence

# Remove by index - O(n)
del arr[index]
arr.pop(index)

# Remove last element - O(1)
arr.pop()
```

---

## 🎓 Important Techniques

### 1️⃣ **Two Pointers**

Dùng 2 pointers để traverse array, thường để:

- Find pairs
- Remove duplicates
- Reverse array
- Merge sorted arrays

**Example: Remove Duplicates từ Sorted Array**

```python
def remove_duplicates(arr):
    if not arr:
        return 0

    write_idx = 1  # Pointer cho position ghi

    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[read_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    return write_idx  # New length

# arr = [1, 1, 2, 2, 3, 4, 4]
# After: [1, 2, 3, 4, _, _, _]
```

**Example: Two Sum với Sorted Array**

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return []
```

### 2️⃣ **Sliding Window**

Maintain một "window" (subarray) với specific properties:

- Fixed size window
- Variable size window
- Optimize từ O(n²) nested loops xuống O(n)

**Example: Max Sum Subarray of Size K**

```python
def max_sum_subarray(arr, k):
    # O(n) - Sliding window
    window_sum = sum(arr[:k])  # First window
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Slide window: add new, remove old
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

**Example: Longest Substring Without Repeating Characters**

```python
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1  # Shrink window

        seen[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

### 3️⃣ **Prefix Sum**

Pre-compute cumulative sums để answer range queries nhanh.

**Example: Range Sum Queries**

```python
def build_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix

def range_sum(prefix, left, right):
    # Sum from arr[left] to arr[right]
    return prefix[right + 1] - prefix[left]

# arr = [1, 2, 3, 4, 5]
# prefix = [0, 1, 3, 6, 10, 15]
# Sum[1:3] = prefix[4] - prefix[1] = 10 - 1 = 9 ✓
```

### 4️⃣ **Kadane's Algorithm** (Max Subarray Sum)

Find contiguous subarray với largest sum.

```python
def max_subarray_sum(arr):
    # O(n) - Dynamic Programming approach
    max_ending_here = max_so_far = arr[0]

    for i in range(1, len(arr)):
        # Either extend current subarray or start new
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Max subarray: [4, -1, 2, 1] = 6
```

### 5️⃣ **Dutch National Flag** (3-Way Partitioning)

Partition array thành 3 parts: low, mid, high.

**Example: Sort Colors (0s, 1s, 2s)**

```python
def sort_colors(arr):
    # O(n) time, O(1) space
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# [2, 0, 2, 1, 1, 0] → [0, 0, 1, 1, 2, 2]
```

---

## 🔄 Array Rotation

### Left Rotate by k positions

**Method 1: Using Slicing - O(n) time, O(n) space**

```python
def rotate_left_slice(arr, k):
    k = k % len(arr)  # Handle k > len
    return arr[k:] + arr[:k]
```

**Method 2: Reversal Algorithm - O(n) time, O(1) space**

```python
def rotate_left_reversal(arr, k):
    n = len(arr)
    k = k % n

    # Reverse first k elements
    reverse(arr, 0, k - 1)
    # Reverse remaining elements
    reverse(arr, k, n - 1)
    # Reverse entire array
    reverse(arr, 0, n - 1)

    return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
```

---

## 🎯 Common Patterns & Tricks

### 1. **Hash Table để reduce O(n²) → O(n)**

```python
# Instead of nested loop
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # Check something

# Use hash table
seen = set()
for element in arr:
    # Check in O(1)
    if complement in seen:
        return result
    seen.add(element)
```

### 2. **Sort + Two Pointers**

Many array problems become easier after sorting.

### 3. **Index as Hash Key**

Nếu elements trong range [0, n-1], dùng array như hash table.

### 4. **XOR Tricks**

- `a ^ a = 0`
- `a ^ 0 = a`
- XOR is commutative & associative

**Find Single Number** (all others appear twice):

```python
def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result  # All pairs cancel out
```

### 5. **Floyd's Cycle Detection**

Find duplicates in O(n) time, O(1) space.

---

## ⚠️ Common Pitfalls

### 1. Off-by-One Errors

```python
# Wrong
for i in range(len(arr)):
    if arr[i + 1]:  # IndexError when i = len-1
        ...

# Correct
for i in range(len(arr) - 1):
    if arr[i + 1]:
        ...
```

### 2. Modifying Array While Iterating

```python
# Dangerous
for element in arr:
    arr.remove(element)  # Can skip elements!

# Better
arr = [x for x in arr if condition(x)]
```

### 3. Integer Overflow in Binary Search

```python
# Wrong (can overflow)
mid = (left + right) // 2

# Correct
mid = left + (right - left) // 2
```

### 4. Not Handling Empty Array

```python
def process(arr):
    if not arr:  # Always check!
        return None
    # ... process
```

---

## 📊 Complexity Cheat Sheet

| Technique      | Time                   | Space        | Use Case                |
| -------------- | ---------------------- | ------------ | ----------------------- |
| Two Pointers   | O(n)                   | O(1)         | Sorted array, pairs     |
| Sliding Window | O(n)                   | O(1)         | Subarray problems       |
| Prefix Sum     | O(n) build, O(1) query | O(n)         | Range sum queries       |
| Binary Search  | O(log n)               | O(1)         | Sorted array search     |
| Sorting        | O(n log n)             | O(1) to O(n) | Preprocessing           |
| Hash Table     | O(n)                   | O(n)         | Lookup, frequency count |

---

## 🎓 Key Takeaways

1. **Arrays provide O(1) access** - exploit this!
2. **Two Pointers** và **Sliding Window** là most common patterns
3. **Hash Tables** thường giúp optimize từ O(n²) → O(n)
4. **Sorting** có thể simplify problem (O(n log n) preprocessing)
5. **Prefix Sum** cho efficient range queries
6. **Always check edge cases**: empty array, single element, duplicates
7. **Space-time tradeoff**: Hash table (O(n) space) vs Two Pointers (O(1) space)

---

## ➡️ Next Steps

- 💻 Xem [Implementation Code](implementation.py)
- 📝 Làm [15 Practice Problems](practice.md)
- ✅ Check [Solutions](solutions.py)
- 📖 Đọc tiếp [Strings](../strings/theory.md)

**Bắt đầu với practice problems để apply các techniques này!** 🚀
