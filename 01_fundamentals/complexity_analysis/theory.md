# ⏱️ Complexity Analysis - Phân tích độ phức tạp

## 📖 Tại sao cần học Complexity Analysis?

Khi giải quyết một bài toán, thường có **nhiều cách tiếp cận** khác nhau. Complexity Analysis giúp bạn:

- ✅ So sánh hiệu quả giữa các algorithms
- ✅ Dự đoán performance khi input size tăng
- ✅ Chọn data structure phù hợp
- ✅ Optimize code một cách có căn cứ

**Ví dụ thực tế**: Tìm một số trong mảng 1 triệu phần tử

- Cách 1: Duyệt từng phần tử → ~1 triệu operations
- Cách 2: Binary Search (nếu sorted) → ~20 operations

➡️ Cách 2 nhanh hơn **50,000 lần**! Đó là sức mạnh của algorithm design.

---

## 🎯 Big O Notation

### Định nghĩa

**Big O** mô tả **upper bound** (giới hạn trên) của tốc độ tăng trưởng thời gian/bộ nhớ khi input size (n) tăng.

### Ký hiệu:

- **O(...)** : Big O (upper bound - worst case thường dùng)
- **Ω(...)** : Big Omega (lower bound - best case)
- **Θ(...)** : Big Theta (tight bound - average case)

➡️ **Trong thực tế**, ta thường nói về **Big O** để đánh giá worst-case scenario.

---

## 📊 Các độ phức tạp thường gặp

### Bảng xếp hạng (từ tốt nhất → tệ nhất)

| Big O          | Tên gọi      | n=10  | n=100       | n=1000      | Ví dụ                                  |
| -------------- | ------------ | ----- | ----------- | ----------- | -------------------------------------- |
| **O(1)**       | Constant     | 1     | 1           | 1           | Truy cập array[i], hash lookup         |
| **O(log n)**   | Logarithmic  | 3     | 7           | 10          | Binary Search, BST operations          |
| **O(n)**       | Linear       | 10    | 100         | 1000        | Linear Search, duyệt array             |
| **O(n log n)** | Linearithmic | 30    | 700         | 10,000      | Merge Sort, Quick Sort                 |
| **O(n²)**      | Quadratic    | 100   | 10,000      | 1,000,000   | Bubble Sort, nested loops              |
| **O(n³)**      | Cubic        | 1,000 | 1,000,000   | 1B          | Triple nested loops                    |
| **O(2ⁿ)**      | Exponential  | 1,024 | 1.27×10³⁰   | Vô cùng lớn | Fibonacci recursion, subset generation |
| **O(n!)**      | Factorial    | 3.6M  | Vô cùng lớn | Vô cùng lớn | Permutations, Traveling Salesman       |

### Visualization:

```
Operations
    |
10⁹ |                                                    ╱ O(n!)
    |                                                ╱╱
10⁶ |                                          ╱╱╱╱  O(2ⁿ)
    |                                    ╱╱╱╱╱
10⁴ |                            ╱╱╱╱╱╱      O(n²)
    |                    ╱╱╱╱╱╱
10² |          ╱╱╱╱╱╱──────────              O(n log n)
    |  ────────────────────────              O(n)
 10 |  ──────────────────────────────────    O(log n)
  1 |  ───────────────────────────────────── O(1)
    |_____________________________________________
      1      10      100     1000    10000    n
```

---

## 🔍 Time Complexity (Độ phức tạp thời gian)

### 1. **O(1) - Constant Time**

Thời gian chạy **không phụ thuộc** vào input size.

```python
def get_first_element(arr):
    return arr[0]  # O(1)

def hash_lookup(hash_map, key):
    return hash_map[key]  # O(1)
```

**Đặc điểm**:

- Tốt nhất có thể
- Direct access
- Không có loops, không recursion

---

### 2. **O(log n) - Logarithmic Time**

Mỗi bước **giảm input size một nửa**.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:          # Loop chạy log₂(n) lần
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1        # Loại bỏ nửa bên trái
        else:
            right = mid - 1       # Loại bỏ nửa bên phải

    return -1
