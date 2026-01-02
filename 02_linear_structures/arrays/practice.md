# 🏋️ Arrays - Practice Problems

## 📝 Hướng dẫn sử dụng

**Cách tiếp cận mỗi problem**:

1. ⏱️ Đọc đề bài, nghĩ 20-30 phút
2. 💡 Nếu stuck, đọc Hint
3. ✍️ Implement solution
4. ✅ Test với examples
5. 📖 So sánh với Solution
6. 🔄 Redo sau 3 ngày

---

## 🎯 Level 1: Easy (Two Pointers Basics)

### Problem 1: Two Sum (Sorted Array)

**Difficulty**: Easy  
**Pattern**: Two Pointers

**Problem**:
Cho sorted array và target sum, tìm 2 indices có tổng = target.

```python
Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1]  # arr[0] + arr[1] = 2 + 7 = 9
```

**Constraints**:

- 2 ≤ arr.length ≤ 10⁴
- Array is sorted in ascending order
- Exactly one solution exists

<details>
<summary>💡 Hint</summary>

- Use two pointers: left at start, right at end
- If sum < target, move left pointer right
- If sum > target, move right pointer left
- Time: O(n), Space: O(1)
</details>

<details>
<summary>✅ Solution</summary>

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Time: O(n)
# Space: O(1)
```

</details>

---

### Problem 2: Remove Duplicates from Sorted Array

**Difficulty**: Easy  
**Pattern**: Two Pointers (Fast & Slow)

**Problem**:
Remove duplicates in-place từ sorted array. Return new length.

```python
Input: arr = [1, 1, 2, 2, 3, 4, 4]
Output: 4
# arr becomes [1, 2, 3, 4, _, _, _]
```

**Constraints**:

- 0 ≤ arr.length ≤ 3 × 10⁴
- Array is sorted
- Modify array in-place

<details>
<summary>💡 Hint</summary>

- Use write_idx for position to write next unique element
- Compare current with previous
- Only write if different
</details>

<details>
<summary>✅ Solution</summary>

```python
def remove_duplicates(arr):
    if not arr:
        return 0

    write_idx = 1

    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[read_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    return write_idx

# Time: O(n)
# Space: O(1)
```

</details>

---

### Problem 3: Move Zeros

**Difficulty**: Easy  
**Pattern**: Two Pointers

**Problem**:
Move all zeros to end, maintain order of non-zeros.

```python
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

<details>
<summary>💡 Hint</summary>

- Move all non-zeros to front first
- Fill remaining with zeros
</details>

<details>
<summary>✅ Solution</summary>

```python
def move_zeros(arr):
    write_idx = 0

    # Move non-zeros to front
    for read_idx in range(len(arr)):
        if arr[read_idx] != 0:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    # Fill remaining with zeros
    for i in range(write_idx, len(arr)):
        arr[i] = 0

    return arr

# Time: O(n)
# Space: O(1)
```

</details>

---

### Problem 4: Valid Palindrome

**Difficulty**: Easy  
**Pattern**: Two Pointers

**Problem**:
Check if string is palindrome (ignore non-alphanumeric, case-insensitive).

```python
Input: "A man, a plan, a canal: Panama"
Output: True
```

<details>
<summary>✅ Solution</summary>

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Time: O(n)
# Space: O(1)
```

</details>

---

### Problem 5: Reverse String

**Difficulty**: Easy  
**Pattern**: Two Pointers

**Problem**:
Reverse string in-place.

```python
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

<details>
<summary>✅ Solution</summary>

```python
def reverse_string(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

# Time: O(n)
# Space: O(1)
```

</details>

---

## 🎯 Level 2: Easy-Medium (Sliding Window)

### Problem 6: Maximum Sum Subarray of Size K

**Difficulty**: Easy  
**Pattern**: Sliding Window (Fixed Size)

**Problem**:
Find maximum sum of any subarray of size K.

```python
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
# Subarray [5, 1, 3] has sum = 9
```

<details>
<summary>💡 Hint</summary>

- Compute sum of first window
- Slide: add new element, subtract leftmost
- Track maximum
</details>

<details>
<summary>✅ Solution</summary>

```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Time: O(n)
# Space: O(1)
```

</details>

---

### Problem 7: Longest Substring Without Repeating Characters

**Difficulty**: Medium  
**Pattern**: Sliding Window (Variable Size)

**Problem**:
Find length of longest substring without repeating characters.

```python
Input: "abcabcbb"
Output: 3  # "abc"
```

<details>
<summary>💡 Hint</summary>

- Use hash map to track last seen position
- Shrink window when duplicate found
</details>

<details>
<summary>✅ Solution</summary>

```python
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n)
# Space: O(min(n, alphabet_size))
```

</details>

---

### Problem 8: Minimum Window Substring

**Difficulty**: Hard  
**Pattern**: Sliding Window

**Problem**:
Find minimum window in S that contains all characters from T.

```python
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

<details>
<summary>💡 Hint</summary>

- Use two hash maps: required and window
- Expand window until valid
- Shrink window while valid
</details>

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter

def min_window_substring(s, t):
    if not s or not t:
        return ""

    required = Counter(t)
    window = {}
    have, need = 0, len(required)

    result = [-1, -1]
    min_len = float('inf')
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            have += 1

        while have == need:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = [left, right]

            char = s[left]
            window[char] -= 1
            if char in required and window[char] < required[char]:
                have -= 1
            left += 1

    return s[result[0]:result[1]+1] if min_len != float('inf') else ""

# Time: O(|S| + |T|)
# Space: O(|S| + |T|)
```

</details>

---

## 🎯 Level 3: Medium (Hash Table + Arrays)

### Problem 9: Two Sum (Unsorted Array)

**Difficulty**: Easy  
**Pattern**: Hash Table

**Problem**:
Find two indices with target sum (unsorted array).

```python
Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

<details>
<summary>✅ Solution</summary>

```python
def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

# Time: O(n)
# Space: O(n)
```

</details>

---

### Problem 10: Contains Duplicate

**Difficulty**: Easy  
**Pattern**: Hash Set

**Problem**:
Return true if any value appears twice.

```python
Input: [1, 2, 3, 1]
Output: True
```

<details>
<summary>✅ Solution</summary>

```python
def contains_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Alternative: return len(arr) != len(set(arr))

# Time: O(n)
# Space: O(n)
```

</details>

---

### Problem 11: Group Anagrams

**Difficulty**: Medium  
**Pattern**: Hash Map

**Problem**:
Group strings that are anagrams.

```python
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

<details>
<summary>💡 Hint</summary>

- Use sorted string as key
- Group strings with same sorted form
</details>

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())

