"""
Complexity Analysis - Code Examples
Các ví dụ minh họa cho từng độ phức tạp với giải thích chi tiết
"""

import time
from typing import List, Dict
from functools import wraps


def timing_decorator(func):
    """Decorator để đo thời gian chạy của function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper


# ============================================================
# O(1) - CONSTANT TIME
# ============================================================

def example_o1_array_access(arr: List[int], index: int) -> int:
    """
    O(1) - Truy cập phần tử array bằng index
    
    Time: O(1) - Direct memory access
    Space: O(1) - Không dùng extra memory
    """
    return arr[index]


def example_o1_hash_lookup(hash_map: Dict, key: str):
    """
    O(1) - Lookup trong hash table
    
    Time: O(1) average case - Hash function + direct access
    Space: O(1) - Không dùng extra memory
    """
    return hash_map.get(key)


def example_o1_arithmetic():
    """
    O(1) - Các phép toán cơ bản
    
    Dù có bao nhiêu operations, nếu là constant thì vẫn O(1)
    """
    x = 5
    y = 10
    sum_val = x + y          # O(1)
    product = x * y          # O(1)
    result = sum_val / product  # O(1)
    
    # 100 operations vẫn là O(1)!
    for _ in range(100):     # Fixed 100, không phụ thuộc input
        result += 1
    
    return result
    # Time: O(1)
    # Space: O(1)


# ============================================================
# O(log n) - LOGARITHMIC TIME
# ============================================================

def example_ologn_binary_search(arr: List[int], target: int) -> int:
    """
    O(log n) - Binary Search
    
    Mỗi iteration giảm search space đi một nửa
    → log₂(n) iterations
    
    Time: O(log n)
    Space: O(1) - Iterative version
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1    # Bỏ nửa trái
        else:
            right = mid - 1   # Bỏ nửa phải
    
    return -1


def example_ologn_binary_search_recursive(arr: List[int], target: int, 
                                          left: int = 0, right: int = None) -> int:
    """
    O(log n) - Binary Search (Recursive)
    
    Time: O(log n)
    Space: O(log n) - Recursion call stack depth
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return example_ologn_binary_search_recursive(arr, target, mid + 1, right)
    else:
        return example_ologn_binary_search_recursive(arr, target, left, mid - 1)


def example_ologn_find_power(base: int, exponent: int) -> int:
    """
    O(log n) - Fast exponentiation
    
    Tính base^exponent bằng cách chia đôi exponent
    → log₂(exponent) iterations
    
    Time: O(log n) where n = exponent
    Space: O(1)
    """
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2  # Giảm exponent đi một nửa
    
    return result


# ============================================================
# O(n) - LINEAR TIME
# ============================================================

def example_on_linear_search(arr: List[int], target: int) -> int:
    """
    O(n) - Linear Search
    
    Worst case: phải duyệt hết n elements
    
    Time: O(n)
    Space: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def example_on_sum_array(arr: List[int]) -> int:
    """
    O(n) - Tính tổng array
    
    Time: O(n) - Duyệt qua n elements một lần
    Space: O(1) - Chỉ dùng 1 variable
    """
    total = 0
    for num in arr:
        total += num
    return total


def example_on_multiple_passes(arr: List[int]) -> tuple:
    """
    O(n) - Multiple passes vẫn là O(n)
    
    O(n) + O(n) + O(n) = O(3n) = O(n)
    
    Time: O(n)
    Space: O(1)
    """
    # Pass 1: Sum
    total = sum(arr)                    # O(n)
    
    # Pass 2: Count evens
    evens = sum(1 for x in arr if x % 2 == 0)  # O(n)
    
    # Pass 3: Find max
    max_val = max(arr)                  # O(n)
    
    return total, evens, max_val


