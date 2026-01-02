# 📝 Stack & Queue - Practice Problems

Tổng hợp 20 bài tập từ Easy → Hard với hints và solutions đầy đủ.

---

## 🟢 EASY LEVEL (1-8)

### Problem 1: Valid Parentheses ⭐⭐⭐

**Độ khó**: Easy  
**Pattern**: Stack Matching

**Đề bài**:
Cho một string chứa các ký tự '(', ')', '{', '}', '[', ']'. Kiểm tra xem string có hợp lệ không.

**Input/Output**:

```
Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

**Constraints**:

- 1 <= s.length <= 10^4
- s chỉ chứa '(){}[]'

<details>
<summary><b>💡 Hints</b></summary>

1. Sử dụng stack để track opening brackets
2. Khi gặp closing bracket, check xem nó match với top of stack không
3. Cuối cùng stack phải empty

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def is_valid_parentheses(s):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Test
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([)]"))    # False
```

**Complexity**:

- Time: O(n) - traverse string once
- Space: O(n) - worst case all opening brackets

</details>

---

### Problem 2: Implement Queue using Stacks ⭐⭐

**Độ khó**: Easy  
**Pattern**: Stack to Queue conversion

**Đề bài**:
Implement queue sử dụng hai stacks.

**Operations**:

- `push(x)`: Add element to rear
- `pop()`: Remove element from front
- `peek()`: Get front element
- `empty()`: Check if empty

<details>
<summary><b>💡 Hints</b></summary>

1. Dùng 2 stacks: stack1 cho input, stack2 cho output
2. Khi pop/peek, nếu stack2 empty thì move tất cả từ stack1
3. Amortized O(1) for all operations

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
class MyQueue:
    def __init__(self):
        self.stack1 = []  # For push
        self.stack2 = []  # For pop/peek

    def push(self, x):
        """O(1)"""
        self.stack1.append(x)

    def pop(self):
        """Amortized O(1)"""
        self._move()
        return self.stack2.pop()

    def peek(self):
        """Amortized O(1)"""
        self._move()
        return self.stack2[-1]

    def empty(self):
        """O(1)"""
        return not self.stack1 and not self.stack2

    def _move(self):
        """Move elements from stack1 to stack2 if needed"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

# Test
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # 1
print(q.pop())   # 1
print(q.empty()) # False
```

**Complexity**:

- Push: O(1)
- Pop/Peek: Amortized O(1)
- Space: O(n)

</details>

---

### Problem 3: Implement Stack using Queues ⭐⭐

**Độ khó**: Easy  
**Pattern**: Queue to Stack conversion

**Đề bài**:
Implement stack sử dụng queues.

<details>
<summary><b>💡 Hints</b></summary>

1. Method 1: Dùng 1 queue, khi push, rotate tất cả elements
2. Method 2: Dùng 2 queues, swap sau mỗi push

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """O(n) - rotate to maintain stack order"""
        self.queue.append(x)
        # Rotate all previous elements after new element
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """O(1)"""
        return self.queue.popleft()

    def top(self):
        """O(1)"""
        return self.queue[0]

    def empty(self):
        """O(1)"""
        return len(self.queue) == 0

# Test
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())   # 2
print(stack.pop())   # 2
print(stack.empty()) # False
```

**Complexity**:

- Push: O(n)
- Pop/Top: O(1)
- Space: O(n)

</details>

---

### Problem 4: Min Stack ⭐⭐⭐

**Độ khó**: Easy  
**Pattern**: Auxiliary Stack

**Đề bài**:
Design stack hỗ trợ push, pop, top, và getMin trong O(1).

**Operations**:

```python
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.get_min()  # -3
stack.pop()
stack.top()      # 0
stack.get_min()  # -2
```

<details>
<summary><b>💡 Hints</b></summary>

1. Dùng thêm 1 stack để track minimums
2. Mỗi khi push, cũng push min(val, current_min) vào min_stack
3. Pop cả 2 stacks cùng lúc

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """O(1)"""
        self.stack.append(val)
        # Push min of (val, previous min)
        min_val = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(min_val)

    def pop(self):
        """O(1)"""
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """O(1)"""
        return self.stack[-1]

    def get_min(self):
        """O(1)"""
        return self.min_stack[-1]
```

**Complexity**:

- All operations: O(1)
- Space: O(n) for min_stack

</details>

---

### Problem 5: Evaluate Reverse Polish Notation ⭐⭐

**Độ khó**: Easy  
**Pattern**: Stack Calculation

**Đề bài**:
Evaluate postfix expression (Reverse Polish Notation).

**Input/Output**:

```
Input: ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

<details>
<summary><b>✅ Solution</b></summary>

```python
def eval_rpn(tokens):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # '/'
                # Truncate toward zero
                stack.append(int(a / b))

    return stack[0]
```

</details>

---

### Problem 6: Number of Recent Calls ⭐

**Độ khó**: Easy  
**Pattern**: Queue with Time Window

**Đề bài**:
Design class đếm số requests trong 3000ms window.

```python
counter = RecentCounter()
counter.ping(1)     # 1
counter.ping(100)   # 2
counter.ping(3001)  # 3
counter.ping(3002)  # 3
```

<details>
<summary><b>✅ Solution</b></summary>

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        """
        Time: O(1) amortized
        Space: O(n) where n is max requests in 3000ms
        """
        self.requests.append(t)

        # Remove requests older than 3000ms
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)
```

</details>

---

### Problem 7: Baseball Game ⭐

**Độ khó**: Easy  
**Pattern**: Stack Simulation

**Đề bài**:
Calculate baseball game score với special operations.

**Operations**:

- Integer x: Add x points
- "+": Add sum of previous 2 scores
- "D": Add double of previous score
- "C": Remove previous score

**Example**:

```
Input: ["5","2","C","D","+"]
Output: 30
Explanation:
5 → [5]
2 → [5, 2]
C → [5]
D → [5, 10]
+ → [5, 10, 15]
Sum = 30
```

<details>
<summary><b>✅ Solution</b></summary>

```python
def cal_points(ops):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []

    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)
```

</details>

---

### Problem 8: Remove All Adjacent Duplicates ⭐

**Độ khó**: Easy  
**Pattern**: Stack for Adjacent Removal

**Đề bài**:
Remove adjacent duplicate characters.

```
Input: "abbaca"
Output: "ca"
Explanation: "bb" removed → "aaca" → "aa" removed → "ca"
```

<details>
<summary><b>✅ Solution</b></summary>

```python
def remove_duplicates(s):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)
```

</details>

---

## 🟡 MEDIUM LEVEL (9-15)

### Problem 9: Daily Temperatures ⭐⭐⭐

**Độ khó**: Medium  
**Pattern**: Monotonic Stack

**Đề bài**:
Tìm số ngày phải đợi để có nhiệt độ cao hơn.

```
Input: [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

<details>
<summary><b>💡 Hints</b></summary>

1. Dùng monotonic stack để track indices
2. Khi gặp temperature cao hơn, pop và update result
3. Traverse left to right

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def daily_temperatures(temperatures):
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Store indices

    for i in range(n):
        # Pop cooler days and update
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        stack.append(i)

    return result
```

**Complexity**:

- Time: O(n) - each element pushed/popped once
- Space: O(n) - stack size

</details>

---

### Problem 10: Next Greater Element II ⭐⭐⭐

**Độ khó**: Medium  
**Pattern**: Monotonic Stack + Circular

**Đề bài**:
Find next greater element trong circular array.

```
Input: [1,2,1]
Output: [2,-1,2]
Explanation: Circular → [1,2,1,1,2,1]
```

<details>
<summary><b>💡 Hints</b></summary>

1. Traverse array 2 lần để handle circular
2. Dùng modulo (%) cho index
3. Monotonic decreasing stack

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def next_greater_elements(nums):
    """
    Time: O(n)
    Space: O(n)
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    # Traverse twice for circular
    for i in range(2 * n):
        idx = i % n

        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]

        if i < n:  # Only push in first round
            stack.append(idx)

    return result
