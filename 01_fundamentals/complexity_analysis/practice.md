# 🏋️ Complexity Analysis - Practice Problems

## 📝 Bài tập 1: Phân tích Complexity

Xác định **Time** và **Space Complexity** của các đoạn code sau:

### Problem 1.1

```python
def problem1(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

<details>
<summary>💡 Gợi ý</summary>

- Có bao nhiêu loops?
- Loop chạy bao nhiêu lần?
- Có dùng extra memory không?
</details>

<details>
<summary>✅ Đáp án</summary>

**Time**: O(n) - Duyệt qua n elements một lần
**Space**: O(1) - Chỉ dùng variable `total`

</details>

---

### Problem 1.2

```python
def problem2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i] + arr[j])
```

<details>
<summary>💡 Gợi ý</summary>

- Nested loops cùng iterate qua array?
- Inner loop phụ thuộc vào outer loop không?
</details>

<details>
<summary>✅ Đáp án</summary>

**Time**: O(n²) - Hai nested loops, mỗi loop n iterations
**Space**: O(1) - Không dùng extra memory

</details>

---

### Problem 1.3

```python
def problem3(arr):
    arr.sort()  # Assume Python's Timsort
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False
```

<details>
<summary>💡 Gợi ý</summary>

- Complexity của sort là gì?
- Complexity của loop là gì?
- Đâu là dominant term?
</details>

<details>
<summary>✅ Đáp án</summary>

**Time**: O(n log n) - Sort O(n log n) + Loop O(n) → O(n log n) dominates
**Space**: O(1) or O(n) depending on sort implementation (Timsort uses O(n) worst case)

</details>

---

### Problem 1.4

```python
def problem4(n):
    if n <= 1:
        return n
    return problem4(n - 1) + problem4(n - 2)
```

<details>
<summary>💡 Gợi ý</summary>

- Đây là Fibonacci recursive
- Mỗi call tạo ra bao nhiêu recursive calls?
- Call stack depth là bao nhiêu?
</details>

<details>
<summary>✅ Đáp án</summary>

**Time**: O(2ⁿ) - Mỗi call tạo 2 calls, exponential growth
**Space**: O(n) - Maximum call stack depth là n

</details>

---

### Problem 1.5

```python
def problem5(arr1, arr2):
    result = []
    for item1 in arr1:
        for item2 in arr2:
            if item1 == item2:
                result.append(item1)
    return result
```

<details>
<summary>💡 Gợi ý</summary>

- Hai arrays có thể khác size
- Dùng variables khác nhau: n và m
</details>

<details>
<summary>✅ Đáp án</summary>

**Time**: O(n × m) where n = len(arr1), m = len(arr2)
**Space**: O(min(n, m)) - Worst case: tất cả elements trùng

</details>

---

### Problem 1.6

```python
def problem6(arr):
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

<details>
<summary>✅ Đáp án</summary>

**Time**: O(log n) - Binary search, giảm search space đi một nửa mỗi iteration
**Space**: O(1) - Chỉ dùng 3 variables (left, right, mid)

</details>

---

### Problem 1.7

```python
def problem7(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = problem7(arr[:mid])
    right = problem7(arr[mid:])

    return merge(left, right)  # merge is O(n)
```

<details>
<summary>💡 Gợi ý</summary>

- Đây là Merge Sort
- Log n levels, mỗi level O(n) work
</details>

<details>
<summary>✅ Đáp án</summary>

**Time**: O(n log n) - Divide: log n levels, Conquer: O(n) per level
**Space**: O(n) - Temporary arrays trong merge

</details>

---

## 🎯 Bài tập 2: Tối ưu hóa Complexity

Optimize các đoạn code sau để có complexity tốt hơn:

### Problem 2.1: Two Sum

**Given**: Array và target sum
**Task**: Tìm 2 indices có tổng = target

```python
# Current: O(n²)
def two_sum_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []
```

**Challenge**: Optimize xuống **O(n)**

<details>
<summary>💡 Gợi ý</summary>

- Sử dụng hash table để store seen values
- Check complement (target - current) trong hash
</details>

<details>
<summary>✅ Solution</summary>

```python
def two_sum_fast(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Time: O(n) - Single pass
# Space: O(n) - Hash table
```

</details>

---

### Problem 2.2: Find Duplicates

