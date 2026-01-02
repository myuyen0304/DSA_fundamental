# 🔗 Linked Lists - Practice Problems

## 📚 Learning Objectives

After completing these problems, you should be able to:
- ✅ Implement basic linked list operations
- ✅ Use fast & slow pointer technique
- ✅ Reverse linked lists (iterative & recursive)
- ✅ Detect and remove cycles
- ✅ Merge and sort linked lists

---

## 🎯 Problem Categories

### **Category 1: Basic Operations** (Easy)
### **Category 2: Two Pointers** (Easy-Medium)
### **Category 3: Reversal** (Medium)
### **Category 4: Cycle Detection** (Medium)
### **Category 5: Merge & Sort** (Medium-Hard)

---

## 📝 Problems

### **Category 1: Basic Operations**

#### Problem 1: Delete Node in Linked List ⭐
**Difficulty**: Easy | **Pattern**: Basic Operations

**Problem**: Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

**Example**:
```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
```

**Constraints**:
- The node to be deleted is not the tail
- The linked list will have at least two elements

**Hints**:
- You can't access the previous node
- Copy the next node's value

<details>
<summary>Solution</summary>

```python
def deleteNode(node):
    """
    Time: O(1), Space: O(1)
    """
    # Copy next node's data to current node
    node.data = node.next.data
    # Skip next node
    node.next = node.next.next
```
</details>

---

#### Problem 2: Middle of Linked List ⭐⭐
**Difficulty**: Easy | **Pattern**: Two Pointers (Slow & Fast)

**Problem**: Find the middle node of a singly linked list. If there are two middle nodes, return the second one.

**Example**:
```
Input: [1,2,3,4,5]
Output: Node(3)

Input: [1,2,3,4,5,6]
Output: Node(4)
```

**Hints**:
- Use slow and fast pointers
- Fast moves 2 steps, slow moves 1 step

<details>
<summary>Solution</summary>

```python
def middleNode(head):
    """
    Two Pointers - Slow & Fast
    Time: O(n), Space: O(1)
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```
</details>

---

#### Problem 3: Linked List Cycle ⭐⭐
**Difficulty**: Easy | **Pattern**: Floyd's Cycle Detection

**Problem**: Determine if a linked list has a cycle.

**Example**:
```
Input: head = [3,2,0,-4], pos = 1 (tail connects to index 1)
Output: true
```

**Hints**:
- Floyd's Cycle Detection (Tortoise & Hare)
- If fast meets slow, there's a cycle

<details>
<summary>Solution</summary>

```python
def hasCycle(head):
    """
    Floyd's Cycle Detection Algorithm
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```
</details>

---

### **Category 2: Reversal Problems**

#### Problem 4: Reverse Linked List ⭐⭐
**Difficulty**: Easy | **Pattern**: Iterative Reversal

**Problem**: Reverse a singly linked list.

**Example**:
```
Input: 1 → 2 → 3 → 4 → 5 → None
Output: 5 → 4 → 3 → 2 → 1 → None
```

**Hints**:
- Use three pointers: prev, curr, next
- Or use recursion

<details>
<summary>Solution 1: Iterative</summary>

```python
def reverseList(head):
    """
    Iterative approach
    Time: O(n), Space: O(1)
    """
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next  # Save next
        curr.next = prev       # Reverse pointer
        prev = curr            # Move prev
        curr = next_temp       # Move curr
    
    return prev
```
</details>

<details>
<summary>Solution 2: Recursive</summary>

```python
def reverseListRecursive(head):
    """
    Recursive approach
    Time: O(n), Space: O(n) - call stack
    """
    if not head or not head.next:
        return head
    
    # Reverse rest of list
    new_head = reverseListRecursive(head.next)
    
    # Fix pointers
    head.next.next = head
    head.next = None
    
    return new_head
```
</details>

---

#### Problem 5: Palindrome Linked List ⭐⭐⭐
**Difficulty**: Easy-Medium | **Pattern**: Two Pointers + Reversal

**Problem**: Check if a linked list is a palindrome.

**Example**:
```
Input: 1 → 2 → 2 → 1
Output: true

Input: 1 → 2 → 3
Output: false
```

**Hints**:
- Find middle using slow/fast pointers
- Reverse second half
- Compare both halves

<details>
<summary>Solution</summary>

```python
def isPalindrome(head):
    """
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    # Compare
    left, right = head, prev
    while right:  # right is shorter or equal
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    
    return True
```
</details>

---

### **Category 3: Two Pointer Problems**

#### Problem 6: Remove Nth Node From End ⭐⭐⭐
**Difficulty**: Medium | **Pattern**: Two Pointers (Gap)

**Problem**: Remove the nth node from the end of list.

**Example**:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Hints**:
- Use two pointers with gap of n
- Use dummy node for edge cases

<details>
<summary>Solution</summary>