def example_on_reverse_array(arr: List[int]) -> List[int]:
    """
    O(n) - Reverse array in-place
    
    Time: O(n) - Duyệt n/2 elements
    Space: O(1) - In-place swap
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


# ============================================================
# O(n log n) - LINEARITHMIC TIME
# ============================================================

def example_onlogn_merge_sort(arr: List[int]) -> List[int]:
    """
    O(n log n) - Merge Sort
    
    - log n levels (chia đôi array mỗi level)
    - Mỗi level merge n elements
    → n * log n operations
    
    Time: O(n log n)
    Space: O(n) - Temporary arrays cho merging
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = example_onlogn_merge_sort(arr[:mid])    # T(n/2)
    right = example_onlogn_merge_sort(arr[mid:])   # T(n/2)
    
    # Conquer (Merge)
    return merge(left, right)  # O(n)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function cho merge sort - O(n)"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def example_onlogn_efficient_duplicate_check(arr: List[int]) -> bool:
    """
    O(n log n) - Check duplicates bằng sorting
    
    Alternative: O(n) với hash set, nhưng O(n) space
    
    Time: O(n log n) - Sort dominates
    Space: O(1) if sort in-place, O(n) if create new array
    """
    sorted_arr = sorted(arr)  # O(n log n)
    
    # Check adjacent elements
    for i in range(len(sorted_arr) - 1):  # O(n)
        if sorted_arr[i] == sorted_arr[i + 1]:
            return True
    
    return False


# ============================================================
# O(n²) - QUADRATIC TIME
# ============================================================