**Given**: Array of integers
**Task**: Check if có duplicate

```python
# Current: O(n²)
def has_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

**Challenge**: Optimize xuống **O(n)**

<details>
<summary>💡 Gợi ý</summary>

Có 2 approaches:

1. Hash Set - O(n) time, O(n) space
2. Sort + compare adjacent - O(n log n) time, O(1) space
</details>

<details>
<summary>✅ Solution 1: Hash Set</summary>

```python
def has_duplicate_fast(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time: O(n)
# Space: O(n)
```

</details>

<details>
<summary>✅ Solution 2: Sort</summary>

```python
def has_duplicate_sort(arr):
    arr.sort()  # O(n log n)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False

# Time: O(n log n)
# Space: O(1) if in-place sort
```

</details>

---

### Problem 2.3: Fibonacci

**Given**: Integer n
**Task**: Compute nth Fibonacci number

```python
# Current: O(2ⁿ) - Cực kỳ chậm!
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)
```

**Challenge**: Optimize xuống **O(n)**

<details>
<summary>💡 Gợi ý</summary>

Có 2 approaches:

1. Memoization (Top-down DP)
2. Iterative (Bottom-up)
</details>

<details>
<summary>✅ Solution 1: Memoization</summary>

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Time: O(n) - Mỗi value tính 1 lần
# Space: O(n) - Memo dict + call stack
```

</details>

<details>
<summary>✅ Solution 2: Iterative (Best Space)</summary>

```python
def fib_iterative(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

# Time: O(n)
# Space: O(1) - Chỉ 2 variables
```

</details>

---

### Problem 2.4: Find Pairs with Given Sum

**Given**: Array và target sum
**Task**: Tìm TẤT CẢ các cặp có tổng = target

```python
# Current: O(n²)
def find_pairs_slow(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
```

**Challenge**: Optimize xuống **O(n log n)**

<details>
<summary>💡 Gợi ý</summary>

- Sort array trước: O(n log n)
- Dùng two pointers: O(n)
- Total: O(n log n)
</details>

<details>
<summary>✅ Solution</summary>

```python
def find_pairs_fast(arr, target):
    arr.sort()  # O(n log n)
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:  # O(n)
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

# Time: O(n log n) - Sort dominates
# Space: O(1) excluding output
```

</details>

---

## 🧠 Bài tập 3: Complexity Quiz

### Question 3.1

Đoạn code nào có Time Complexity là O(n)?

A)

```python
for i in range(n):
    for j in range(n):
        print(i + j)
```

B)

```python
for i in range(n):
    print(i)
for j in range(n):
    print(j)
```

C)

```python
for i in range(n):
    for j in range(i):
        print(i + j)
```

<details>
<summary>✅ Đáp án</summary>

**B** là O(n)

- A: O(n²) - Nested loops cùng n
- B: O(n) - Two sequential loops: O(n) + O(n) = O(n)
- C: O(n²) - Inner loop phụ thuộc i, tổng là n(n-1)/2 = O(n²)
</details>

---

### Question 3.2

Simplify: O(3n² + 5n + 100)

<details>
<summary>✅ Đáp án</summary>

**O(n²)**

Giải thích:

- Drop constants: 3n² → n²
- Drop non-dominant terms: n² >> n và n² >> 100
- Result: O(n²)
</details>

---

### Question 3.3

Code nào KHÔNG phải O(log n)?

A) Binary Search
B) BST search (balanced tree)
C) Finding mid element của sorted array
D) Heap insert

<details>
<summary>✅ Đáp án</summary>

**C** - Finding mid element is O(1)

Các còn lại:

- A, B, D đều O(log n) vì giảm problem size đi một nửa mỗi step
</details>

---

### Question 3.4

Cho hai arrays: arr1 (size n) và arr2 (size m).
Complexity của nested loop qua cả hai là gì?

```python
for item1 in arr1:
    for item2 in arr2:
        print(item1, item2)
```

<details>
<summary>✅ Đáp án</summary>

**O(n × m)** hoặc **O(nm)**

KHÔNG phải O(n²) vì hai arrays có thể khác size!

</details>

---

## 🎓 Bài tập 4: Real-World Scenarios

### Scenario 4.1: Social Media Feed

Bạn đang build một social media feed. Có 3 approaches:

