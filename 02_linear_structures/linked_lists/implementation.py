"""
Linked Lists - Implementation Examples
Comprehensive implementations with all important patterns
"""

from typing import Optional, List


# ============================================================
# NODE CLASSES
# ============================================================

class ListNode:
    """Singly Linked List Node"""
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f"Node({self.data})"


class DoublyListNode:
    """Doubly Linked List Node"""
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


# ============================================================
# SINGLY LINKED LIST CLASS
# ============================================================

class LinkedList:
    """Singly Linked List Implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_head(self, data):
        """Insert node at beginning - O(1)"""
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data):
        """Insert node at end - O(n)"""
        new_node = ListNode(data)
        
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert at specific position - O(n)"""
        if position == 0:
            self.insert_at_head(data)
            return
        
        new_node = ListNode(data)
        current = self.head
        
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of bounds")
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, key):
        """Delete first node with given key - O(n)"""
        if not self.head:
            return
        
        # Delete head
        if self.head.data == key:
            self.head = self.head.next
            self.size -= 1
            return
        
        # Delete middle/tail
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
    
    def search(self, key):
        """Search for node with given key - O(n)"""
        current = self.head
        position = 0
        
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def get(self, index):
        """Get value at index - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def display(self):
        """Print linked list"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) + " -> None")
    
    def to_list(self):
        """Convert to Python list"""
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"LinkedList({self.to_list()})"


# ============================================================
# PATTERN 1: FAST & SLOW POINTERS
# ============================================================

def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node using Fast & Slow Pointers
    
    Time: O(n)
    Space: O(1)
    
    Example: 1 -> 2 -> 3 -> 4 -> 5
    Result: 3 (middle node)
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
    
    return slow


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using Floyd's Algorithm
    
    Time: O(n)
    Space: O(1)
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find where cycle starts (if exists)
    
    Time: O(n)
    Space: O(1)
    
    Algorithm:
    1. Use Fast & Slow to detect cycle
    2. Reset slow to head
    3. Move both 1 step until they meet
    4. Meeting point is cycle start
    """
    # Detect cycle
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end
    
    Time: O(n)
    Space: O(1)
    
    Technique: Two pointers with n gap
    """
    dummy = ListNode(0)
    dummy.next = head
    
    # Move fast n+1 steps ahead
    fast = dummy
    for _ in range(n + 1):
        if not fast:
            return head
        fast = fast.next
    
    # Move both until fast reaches end
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove node
    slow.next = slow.next.next
    
    return dummy.next


# ============================================================
# PATTERN 2: IN-PLACE REVERSAL
# ============================================================

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list in-place
    
    Time: O(n)
    Space: O(1)
    
    Most important LL operation!
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    
    return prev  # New head


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse nodes from position left to right
    
    Time: O(n)
    Space: O(1)
    
    Example: 1 -> 2 -> 3 -> 4 -> 5, left=2, right=4
    Result: 1 -> 4 -> 3 -> 2 -> 5
    """
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to node before left
    for _ in range(left - 1):
        prev = prev.next
    
    # Reverse from left to right
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Reverse nodes in groups of k
    
    Time: O(n)
    Space: O(1)
    
    Example: 1 -> 2 -> 3 -> 4 -> 5, k=2
    Result: 2 -> 1 -> 4 -> 3 -> 5
    """
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    
    while True:
        # Check if k nodes remaining
        kth_node = prev_group
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next
        
        # Reverse k nodes
        group_prev = kth_node.next
        group_current = prev_group.next
        
        for _ in range(k):
            next_node = group_current.next
            group_current.next = group_prev
            group_prev = group_current
            group_current = next_node
        
        # Connect with previous group
        temp = prev_group.next
        prev_group.next = kth_node
        prev_group = temp
    
    return dummy.next


# ============================================================
# PATTERN 3: MERGE & SORT
# ============================================================