```

</details>

---

### Problem 11: Largest Rectangle in Histogram ⭐⭐⭐

**Độ khó**: Hard  
**Pattern**: Monotonic Stack

**Đề bài**:
Find largest rectangle area in histogram.

```
Input: heights = [2,1,5,6,2,3]
Output: 10
```

<details>
<summary><b>💡 Hints</b></summary>

1. Monotonic increasing stack
2. Khi gặp smaller height, pop và calculate area
3. Width = current_index - stack[-1] - 1

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def largest_rectangle_area(heights):
    """
    Time: O(n)
    Space: O(n)
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

    # Process remaining
    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area
```

</details>

---

### Problem 12: Sliding Window Maximum ⭐⭐⭐

**Độ khó**: Hard  
**Pattern**: Deque

**Đề bài**:
Find maximum trong mỗi sliding window size k.

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

<details>
<summary><b>💡 Hints</b></summary>

1. Dùng deque để maintain decreasing order
2. Store indices, not values
3. Remove indices outside window
4. Front of deque is always maximum

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
from collections import deque

def max_sliding_window(nums, k):
    """
    Time: O(n)
    Space: O(k)
    """
    dq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result after first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

</details>

---

### Problem 13: Binary Tree Level Order Traversal ⭐⭐

**Độ khó**: Medium  
**Pattern**: BFS with Queue

**Đề bài**:
Return level-order traversal of binary tree.

```
Input:
    3
   / \
  9  20
    /  \
   15   7

Output: [[3],[9,20],[15,7]]
```

<details>
<summary><b>✅ Solution</b></summary>

```python
from collections import deque

def level_order(root):
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

</details>

---

### Problem 14: Decode String ⭐⭐⭐

**Độ khó**: Medium  
**Pattern**: Stack for Nested Operations

**Đề bài**:
Decode encoded string với format k[encoded_string].

```
Input: "3[a]2[bc]"
Output: "aaabcbc"

Input: "3[a2[c]]"
Output: "accaccacc"
```

<details>
<summary><b>💡 Hints</b></summary>

1. Stack lưu (count, string_so_far)
2. Khi gặp '[', push current state
3. Khi gặp ']', pop và repeat

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def decode_string(s):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push state
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop and decode
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string
```

