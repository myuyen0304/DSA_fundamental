"""
Arrays - Implementation Examples
Các techniques và patterns quan trọng với arrays
"""

from typing import List, Tuple, Optional


# ============================================================
# 1. TWO POINTERS TECHNIQUE
# ============================================================

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Two Sum trên sorted array - Two Pointers
    
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger value
        else:
            right -= 1  # Need smaller value
    
    return []


def remove_duplicates_sorted(arr: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place
    Returns new length
    
    Time: O(n)
    Space: O(1)
    
    Example: [1,1,2,2,3] → [1,2,3,_,_], return 3
    """
    if not arr:
        return 0
    
    write_idx = 1  # Position để ghi unique element
    
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[read_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    
    return write_idx


def reverse_array(arr: List[int]) -> List[int]:
    """
    Reverse array in-place using two pointers
    
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome - Two Pointers
    
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def move_zeros(arr: List[int]) -> List[int]:
    """
    Move all zeros to end, maintain order of non-zeros
    
    Time: O(n)
    Space: O(1)
    
    Example: [0,1,0,3,12] → [1,3,12,0,0]
    """
    write_idx = 0  # Position cho next non-zero
    
    # Move all non-zeros to front
    for read_idx in range(len(arr)):
        if arr[read_idx] != 0:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    
    # Fill remaining with zeros
    for i in range(write_idx, len(arr)):
        arr[i] = 0
    
    return arr


# ============================================================
# 2. SLIDING WINDOW
# ============================================================

def max_sum_subarray_fixed(arr: List[int], k: int) -> int:
    """
    Maximum sum of any subarray of size k
    
    Time: O(n) - Single pass with sliding window
    Space: O(1)
    """
    if len(arr) < k:
        return 0
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window: add new element, remove leftmost
    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Longest substring with at most k distinct characters
    
    Time: O(n)
    Space: O(k) - Hash map for distinct chars
    """
    if k == 0:
        return 0
    
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window if needed
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


def min_subarray_sum(arr: List[int], target: int) -> int:
    """
    Minimum length subarray with sum >= target
    
    Time: O(n)
    Space: O(1)
    
    Return 0 if không tồn tại
    """
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        # Shrink window while sum >= target
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0


# ============================================================
# 3. PREFIX SUM
# ============================================================

class PrefixSum:
    """
    Prefix Sum for efficient range sum queries
    
    Build: O(n)
    Query: O(1)
    Space: O(n)
    """
    
    def __init__(self, arr: List[int]):
        self.prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            self.prefix[i + 1] = self.prefix[i] + arr[i]
    
    def range_sum(self, left: int, right: int) -> int:
        """Sum from arr[left] to arr[right] inclusive"""
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum_equals_k(arr: List[int], k: int) -> int:
    """
    Count number of subarrays with sum = k
    
    Time: O(n)
    Space: O(n)
    
    Uses prefix sum + hash table
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum: frequency
    
    for num in arr:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        # If yes, found subarray with sum = k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


# ============================================================
# 4. KADANE'S ALGORITHM
# ============================================================

def max_subarray_sum(arr: List[int]) -> int:
    """
    Maximum sum of contiguous subarray (Kadane's Algorithm)
    
    Time: O(n)
    Space: O(1)
    """
    if not arr:
        return 0
    
    max_ending_here = max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend current subarray or start new one
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def max_subarray_with_indices(arr: List[int]) -> Tuple[int, int, int]:
    """
    Return (max_sum, start_index, end_index)
    
    Time: O(n)
    Space: O(1)
    """
    max_sum = arr[0]
    max_ending_here = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here = max_ending_here + arr[i]
        
        if max_ending_here > max_sum:
            max_sum = max_ending_here
            start = temp_start
            end = i
    
    return max_sum, start, end


# ============================================================
# 5. DUTCH NATIONAL FLAG (3-Way Partitioning)
# ============================================================

def sort_colors(arr: List[int]) -> List[int]:
    """
    Sort array containing only 0s, 1s, 2s in-place
    
    Time: O(n)
    Space: O(1)
    
    Example: [2,0,2,1,1,0] → [0,0,1,1,2,2]
    """
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


# ============================================================
# 6. ARRAY ROTATION
# ============================================================

def rotate_left(arr: List[int], k: int) -> List[int]:
    """
    Rotate array left by k positions
    
    Time: O(n)
    Space: O(1) if in-place, O(n) if create new
    
    Example: [1,2,3,4,5], k=2 → [3,4,5,1,2]
    """
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Using reversal algorithm
    # 1. Reverse first k elements
    reverse_range(arr, 0, k - 1)
    # 2. Reverse remaining elements
    reverse_range(arr, k, n - 1)
    # 3. Reverse entire array
    reverse_range(arr, 0, n - 1)
    
    return arr


def reverse_range(arr: List[int], start: int, end: int):
    """Helper: reverse arr[start:end+1] in-place"""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# ============================================================
# 7. BINARY SEARCH ON ARRAY
# ============================================================

def binary_search(arr: List[int], target: int) -> int:
    """
    Binary search on sorted array
    
    Time: O(log n)
    Space: O(1)
    
    Returns index if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find first occurrence of target in sorted array (can have duplicates)
    
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def search_rotated_array(arr: List[int], target: int) -> int:
    """
    Search in rotated sorted array
    
    Time: O(log n)
    Space: O(1)
    
    Example: [4,5,6,7,0,1,2], target=0 → 4
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[left] <= arr[mid]:  # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


# ============================================================
# 8. COMMON TRICKS & OPTIMIZATIONS
# ============================================================

def two_sum_hash(arr: List[int], target: int) -> List[int]:
    """
    Two Sum using hash table (works on unsorted array)
    
    Time: O(n)
    Space: O(n)
    """
    seen = {}  # value: index
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


def find_duplicates(arr: List[int]) -> List[int]:
    """
    Find all duplicates in array where elements are in range [1, n]
    
    Time: O(n)
    Space: O(1) - Using input array as hash
    
    Trick: Negate arr[num] to mark as seen
    """
    result = []
    
    for num in arr:
        index = abs(num) - 1
        if arr[index] < 0:
            result.append(abs(num))  # Seen before
        else:
            arr[index] = -arr[index]  # Mark as seen
    
    # Restore array
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    
    return result


def single_number(arr: List[int]) -> int:
    """
    Find element that appears once (all others appear twice)
    
    Time: O(n)
    Space: O(1)
    
    Trick: XOR all elements, pairs cancel out
    """
    result = 0
    for num in arr:
        result ^= num
    return result


def product_except_self(arr: List[int]) -> List[int]:
    """
    Product of all elements except self, WITHOUT division
    
    Time: O(n)
    Space: O(1) excluding output array
    
    Example: [1,2,3,4] → [24,12,8,6]
    """
    n = len(arr)
    result = [1] * n
    
    # Left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= arr[i]
    
    # Right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
    
    return result


# ============================================================
# 9. MATRIX (2D ARRAY)
# ============================================================

def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Return all elements in spiral order
    
    Time: O(m × n)
    Space: O(1) excluding output
    """
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            # Traverse left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        if left <= right:
            # Traverse up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result


# ============================================================
# DEMO
# ============================================================

if __name__ == "__main__":
    print("="*60)
    print("ARRAY TECHNIQUES - EXAMPLES")
    print("="*60)
    
    # Two Pointers
    print("\n1. TWO POINTERS")
    arr = [1, 2, 3, 4, 6]
    print(f"Two Sum Sorted: arr={arr}, target=6")
    print(f"Result: {two_sum_sorted(arr, 6)}")
    
    # Sliding Window
    print("\n2. SLIDING WINDOW")
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Max Sum Subarray: arr={arr}, k={k}")
    print(f"Result: {max_sum_subarray_fixed(arr, k)}")
    
    # Kadane's
    print("\n3. KADANE'S ALGORITHM")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max Subarray Sum: arr={arr}")
    print(f"Result: {max_subarray_sum(arr)}")
    
    # Dutch Flag
    print("\n4. DUTCH NATIONAL FLAG")
    arr = [2, 0, 2, 1, 1, 0]
    print(f"Sort Colors: before={arr}")
    sort_colors(arr)
    print(f"After: {arr}")
    
    print("\n" + "="*60)