def merge_two_sorted_lists(l1: Optional[ListNode], 
                          l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists
    
    Time: O(n + m)
    Space: O(1)
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Append remaining
    current.next = l1 if l1 else l2
    
    return dummy.next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists
    
    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(1)
    
    Approach: Divide and conquer
    """
    if not lists:
        return None
    
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_sorted_lists(l1, l2))
        lists = merged
    
    return lists[0]


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Sort linked list using merge sort
    
    Time: O(n log n)
    Space: O(log n) - recursion stack
    """
    if not head or not head.next:
        return head
    
    # Find middle
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Split list
    prev.next = None
    
    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(slow)
    
    # Merge sorted halves
    return merge_two_sorted_lists(left, right)


# ============================================================
# PATTERN 4: PALINDROME CHECK
# ============================================================

def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome
    
    Time: O(n)
    Space: O(1)
    
    Approach:
    1. Find middle
    2. Reverse second half
    3. Compare both halves
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = reverse_list(slow)
    
    # Compare
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True


# ============================================================
# PATTERN 5: REARRANGEMENT
# ============================================================

def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorder: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
    
    Time: O(n)
    Space: O(1)
    
    Example: 1 -> 2 -> 3 -> 4 -> 5
    Result: 1 -> 5 -> 2 -> 4 -> 3
    """
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second = reverse_list(slow)
    first = head
    
    # Merge alternately
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swap every two adjacent nodes
    
    Time: O(n)
    Space: O(1)
    
    Example: 1 -> 2 -> 3 -> 4
    Result: 2 -> 1 -> 4 -> 3
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        
        # Swap
        first.next = second.next
        second.next = first
        current.next = second
        
        current = first
    
    return dummy.next


# ============================================================
# ADDITIONAL OPERATIONS
# ============================================================

def remove_duplicates_sorted(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from sorted linked list
    
    Time: O(n)
    Space: O(1)
    """
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Add two numbers represented as linked lists
    
    Time: O(max(n, m))
    Space: O(max(n, m))
    
    Example: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)
    Represents: 342 + 465 = 807
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return dummy.next


def partition_list(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    Partition list: all nodes < x before nodes >= x
    
    Time: O(n)
    Space: O(1)
    
    Example: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
    Result: 1 -> 2 -> 2 -> 4 -> 3 -> 5
    """
    before_head = ListNode(0)
    after_head = ListNode(0)
    before = before_head
    after = after_head
    
    while head:
        if head.data < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    
    after.next = None
    before.next = after_head.next
    
    return before_head.next


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def create_linked_list(values: List) -> Optional[ListNode]:
    """Create linked list from list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def print_linked_list(head: Optional[ListNode]):
    """Print linked list"""
    elements = []
    current = head
    
    while current:
        elements.append(str(current.data))
        current = current.next
    
    print(" -> ".join(elements) + " -> None")


def linked_list_to_list(head: Optional[ListNode]) -> List:
    """Convert linked list to Python list"""
    result = []
    current = head
    
    while current:
        result.append(current.data)
        current = current.next
    
    return result


# ============================================================
# DEMO
# ============================================================

if __name__ == "__main__":
    print("="*60)
    print("LINKED LIST IMPLEMENTATIONS - DEMO")
    print("="*60)
    
    # Demo 1: Basic LinkedList class
    print("\n1. BASIC LINKED LIST OPERATIONS")
    ll = LinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    print("Created list:", ll)
    ll.insert_at_head(0)
    print("After insert at head:", ll)
    ll.display()
    
    # Demo 2: Fast & Slow Pointers
    print("\n2. FAST & SLOW POINTERS - Find Middle")
    head = create_linked_list([1, 2, 3, 4, 5])
    print("List:", end=" ")
    print_linked_list(head)
    middle = find_middle(head)
    print(f"Middle node: {middle.data}")
    
    # Demo 3: Reverse List
    print("\n3. REVERSE LINKED LIST")
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original:", end=" ")
    print_linked_list(head)
    reversed_head = reverse_list(head)
    print("Reversed:", end=" ")
    print_linked_list(reversed_head)
    
    # Demo 4: Merge Two Sorted Lists
    print("\n4. MERGE TWO SORTED LISTS")
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    print("List 1:", end=" ")
    print_linked_list(l1)
    print("List 2:", end=" ")
    print_linked_list(l2)
    merged = merge_two_sorted_lists(l1, l2)
    print("Merged:", end=" ")
    print_linked_list(merged)
    
    # Demo 5: Palindrome Check
    print("\n5. PALINDROME CHECK")
    head = create_linked_list([1, 2, 3, 2, 1])
    print("List:", end=" ")
    print_linked_list(head)
    print(f"Is palindrome: {is_palindrome(head)}")
    
    print("\n" + "="*60)
    print("All demos complete!")
    print("="*60)