```

**Đặc điểm**:

- Chia input làm đôi mỗi iteration
- Rất hiệu quả với large datasets
- Log₂(1,000,000) = ~20 operations!

**Các algorithms O(log n)**:

- Binary Search
- BST search (balanced tree)
- Heap insert/delete

---

### 3. **O(n) - Linear Time**

Thời gian tỷ lệ **tuyến tính** với input size.

```python
def linear_search(arr, target):
    for i in range(len(arr)):     # Loop qua n elements
        if arr[i] == target:
            return i
    return -1

def sum_array(arr):
    total = 0
    for num in arr:               # O(n)
        total += num
    return total
```

**Đặc điểm**:

- Duyệt qua tất cả elements một lần
- Không thể tránh nếu cần xem tất cả data
- Acceptable cho hầu hết problems

**Lưu ý**: Multiple passes vẫn là O(n)

```python
def process_array(arr):
    # Pass 1: Sum
    total = sum(arr)              # O(n)

    # Pass 2: Count evens
    evens = sum(1 for x in arr if x % 2 == 0)  # O(n)

    return total, evens
    # Total: O(n) + O(n) = O(2n) = O(n)  ✓
```

---

### 4. **O(n log n) - Linearithmic Time**

Kết hợp của **linear** và **logarithmic**.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Chia array làm đôi (log n levels)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge hai nửa (n operations per level)
    return merge(left, right)
```

**Đặc điểm**:

- Best sorting algorithms đều là O(n log n)
- Divide-and-conquer approach
- Hiệu quả với large datasets

**Algorithms O(n log n)**:

- Merge Sort
- Quick Sort (average case)
- Heap Sort

---

### 5. **O(n²) - Quadratic Time**

**Nested loops** qua n elements.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Outer loop: n times
        for j in range(n - i - 1):  # Inner loop: n times
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_pairs_with_sum(arr, target):
    pairs = []
    for i in range(len(arr)):           # O(n)
        for j in range(i + 1, len(arr)):  # O(n)
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
    # Total: O(n²)
```

**Đặc điểm**:

- Không scalable với large inputs
- Acceptable chỉ với small data (n < 1000)
- Có thể optimize bằng hash tables hoặc sorting

**Khi nào chấp nhận O(n²)**:

- Small input size (n ≤ 100)
- Code simplicity là priority
- Không có better approach

---

### 6. **O(2ⁿ) - Exponential Time**

Mỗi step **nhân đôi** số operations.

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    # Mỗi call tạo ra 2 calls → 2ⁿ calls!
```

**Recursion Tree cho fib(5)**:

```
                    fib(5)
                  /        \
            fib(4)          fib(3)
           /      \        /      \
       fib(3)   fib(2)  fib(2)  fib(1)
       /    \
   fib(2) fib(1)
   ...
```

**Đặc điểm**:

- Grows **cực kỳ nhanh**
- Không practical cho n > 30
- Thường cần optimize bằng memoization/DP

**Algorithms O(2ⁿ)**:

- Naive recursive Fibonacci
- Subset generation (2ⁿ subsets)
- Backtracking without pruning

---

## 💾 Space Complexity (Độ phức tạp không gian)

Đo lường **bộ nhớ** algorithm sử dụng.

### Ví dụ:

```python
# O(1) space - constant
def sum_array(arr):
    total = 0  # Chỉ 1 variable
    for num in arr:
        total += num
    return total

# O(n) space - linear
def create_copy(arr):
    return arr[:]  # Tạo copy toàn bộ array

# O(n) space - recursion call stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
    # Call stack depth = n → O(n) space
```

**Lưu ý**:

- Input array không tính vào space complexity
- Chỉ tính auxiliary space (extra memory used)
- Recursion call stack cũng tính!

---

## 🎯 Rules để tính Complexity

### 1. **Drop Constants**

```python
O(2n) → O(n)
O(n + 500) → O(n)
O(13n²) → O(n²)
```

### 2. **Drop Non-Dominant Terms**

```python
O(n² + n) → O(n²)      # n² dominates
O(n + log n) → O(n)    # n dominates
O(2ⁿ + n³) → O(2ⁿ)     # 2ⁿ dominates
```

### 3. **Different Variables**

