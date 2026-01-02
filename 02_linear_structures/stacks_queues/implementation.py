"""
Stack và Queue Implementations
Tất cả operations O(1)
"""

from collections import deque


# ============================================================================
# STACK IMPLEMENTATIONS
# ============================================================================

class Stack:
    """
    Stack using Python list
    All operations: O(1)
    """
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"


class Node:
    """Node for Linked List based Stack"""
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    """
    Stack using Linked List
    Better for very large stacks (no resizing overhead)
    """
    
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
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
    
    def peek(self):
        """Return top item - O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size


# ============================================================================
# QUEUE IMPLEMENTATIONS
# ============================================================================

class Queue:
    """
    Queue using collections.deque (RECOMMENDED)
    All operations: O(1)
    """
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to rear - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item - O(1)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()
    
    def front(self):
        """View front item - O(1)"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return size - O(1)"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({list(self.items)})"


class CircularQueue:
    """
    Circular Queue with fixed capacity
    Efficient for bounded size queues
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item):
        """Add item to rear - O(1)"""
        if self.is_full():
            raise OverflowError("queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def front_item(self):
        """View front - O(1)"""
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.items[self.front]
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity


# ============================================================================
# STACK APPLICATIONS
# ============================================================================

def is_balanced_parentheses(expression):
    """
    Check if parentheses are balanced
    
    Example:
        "({[]})" → True
        "({[}])" → False
    
    Time: O(n)
    Space: O(n)
    """
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in expression:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0


def evaluate_postfix(expression):
    """
    Evaluate postfix (RPN) expression
    
    Example:
        "2 3 1 * + 9 -" → ((2 + (3 * 1)) - 9) = -4
    
    Time: O(n)
    Space: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = int(a / b)  # Integer division
            
            stack.append(result)
    
    return stack[0]


def next_greater_element(arr):
    """
    Find next greater element for each element
    Uses stack to maintain potential candidates
    
    Example:
        [4, 5, 2, 10, 8]
        [5, 10, 10, -1, -1]
    
    Time: O(n)
    Space: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Store indices
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Pop smaller elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # Top element is next greater (if exists)
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result


def largest_rectangle_histogram(heights):
    """
    Find largest rectangle in histogram
    Uses monotonic increasing stack
    
    Example:
        heights = [2, 1, 5, 6, 2, 3]
        Output: 10 (rectangle with height 5-6)
    
    Time: O(n)
    Space: O(n)
    """
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        # Maintain increasing stack
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


def daily_temperatures(temperatures):
    """
    Find days until warmer temperature
    
    Example:
        [73, 74, 75, 71, 69, 72, 76, 73]
        [1, 1, 4, 2, 1, 1, 0, 0]
    
    Time: O(n)
    Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Store indices
    
    for i in range(n):
        # Pop cooler days and update their result
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        
        stack.append(i)
    
    return result


def min_stack_design():
    """
    Design a stack that supports push, pop, top, and getMin in O(1)
    """
    
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []  # Track minimums
        
        def push(self, val):
            self.stack.append(val)
            # Push min of (current val, previous min)
            min_val = val if not self.min_stack else min(val, self.min_stack[-1])
            self.min_stack.append(min_val)
        
        def pop(self):
            self.stack.pop()
            self.min_stack.pop()
        
        def top(self):
            return self.stack[-1]
        
        def get_min(self):
            return self.min_stack[-1]
    
    return MinStack


# ============================================================================
# QUEUE APPLICATIONS
# ============================================================================

def bfs_graph(graph, start):
    """
    Breadth-First Search using queue
    
    Args:
        graph: dict mapping node -> list of neighbors
        start: starting node
    
    Returns:
        List of nodes in BFS order
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def level_order_traversal(root):
    """
    Level-order traversal of binary tree
    
    Returns: List of lists (each level)
    
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


def sliding_window_maximum(arr, k):
    """
    Find maximum in each sliding window of size k
    Uses deque to maintain decreasing order
    
    Example:
        arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        Output: [3, 3, 5, 5, 6, 7]
    
    Time: O(n)
    Space: O(k)
    """
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(arr)):
        # Remove indices outside current window
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (maintain decreasing order)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add max to result after first complete window
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result


def recent_counter():
    """
    Design a class to count recent requests within 3000ms time window
    """
    
    class RecentCounter:
        def __init__(self):
            self.requests = deque()
        
        def ping(self, t):
            """
            Add new request at time t
            Return count of requests in [t-3000, t]
            """
            self.requests.append(t)
            
            # Remove requests older than 3000ms
            while self.requests and self.requests[0] < t - 3000:
                self.requests.popleft()
            
            return len(self.requests)
    
    return RecentCounter


def generate_binary_numbers(n):
    """
    Generate binary numbers from 1 to n using queue
    
    Example: n = 5
    Output: ['1', '10', '11', '100', '101']
    
    Time: O(n)
    Space: O(n)
    """
    result = []
    queue = deque(['1'])
    
    for _ in range(n):
        binary = queue.popleft()
        result.append(binary)
        
        # Generate next numbers by appending 0 and 1
        queue.append(binary + '0')
        queue.append(binary + '1')
    
    return result


# ============================================================================
# DEQUE APPLICATIONS
# ============================================================================

def palindrome_checker(s):
    """
    Check if string is palindrome using deque
    
    Time: O(n)
    Space: O(n)
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    dq = deque(s)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True


# ============================================================================
# DEMO & TESTING
# ============================================================================

def demo_stack():
    """Demo Stack operations"""
    print("=== STACK DEMO ===")
    stack = Stack()
    
    # Push elements
    for i in [1, 2, 3, 4]:
        stack.push(i)
        print(f"Push {i}: {stack}")
    
    # Pop elements
    while not stack.is_empty():
        print(f"Pop: {stack.pop()}, Stack: {stack}")
    
    print()


def demo_queue():
    """Demo Queue operations"""
    print("=== QUEUE DEMO ===")
    queue = Queue()
    
    # Enqueue
    for i in [1, 2, 3, 4]:
        queue.enqueue(i)
        print(f"Enqueue {i}: {queue}")
    
    # Dequeue
    while not queue.is_empty():
        print(f"Dequeue: {queue.dequeue()}, Queue: {queue}")
    
    print()


def demo_applications():
    """Demo Stack/Queue applications"""
    print("=== APPLICATIONS DEMO ===\n")
    
    # Balanced parentheses
    expressions = ["({[]})", "({[}])", "((()))", "((()]"]
    print("Balanced Parentheses:")
    for exp in expressions:
        print(f"  {exp}: {is_balanced_parentheses(exp)}")
    print()
    
    # Postfix evaluation
    print("Postfix Evaluation:")
    print(f"  '2 3 1 * + 9 -' = {evaluate_postfix('2 3 1 * + 9 -')}")
    print()
    
    # Next greater element
    arr = [4, 5, 2, 10, 8]
    print(f"Next Greater Element:")
    print(f"  Input:  {arr}")
    print(f"  Output: {next_greater_element(arr)}")
    print()
    
    # Sliding window maximum
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Sliding Window Maximum (k={k}):")
    print(f"  Input:  {arr}")
    print(f"  Output: {sliding_window_maximum(arr, k)}")
    print()
    
    # BFS
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print(f"BFS from 'A':")
    print(f"  {bfs_graph(graph, 'A')}")
    print()


if __name__ == "__main__":
    demo_stack()
    demo_queue()
    demo_applications()
    
    print("All demos completed! ✅")