**Approach A**: Mỗi lần load feed, query database cho tất cả friends' posts, sort by time

- Query: O(n) where n = số friends
- Sort: O(m log m) where m = total posts
- Total: O(n + m log m)

**Approach B**: Pre-compute và cache sorted feed, update khi có post mới

- Load: O(k) where k = số posts hiển thị (e.g., 20)
- Update: O(log m) insert vào sorted list
- Total: O(k) cho load, O(log m) cho update

**Question**: Approach nào tốt hơn? Tại sao?

<details>
<summary>✅ Đáp án & Analysis</summary>

**Approach B tốt hơn** cho hầu hết cases:

**Reasons**:

1. Read operations (load feed) >> Write operations (post)
2. Users load feed nhiều lần, nhưng post ít
3. O(k) với k = 20 là constant → O(1) trong thực tế
4. Trade space for time - worth it!

**Trade-offs**:

- B dùng nhiều memory hơn (cache)
- A dùng ít memory, nhưng slow mỗi lần load
- For social media: Speed > Memory → Choose B
</details>

---

### Scenario 4.2: Autocomplete Search

Implement autocomplete feature. Có 2 options:

**Option A**: Linear search qua tất cả words

- Time: O(n) per query
- Space: O(1)

**Option B**: Trie data structure

- Build Trie: O(n × L) where L = average word length
- Search: O(L) per query
- Space: O(n × L)

**Question**: Option nào nên chọn? Khi nào chọn option kia?

<details>
<summary>✅ Đáp án & Analysis</summary>

**Option B (Trie) tốt hơn** cho autocomplete:

**Reasons**:

1. Queries rất nhiều, O(L) << O(n)
2. L thường nhỏ (< 20 characters)
3. Autocomplete yêu cầu real-time speed

**When to use Option A**:

- Dictionary rất nhỏ (< 100 words)
- Memory constrained
- Infrequent searches
- One-time operation

**Real-world**:

- Google, IDE autocomplete dùng Trie
- Trade memory for speed
</details>

---

## 🏆 Challenge Problems

### Challenge 1: Optimize This!

```python
def mystery_function(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == 0:
                result.append((arr[i], arr[j]))
    return result
```

**Tasks**:

1. Phân tích current complexity
2. Giải thích function làm gì
3. Optimize xuống O(n)
4. Implement optimized version

<details>
<summary>💡 Gợi ý</summary>

- Function tìm các cặp có tổng = 0
- Current: O(n²) với nested loops
- Optimize: Hash set để check complement
</details>

---

### Challenge 2: Complexity Comparison

Cho array size n = 1,000,000. Estimate thời gian chạy:

**Given**: 1 operation = 1 nanosecond (1 billionth of a second)

| Complexity      | Operations        | Time |
| --------------- | ----------------- | ---- |
| O(1)            | 1                 | ?    |
| O(log n)        | ~20               | ?    |
| O(n)            | 1,000,000         | ?    |
| O(n log n)      | ~20,000,000       | ?    |
| O(n²)           | 1,000,000,000,000 | ?    |
| O(2ⁿ) with n=30 | ~1,000,000,000    | ?    |

**Calculate** và **convert to seconds/minutes**.

<details>
<summary>✅ Đáp án</summary>

| Complexity | Operations        | Time            |
| ---------- | ----------------- | --------------- |
| O(1)       | 1                 | 1 nanosecond    |
| O(log n)   | ~20               | 20 nanoseconds  |
| O(n)       | 1,000,000         | 1 millisecond   |
| O(n log n) | ~20,000,000       | 20 milliseconds |
| O(n²)      | 1,000,000,000,000 | ~16.7 minutes   |
| O(2³⁰)     | ~1,000,000,000    | 1 second        |

**Key Insight**: O(n²) với large n là không practical!

</details>

---

## 📚 Next Steps

Sau khi hoàn thành practice này:

1. ✅ Chạy code trong [examples.py](examples.py) để thấy performance differences
2. ✅ Đọc tiếp [Arrays & Strings Theory](../../02_linear_structures/arrays/theory.md)
3. ✅ Check [Complexity Cheat Sheet](../../resources/cheatsheets/complexity_cheatsheet.md)

**Remember**: Understanding complexity là foundation để become good programmer! 🚀