# Time: O(n × k log k) where k = max string length
# Space: O(n × k)
```

</details>

---

## 🎯 Level 4: Medium (Prefix Sum & Kadane's)

### Problem 12: Maximum Subarray (Kadane's Algorithm)

**Difficulty**: Medium  
**Pattern**: Kadane's Algorithm

**Problem**:
Find contiguous subarray with largest sum.

```python
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6  # [4, -1, 2, 1]
```

<details>
<summary>✅ Solution</summary>

```python
def max_subarray_sum(arr):
    if not arr:
        return 0

    max_ending_here = max_so_far = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Time: O(n)
# Space: O(1)
```

</details>

---

### Problem 13: Subarray Sum Equals K

**Difficulty**: Medium  
**Pattern**: Prefix Sum + Hash Map

**Problem**:
Count number of subarrays with sum = K.

```python
Input: arr = [1, 1, 1], k = 2
Output: 2  # [1,1] appears twice
```

<details>
<summary>💡 Hint</summary>

- Use prefix sum
- Check if (prefix_sum - k) exists in map
</details>

<details>
<summary>✅ Solution</summary>

```python
def subarray_sum(arr, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}

    for num in arr:
        prefix_sum += num

        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count

# Time: O(n)
# Space: O(n)
```

</details>

---

### Problem 14: Product of Array Except Self

**Difficulty**: Medium  
**Pattern**: Prefix/Suffix Products

**Problem**:
Return array where output[i] = product of all except arr[i].
Cannot use division.

```python
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

<details>
<summary>✅ Solution</summary>

```python
def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result

# Time: O(n)
# Space: O(1) excluding output
```

</details>

---

## 🎯 Level 5: Medium-Hard (Binary Search)

### Problem 15: Binary Search

**Difficulty**: Easy  
**Pattern**: Binary Search

**Problem**:
Search target in sorted array. Return index or -1.

```python
Input: arr = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

<details>
<summary>✅ Solution</summary>

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Time: O(log n)
# Space: O(1)
```

</details>

---

### Problem 16: Search in Rotated Sorted Array

**Difficulty**: Medium  
**Pattern**: Modified Binary Search

**Problem**:
Search in rotated sorted array.

```python
Input: arr = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

<details>
<summary>💡 Hint</summary>

- One half is always sorted
- Determine which half is sorted
- Check if target in sorted half
</details>

<details>
<summary>✅ Solution</summary>

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Time: O(log n)
# Space: O(1)
```

</details>

---

## 📈 Progress Tracker

Mark problems as you complete them:

**Easy (Two Pointers)**:

- [ ] Problem 1: Two Sum (Sorted)
- [ ] Problem 2: Remove Duplicates
- [ ] Problem 3: Move Zeros
- [ ] Problem 4: Valid Palindrome
- [ ] Problem 5: Reverse String

**Easy-Medium (Sliding Window)**:

- [ ] Problem 6: Max Sum Subarray
- [ ] Problem 7: Longest Substring Without Repeating
- [ ] Problem 8: Minimum Window Substring

**Medium (Hash Table)**:

- [ ] Problem 9: Two Sum (Unsorted)
- [ ] Problem 10: Contains Duplicate
- [ ] Problem 11: Group Anagrams

**Medium (Prefix Sum)**:

- [ ] Problem 12: Maximum Subarray
- [ ] Problem 13: Subarray Sum Equals K
- [ ] Problem 14: Product Except Self

**Medium-Hard (Binary Search)**:

- [ ] Problem 15: Binary Search
- [ ] Problem 16: Search in Rotated Array

---

## 🎓 Study Tips

1. **Do problems in order** - They're arranged by difficulty
2. **Spend 20-30 min** thinking before checking hints
3. **Implement from scratch** after seeing solution
4. **Redo problems** after 3 days
5. **Track your progress** in progress.md

---

## ➡️ Next Steps

After completing these 16 problems:

- ✅ Move to [Linked Lists](../../02_linear_structures/linked_lists/practice.md)
- 📖 Review [Common Patterns](../../resources/patterns/common_patterns.md)
- 🎯 Try [LeetCode](https://leetcode.com) problems tagged "Array"

**Keep practicing! Consistency is key! 🚀**