```python
def removeNthFromEnd(head, n):
    """
    Two pointers with gap
    Time: O(L), Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    
    first = second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node
    second.next = second.next.next
    
    return dummy.next
```
</details>

---

#### Problem 7: Intersection of Two Linked Lists ⭐⭐⭐
**Difficulty**: Easy-Medium | **Pattern**: Two Pointers

**Problem**: Find the node at which two singly linked lists intersect.

**Example**:
```
List A: 4 → 1 → 8 → 4 → 5
List B: 5 → 6 → 1 → 8 → 4 → 5
                    ↑ intersection point
Output: 8
```

**Hints**:
- Two pointers switch lists when reaching end
- They'll meet at intersection or None

<details>
<summary>Solution</summary>

```python
def getIntersectionNode(headA, headB):
    """
    Time: O(m + n), Space: O(1)
    """
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        # When reaching end, switch to other list
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA  # intersection or None
```
</details>

---

### **Category 4: Cycle Detection Advanced**

#### Problem 8: Linked List Cycle II ⭐⭐⭐⭐
**Difficulty**: Medium | **Pattern**: Floyd's Cycle Detection

**Problem**: Find the node where the cycle begins. Return null if no cycle.

**Example**:
```
Input: head = [3,2,0,-4], pos = 1
Output: node with value 2
```

**Hints**:
- Use Floyd's algorithm to detect cycle
- Use math: distance from head to cycle start = distance from meeting point to cycle start

<details>
<summary>Solution</summary>

```python
def detectCycle(head):
    """
    Floyd's Cycle Detection + Math
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None
    
    # Phase 1: Detect cycle
    slow = fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    
    if not has_cycle:
        return None
    
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
```
</details>

---

### **Category 5: Merge & Sort**

#### Problem 9: Merge Two Sorted Lists ⭐⭐
**Difficulty**: Easy | **Pattern**: Merge

**Problem**: Merge two sorted linked lists.

**Example**:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

<details>
<summary>Solution</summary>

```python
def mergeTwoLists(l1, l2):
    """
    Time: O(m + n), Space: O(1)
    """
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    # Append remaining
    curr.next = l1 if l1 else l2
    
    return dummy.next
```
</details>

---

#### Problem 10: Sort List ⭐⭐⭐⭐⭐
**Difficulty**: Medium-Hard | **Pattern**: Merge Sort

**Problem**: Sort a linked list in O(n log n) time using constant space.

**Example**:
```
Input: [4,2,1,3]
Output: [1,2,3,4]
```

**Hints**:
- Use merge sort
- Find middle, split, sort recursively, merge

<details>
<summary>Solution</summary>

```python
def sortList(head):
    """
    Merge Sort for Linked List
    Time: O(n log n), Space: O(log n) - recursion stack
    """
    if not head or not head.next:
        return head
    
    # Find middle and split
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None  # Split
    
    # Sort both halves
    left = sortList(head)
    right = sortList(mid)
    
    # Merge
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 if l1 else l2
    return dummy.next
```
</details>

---

## 🎯 Additional Practice Problems

### **More Easy Problems**:
11. Merge k Sorted Lists
12. Remove Duplicates from Sorted List
13. Remove Duplicates from Sorted List II
14. Partition List

### **More Medium Problems**:
15. Rotate List
16. Reorder List
17. Add Two Numbers (as linked lists)
18. Copy List with Random Pointer
19. Flatten a Multilevel Doubly Linked List
20. Reverse Nodes in k-Group

---

## 📊 Progress Tracker

```markdown
Category 1: Basic Operations
- [ ] Problem 1: Delete Node
- [ ] Problem 2: Middle of List
- [ ] Problem 3: Linked List Cycle

Category 2: Reversal
- [ ] Problem 4: Reverse List
- [ ] Problem 5: Palindrome List

Category 3: Two Pointers
- [ ] Problem 6: Remove Nth From End
- [ ] Problem 7: Intersection of Lists

Category 4: Cycle Detection
- [ ] Problem 8: Cycle II

Category 5: Merge & Sort
- [ ] Problem 9: Merge Two Lists
- [ ] Problem 10: Sort List
```

---

## 💡 Key Patterns Summary

### **1. Fast & Slow Pointers**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```
**Use for**: Middle, cycle detection, palindrome

### **2. Dummy Node**
```python
dummy = ListNode(0)
dummy.next = head
```
**Use for**: When head might change

### **3. Reversal Template**
```python
prev = None
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
```

### **4. Two Pointers with Gap**
```python
for _ in range(n):
    first = first.next
while first:
    first = first.next
    second = second.next
```
**Use for**: Nth from end

---

## 🚀 Next Steps

After mastering linked lists:
1. ✅ Move to [Stacks & Queues](../stacks_queues/theory.md)
2. ✅ Review [Common Patterns](../../resources/patterns/common_patterns.md)
3. ✅ Practice more on LeetCode

**Good luck! 🎯**