def example_on2_bubble_sort(arr: List[int]) -> List[int]:
    """
    O(n²) - Bubble Sort
    
    Nested loops: outer loop n times, inner loop n times
    
    Time: O(n²)
    Space: O(1) - In-place sorting
    """
    n = len(arr)
    
    for i in range(n):              # O(n)
        for j in range(n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def example_on2_find_all_pairs(arr: List[int]) -> List[tuple]:
    """
    O(n²) - Tìm tất cả các cặp trong array
    
    Time: O(n²) - Nested loops
    Space: O(n²) - Worst case n(n-1)/2 pairs
    """
    pairs = []
    
    for i in range(len(arr)):           # O(n)
        for j in range(i + 1, len(arr)):  # O(n)
            pairs.append((arr[i], arr[j]))
    
    return pairs


def example_on2_two_sum_brute_force(arr: List[int], target: int) -> List[int]:
    """
    O(n²) - Two Sum brute force
    
    Time: O(n²)
    Space: O(1)
    
    Note: Có thể optimize xuống O(n) với hash table!
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return []


# ============================================================
# O(2ⁿ) - EXPONENTIAL TIME
# ============================================================

def example_o2n_fibonacci_recursive(n: int) -> int:
    """
    O(2ⁿ) - Fibonacci naive recursion
    
    Mỗi call tạo ra 2 recursive calls
    → Tree with 2ⁿ nodes
    
    Time: O(2ⁿ) - Exponential!
    Space: O(n) - Call stack depth
    
    Note: Cực kỳ chậm! fib(40) mất vài giây.
    """
    if n <= 1:
        return n
    
    return example_o2n_fibonacci_recursive(n - 1) + \
           example_o2n_fibonacci_recursive(n - 2)


def example_o2n_generate_all_subsets(arr: List[int]) -> List[List[int]]:
    """
    O(2ⁿ) - Generate tất cả subsets
    
    Mỗi element có 2 choices: include hoặc exclude
    → 2ⁿ subsets
    
    Time: O(2ⁿ)
    Space: O(2ⁿ) - Store all subsets
    """
    result = []
    
    def backtrack(index: int, current: List[int]):
        if index == len(arr):
            result.append(current[:])
            return
        
        # Exclude current element
        backtrack(index + 1, current)
        
        # Include current element
        current.append(arr[index])
        backtrack(index + 1, current)
        current.pop()
    
    backtrack(0, [])
    return result


# ============================================================
# OPTIMIZED VERSIONS - So sánh Before/After
# ============================================================

def two_sum_optimized(arr: List[int], target: int) -> List[int]:
    """
    O(n) - Two Sum với hash table
    
    Optimize từ O(n²) brute force xuống O(n)
    
    Time: O(n)
    Space: O(n) - Hash table
    """
    seen = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


def fibonacci_optimized(n: int, memo: Dict[int, int] = None) -> int:
    """
    O(n) - Fibonacci với memoization
    
    Optimize từ O(2ⁿ) xuống O(n)
    
    Time: O(n) - Mỗi value chỉ tính 1 lần
    Space: O(n) - Memo dictionary + call stack
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_optimized(n - 1, memo) + fibonacci_optimized(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n: int) -> int:
    """
    O(n) - Fibonacci iterative (best space complexity)
    
    Time: O(n)
    Space: O(1) - Chỉ dùng 2 variables
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


# ============================================================
# COMPARISON DEMO
# ============================================================

@timing_decorator
def demo_comparison():
    """
    Demo để thấy sự khác biệt giữa các complexities
    """
    print("\n" + "="*60)
    print("COMPLEXITY COMPARISON DEMO")
    print("="*60)
    
    # Test với array size tăng dần
    sizes = [10, 100, 1000, 10000]
    
    for n in sizes:
        arr = list(range(n))
        target = n - 1  # Worst case: element cuối
        
        print(f"\n--- Array size: {n} ---")
        
        # O(1) - Instant
        result = example_o1_array_access(arr, 0)
        print(f"O(1) access: index 0 = {result}")
        
        # O(log n) - Very fast
        start = time.perf_counter()
        result = example_ologn_binary_search(arr, target)
        end = time.perf_counter()
        print(f"O(log n) binary search: {(end - start)*1000:.3f}ms")
        
        # O(n) - Linear growth
        start = time.perf_counter()
        result = example_on_linear_search(arr, target)
        end = time.perf_counter()
        print(f"O(n) linear search: {(end - start)*1000:.3f}ms")
        
        # O(n²) - Slow for large n
        if n <= 1000:  # Skip for n=10000, too slow!
            start = time.perf_counter()
            result = example_on2_find_all_pairs(arr[:min(n, 100)])
            end = time.perf_counter()
            print(f"O(n²) find pairs (n=100): {(end - start)*1000:.3f}ms")


def demo_fibonacci_comparison():
    """
    So sánh 3 cách implement Fibonacci
    """
    print("\n" + "="*60)
    print("FIBONACCI IMPLEMENTATIONS COMPARISON")
    print("="*60)
    
    test_values = [10, 20, 30, 35]
    
    for n in test_values:
        print(f"\n--- Computing fib({n}) ---")
        
        # O(2ⁿ) - Exponential
        if n <= 35:  # Quá chậm với n > 35
            start = time.perf_counter()
            result = example_o2n_fibonacci_recursive(n)
            end = time.perf_counter()
            print(f"O(2ⁿ) recursive: {result}, time: {(end - start)*1000:.3f}ms")
        
        # O(n) with memoization
        start = time.perf_counter()
        result = fibonacci_optimized(n)
        end = time.perf_counter()
        print(f"O(n) memoization: {result}, time: {(end - start)*1000:.3f}ms")
        
        # O(n) iterative
        start = time.perf_counter()
        result = fibonacci_iterative(n)
        end = time.perf_counter()
        print(f"O(n) iterative: {result}, time: {(end - start)*1000:.3f}ms")


# ============================================================
# MAIN - RUN EXAMPLES
# ============================================================

if __name__ == "__main__":
    print("="*60)
    print("COMPLEXITY ANALYSIS - CODE EXAMPLES")
    print("="*60)
    
    # Run comparison demos
    demo_comparison()
    demo_fibonacci_comparison()
    
    print("\n" + "="*60)
    print("KEY TAKEAWAYS:")
    print("="*60)
    print("1. O(1) và O(log n) cực kỳ nhanh, ngay cả với large input")
    print("2. O(n) acceptable cho hầu hết problems")
    print("3. O(n log n) là best có thể cho comparison-based sorting")
    print("4. O(n²) chỉ OK với small input (n < 1000)")
    print("5. O(2ⁿ) không practical cho n > 30, cần optimize!")
    print("="*60)