```python
def process_two_arrays(arr1, arr2):
    # Duyệt arr1
    for item in arr1:        # O(n)
        print(item)

    # Duyệt arr2
    for item in arr2:        # O(m)
        print(item)

    # Total: O(n + m), KHÔNG phải O(n)!
```

### 4. **Nested Loops với Different Variables**

```python
def nested_different(arr1, arr2):
    for item1 in arr1:         # O(n)
        for item2 in arr2:     # O(m)
            print(item1, item2)

    # Total: O(n × m)
```

---

## 🧮 Ví dụ phân tích

### Example 1: Simple Loop

```python
def example1(arr):
    for i in range(len(arr)):        # O(n)
        print(arr[i])                # O(1)

# Time: O(n)
# Space: O(1)
```

### Example 2: Nested Loops (same array)

```python
def example2(arr):
    for i in range(len(arr)):            # O(n)
        for j in range(len(arr)):        # O(n)
            print(arr[i], arr[j])        # O(1)

# Time: O(n²)
# Space: O(1)
```

### Example 3: Two Sequential Loops

```python
def example3(arr):
    for item in arr:        # O(n)
        print(item)

    for item in arr:        # O(n)
        print(item)

# Time: O(n) + O(n) = O(2n) = O(n)
# Space: O(1)
```

### Example 4: Loop + Sort

```python
def example4(arr):
    arr.sort()              # O(n log n)

    for item in arr:        # O(n)
        print(item)

# Time: O(n log n) + O(n) = O(n log n)  ← dominant term
# Space: O(1) for in-place sort
```

### Example 5: Recursive with Memoization

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]      # O(1)

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Time: O(n) - each value computed once
# Space: O(n) - memo dictionary + call stack
```

---

## 🎓 Best/Average/Worst Case

Một số algorithms có performance khác nhau tùy input:

### Quick Sort Example:

- **Best Case**: O(n log n) - pivot luôn chia đều
- **Average Case**: O(n log n) - pivot random
- **Worst Case**: O(n²) - pivot luôn min/max (sorted array)

### Binary Search:

- **Best Case**: O(1) - tìm thấy ngay ở mid
- **Average Case**: O(log n)
- **Worst Case**: O(log n) - phải search hết

➡️ **Trong interviews**, thường nói về **Worst Case** (Big O).

---

## ⚡ Cách Optimize Complexity

### 1. **Hash Table thay vì Nested Loop**

```python
# Bad: O(n²)
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

# Good: O(n)
def two_sum_hash(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### 2. **Sort + Two Pointers thay vì Nested Loop**

```python
# Bad: O(n²)
def find_pairs_brute(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 10:
                pairs.append((arr[i], arr[j]))
    return pairs

# Good: O(n log n)
def find_pairs_optimized(arr):
    arr.sort()  # O(n log n)
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:  # O(n)
        current_sum = arr[left] + arr[right]
        if current_sum == 10:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < 10:
            left += 1
        else:
            right -= 1

    return pairs
```

### 3. **Memoization cho Recursion**

```python
# Bad: O(2ⁿ)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Good: O(n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

---

## 📝 Practice Problems

1. Phân tích time & space complexity của đoạn code sau:

```python
def mystery(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result.append(arr[i] + arr[j])
    return result
```

2. Optimize đoạn code này từ O(n²) xuống O(n):

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

3. Tính complexity của merge sort cho array size n = 1000.

---

## 🎯 Key Takeaways

1. **Big O** mô tả growth rate, không phải exact time
2. **Drop constants** và **non-dominant terms**
3. **O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)**
4. **Hash tables** thường giúp reduce từ O(n²) → O(n)
5. **Sorting + Two Pointers** là alternative cho nested loops
6. **Memoization** biến O(2ⁿ) thành O(n)
7. **Space complexity** cũng quan trọng, nhất là với large data

---

## ➡️ Next Steps

- 📖 Đọc [Examples & Code](examples.py)
- 💻 Làm [Practice Problems](practice.md)
- 📊 Xem [Complexity Cheat Sheet](../../resources/cheatsheets/complexity_cheatsheet.md)

**Bắt đầu với Arrays & Strings**: [02_linear_structures/arrays/theory.md](../../02_linear_structures/arrays/theory.md)