</details>

---

### Problem 15: Asteroid Collision ⭐⭐

**Độ khó**: Medium  
**Pattern**: Stack Simulation

**Đề bài**:
Simulate asteroid collisions.

- Positive = moving right
- Negative = moving left
- Absolute value = size

```
Input: [5,10,-5]
Output: [5,10]
Explanation: 10 và -5 collide → 10 wins

Input: [8,-8]
Output: []
Explanation: Equal size → both destroyed
```

<details>
<summary><b>✅ Solution</b></summary>

```python
def asteroid_collision(asteroids):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)

    return stack
```

</details>

---

## 🔴 HARD LEVEL (16-20)

### Problem 16: Maximal Rectangle ⭐⭐⭐

**Độ khó**: Hard  
**Pattern**: Largest Rectangle in Histogram

**Đề bài**:
Find largest rectangle containing only 1's in binary matrix.

```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

<details>
<summary><b>💡 Hints</b></summary>

1. Convert mỗi row thành histogram
2. Apply largest rectangle in histogram cho mỗi row
3. Track heights

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def maximal_rectangle(matrix):
    """
    Time: O(m * n)
    Space: O(n)
    """
    if not matrix:
        return 0

    n = len(matrix[0])
    heights = [0] * n
    max_area = 0

    for row in matrix:
        # Update heights
        for i in range(n):
            if row[i] == '1':
                heights[i] += 1
            else:
                heights[i] = 0

        # Calculate max rectangle for this histogram
        max_area = max(max_area, largest_rectangle_area(heights))

    return max_area

def largest_rectangle_area(heights):
    """Helper from Problem 11"""
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
```

</details>

---

### Problem 17: Trapping Rain Water ⭐⭐⭐

**Độ khó**: Hard  
**Pattern**: Monotonic Stack

**Đề bài**:
Calculate how much rain water can be trapped.

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

<details>
<summary><b>💡 Hints</b></summary>

1. Monotonic decreasing stack
2. Khi gặp higher bar, calculate trapped water
3. Water = (min(left, right) - current) \* width

</details>

<details>
<summary><b>✅ Solution</b></summary>

```python
def trap(height):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    water = 0

    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom_idx = stack.pop()

            if not stack:
                break

            left_idx = stack[-1]
            width = i - left_idx - 1
            bounded_height = min(height[left_idx], h) - height[bottom_idx]
            water += width * bounded_height

        stack.append(i)

    return water
```

</details>

---

### Problem 18: Basic Calculator ⭐⭐⭐

**Độ khó**: Hard  
**Pattern**: Stack with Nested Operations

**Đề bài**:
Implement basic calculator supporting +, -, (, ).

```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

<details>
<summary><b>✅ Solution</b></summary>

```python
def calculate(s):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    result = 0
    sign = 1
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            sign = 1
            num = 0
        elif char == '-':
            result += sign * num
            sign = -1
            num = 0
        elif char == '(':
            # Push result and sign
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            result *= stack.pop()  # Sign before '('
            result += stack.pop()  # Result before '('
            num = 0

    return result + sign * num
```

</details>

---

### Problem 19: LRU Cache ⭐⭐⭐

**Độ khó**: Medium  
**Pattern**: Queue + HashMap

**Đề bài**:
Implement LRU (Least Recently Used) cache.

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # 1
cache.put(3, 3)    # Evicts key 2
cache.get(2)       # -1 (not found)
```

<details>
<summary><b>✅ Solution</b></summary>

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """O(1)"""
        if key not in self.cache:
            return -1
        # Move to end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """O(1)"""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # Remove least recent (first item)
            self.cache.popitem(last=False)
```

</details>

---

### Problem 20: Serialize and Deserialize Binary Tree ⭐⭐⭐

**Độ khó**: Hard  
**Pattern**: BFS with Queue

**Đề bài**:
Serialize binary tree to string và deserialize back.

<details>
<summary><b>✅ Solution</b></summary>

```python
from collections import deque

class Codec:
    def serialize(self, root):
        """
        Encode tree to string using BFS
        Time: O(n), Space: O(n)
        """
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data):
        """
        Decode string to tree
        Time: O(n), Space: O(n)
        """
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
```

</details>

---

## 📊 Summary

### Patterns đã học:

1. ✅ **Stack Matching** - Parentheses, brackets
2. ✅ **Monotonic Stack** - Next greater/smaller element
3. ✅ **Stack Calculation** - Expression evaluation
4. ✅ **BFS with Queue** - Level-order traversal
5. ✅ **Sliding Window with Deque** - Window maximum/minimum
6. ✅ **Nested Operations** - Decode string, calculator

### Complexity:

- Most problems: **O(n) time, O(n) space**
- Key: Each element pushed/popped **at most once**

### Tips:

1. Stack for **nested/matching** problems
2. Queue for **BFS/level-order**
3. Deque for **sliding window**
4. Monotonic stack for **next greater/smaller**

**Keep practicing! 🚀**
