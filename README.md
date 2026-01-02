# 📚 Data Structures and Algorithms - Lộ trình học từ Lý thuyết đến Hands-on

> **"Algorithms + Data Structures = Programs"** - Niklaus Wirth

## 🎯 Mục tiêu

Repository này được thiết kế để giúp bạn học DSA một cách **có hệ thống** từ lý thuyết cơ bản đến thực hành nâng cao, bao gồm:

- ✅ Lý thuyết chi tiết với giải thích dễ hiểu
- ✅ Implementation code với comments chi tiết
- ✅ Phân tích complexity (Time & Space)
- ✅ Bài tập thực hành từ Easy → Hard
- ✅ Solutions với nhiều approaches

## 📂 Cấu trúc Repository

```
dsa/
├── 01_fundamentals/           # Nền tảng cơ bản
│   ├── complexity_analysis/   # Big O, Time/Space Complexity
│   └── problem_solving/       # Cách tiếp cận giải quyết vấn đề
│
├── 02_linear_structures/      # Cấu trúc tuyến tính
│   ├── arrays/                # Mảng và kỹ thuật xử lý
│   ├── strings/               # Xử lý chuỗi
│   ├── linked_lists/          # Danh sách liên kết
│   ├── stacks/                # Ngăn xếp
│   └── queues/                # Hàng đợi
│
├── 03_trees/                  # Cấu trúc cây
│   ├── binary_trees/          # Cây nhị phân
│   ├── bst/                   # Binary Search Tree
│   ├── avl_trees/             # Cây AVL
│   ├── heaps/                 # Heap & Priority Queue
│   └── trie/                  # Trie
│
├── 04_graphs/                 # Đồ thị
│   ├── representation/        # Biểu diễn đồ thị
│   ├── traversal/             # DFS, BFS
│   ├── shortest_path/         # Dijkstra, Bellman-Ford
│   └── mst/                   # Minimum Spanning Tree
│
├── 05_algorithms/             # Thuật toán
│   ├── sorting/               # Các thuật toán sắp xếp
│   ├── searching/             # Tìm kiếm
│   ├── two_pointers/          # Kỹ thuật hai con trỏ
│   ├── sliding_window/        # Sliding Window
│   └── binary_search/         # Binary Search nâng cao
│
├── 06_advanced/               # Nâng cao
│   ├── dynamic_programming/   # Quy hoạch động
│   ├── greedy/                # Thuật toán tham lam
│   ├── backtracking/          # Quay lui
│   └── bit_manipulation/      # Thao tác bit
│
├── practice/                  # Bài tập thực hành
│   ├── easy/                  # Bài tập dễ
│   ├── medium/                # Bài tập trung bình
│   └── hard/                  # Bài tập khó
│
└── resources/                 # Tài liệu tham khảo
    ├── cheatsheets/           # Bảng tóm tắt
    ├── patterns/              # Các pattern thường gặp
    └── interview_prep/        # Chuẩn bị phỏng vấn
```

## 🗺️ Lộ trình học chi tiết (20 Tuần - 7-10 Tháng)

### **Phase 1: Fundamentals (Tuần 1-3)** ✅

Xây dựng nền tảng vững chắc trước khi đi sâu vào các cấu trúc dữ liệu phức tạp.

#### **Tuần 1: Complexity Analysis** ⭐ BẮT ĐẦU TẠI ĐÂY

**Thời gian**: 10-12 giờ | **Mục tiêu**: Hiểu Big O và phân tích complexity

- **Day 1-2**: Big O Notation
  - 📖 [Lý thuyết](01_fundamentals/complexity_analysis/theory.md) (2h)
  - 💻 [Examples](01_fundamentals/complexity_analysis/examples.py) (1h)
  - Học các complexity: O(1), O(log n), O(n), O(n log n), O(n²)
- **Day 3-4**: Time vs Space Complexity
  - Phân biệt time và space complexity
  - Best/Average/Worst case
  - 📝 [Practice](01_fundamentals/complexity_analysis/practice.md) - làm 5 bài đầu
- **Day 5-7**: Master Complexity
  - Làm 10 bài practice còn lại
  - Học recognize complexity patterns
  - Review [Complexity Cheatsheet](resources/cheatsheets/complexity_cheatsheet.md)

**Checkpoint**: Có thể phân tích complexity của bất kỳ code nào trong vài giây

---

#### **Tuần 2: Arrays & Two Pointers**

**Thời gian**: 12-15 giờ | **Mục tiêu**: Master array operations và Two Pointers pattern

- **Day 1-2**: Array Fundamentals
  - 📖 [Theory](02_linear_structures/arrays/theory.md) (2h)
  - Array operations: insert, delete, search
  - Memory layout và indexing
- **Day 3-4**: Two Pointers Pattern
  - 💻 [Implementation](02_linear_structures/arrays/implementation.py) - Two Pointers section
  - Two Sum, Remove Duplicates, Reverse
  - Container With Most Water
- **Day 5-6**: Sliding Window
  - Fixed và Variable size windows
  - Maximum subarray problems
  - Longest substring problems
- **Day 7**: Practice
  - 📝 [Practice](02_linear_structures/arrays/practice.md) - làm 8 bài Easy đầu
  - Focus: Two Pointers và Sliding Window

**Checkpoint**: Có thể identify và solve Two Pointers/Sliding Window problems

---

#### **Tuần 3: Linked Lists, Stacks & Queues**

**Thời gian**: 12-15 giờ | **Mục tiêu**: Understand pointer manipulation và LIFO/FIFO

- **Day 1-3**: Linked Lists
  - 📖 [Theory](02_linear_structures/linked_lists/theory.md) (2h)
  - 💻 [Implementation](02_linear_structures/linked_lists/implementation.py) (3h)
  - Singly/Doubly/Circular lists
  - Fast & Slow Pointers (cycle detection)
- **Day 4-5**: Stacks & Queues
  - 📖 [Theory](02_linear_structures/stacks_queues/theory.md) (2h)
  - 💻 [Implementation](02_linear_structures/stacks_queues/implementation.py) (2h)
  - Stack: Valid Parentheses, Min Stack
  - Queue: Implement using arrays/linked lists
- **Day 6-7**: Practice
  - 📝 [Stacks/Queues Practice](02_linear_structures/stacks_queues/practice.md) - 10 bài
  - Monotonic Stack problems
  - BFS với Queue

**Checkpoint**: Comfortable với pointer manipulation và stack/queue applications

---

### **Phase 2: Trees & Graphs (Tuần 4-7)** 🌳

#### **Tuần 4: Binary Trees**

**Thời gian**: 12-15 giờ | **Mục tiêu**: Master tree traversals và recursion

- **Day 1-2**: Tree Basics
  - 📖 [Theory](03_trees/binary_trees/theory.md) (2h)
  - Tree terminology: root, leaf, height, depth
  - Types: Full, Complete, Perfect, Balanced
- **Day 3-4**: Tree Traversals
  - 💻 [Implementation](03_trees/binary_trees/implementation.py) (3h)
  - Inorder, Preorder, Postorder (recursive + iterative)
  - Level Order (BFS)
- **Day 5-6**: Tree Properties
  - Height, Diameter, Balance check
  - Path Sum problems
  - Lowest Common Ancestor
- **Day 7**: Practice
  - 📝 [Practice](03_trees/binary_trees/practice.md) - 8 bài Easy đầu

**Checkpoint**: Thành thạo tree traversals và recursive thinking

---

#### **Tuần 5: Binary Search Tree (BST)**

**Thời gian**: 10-12 giờ | **Mục tiêu**: Understand BST property và operations

- **Day 1-2**: BST Theory
  - 📖 [Theory](03_trees/bst/theory.md) (2h)
  - BST property: left < root < right
  - Search, Insert, Delete operations
- **Day 3-4**: BST Implementation
  - 💻 [Implementation](03_trees/bst/implementation.py) (3h)
  - Validate BST (common interview question!)
  - Kth Smallest Element
  - LCA in BST
- **Day 5-7**: Practice
  - 📝 [Practice](03_trees/bst/practice.md) - 10 bài
  - Convert sorted array to BST
  - Range sum queries

**Checkpoint**: Can implement và validate BST, hiểu khi nào dùng BST

---

#### **Tuần 6: Heaps & Priority Queues**

**Thời gian**: 10-12 giờ | **Mục tiêu**: Master heap operations và Top K problems

- **Day 1-2**: Heap Theory
  - Min Heap vs Max Heap
  - Heapify operations
  - Heap vs BST
- **Day 3-4**: Implementation
  - Build heap from array
  - Heap Sort
  - Python heapq module
- **Day 5-7**: Practice
  - Top K Frequent Elements
  - Kth Largest Element
  - Merge K Sorted Lists
  - Median from Data Stream

**Checkpoint**: Comfortable với heap operations và Priority Queue problems

---

#### **Tuần 7: Graphs Basics**

**Thời gian**: 12-15 giờ | **Mục tiêu**: Understand graph representation và traversals

- **Day 1-2**: Graph Theory
  - Adjacency Matrix vs List
  - Directed vs Undirected
  - Weighted vs Unweighted
- **Day 3-4**: Graph Traversals
  - DFS (recursive + iterative)
  - BFS with Queue
  - Connected Components
- **Day 5-7**: Practice
  - Number of Islands
  - Clone Graph
  - Course Schedule (Topological Sort)
  - Shortest Path in Binary Matrix

**Checkpoint**: Can implement DFS/BFS và solve basic graph problems

---

### **Phase 3: Algorithms (Tuần 8-12)** ⚡

#### **Tuần 8: Sorting Algorithms**

**Thời gian**: 10-12 giờ | **Mục tiêu**: Understand sorting algorithms deeply

- **Day 1-3**: Comparison Sorts
  - Merge Sort: O(n log n)
  - Quick Sort: Average O(n log n)
  - Heap Sort
- **Day 4-5**: Non-Comparison Sorts
  - Counting Sort: O(n + k)
  - Radix Sort
  - Bucket Sort
- **Day 6-7**: Practice
  - Sort Colors (Dutch National Flag)
  - Merge Sorted Arrays
  - Custom sort comparators

**Checkpoint**: Know when to use which sorting algorithm

---

#### **Tuần 9: Binary Search Mastery**

**Thời gian**: 10-12 giờ | **Mục tiêu**: Master binary search và variants

- **Day 1-2**: Binary Search Basics
  - Classic binary search
  - Lower bound / Upper bound
  - Search in rotated array
- **Day 3-5**: Binary Search on Answer
  - Minimize/Maximize problems
  - Split Array Largest Sum
  - Capacity To Ship Packages
- **Day 6-7**: Practice
  - 15-20 binary search problems
  - Focus on edge cases

**Checkpoint**: Can identify when to use binary search on complex problems

---

#### **Tuần 10-11: Advanced Graph Algorithms**

**Thời gian**: 15-18 giờ | **Mục tiêu**: Shortest paths và advanced techniques

- **Tuần 10**: Shortest Path
  - Dijkstra's Algorithm
  - Bellman-Ford
  - Floyd-Warshall
- **Tuần 11**: Advanced Topics
  - Minimum Spanning Tree (Kruskal, Prim)
  - Strongly Connected Components
  - Union-Find (Disjoint Set)

**Checkpoint**: Can solve shortest path và MST problems

---

#### **Tuần 12: Pattern Recognition**

**Thời gian**: 10-12 giờ | **Mục tiêu**: Master common coding patterns

- Review patterns đã học:
  - Two Pointers
  - Sliding Window
  - Fast & Slow Pointers
  - Merge Intervals
  - Cyclic Sort
  - Top K Elements
- 📖 [Common Patterns](resources/patterns/common_patterns.md)
- Practice mixed problems (20+ bài)

**Checkpoint**: Can quickly identify pattern cho mỗi problem

---

### **Phase 4: Advanced (Tuần 13-20)** 🚀

#### **Tuần 13-15: Dynamic Programming**

**Thời gian**: 20-25 giờ | **Mục tiêu**: Master DP thinking

- **Tuần 13**: DP Fundamentals
  - Memoization vs Tabulation
  - 1D DP: Fibonacci, Climbing Stairs, House Robber
  - State definition
- **Tuần 14**: 2D DP
  - Grid problems
  - Longest Common Subsequence (LCS)
  - Edit Distance
  - Knapsack problems
- **Tuần 15**: Advanced DP
  - Longest Increasing Subsequence (LIS)
  - Palindrome problems
  - DP on trees
  - DP with bitmask

**Checkpoint**: Can solve 60%+ medium DP problems

---

#### **Tuần 16-17: Greedy & Backtracking**

**Thời gian**: 12-15 giờ mỗi tuần

- **Tuần 16**: Greedy Algorithms
  - When to use greedy
  - Interval scheduling
  - Jump Game
  - Gas Station
- **Tuần 17**: Backtracking
  - Template và pruning
  - Permutations & Combinations
  - N-Queens
  - Sudoku Solver
  - Generate Parentheses

**Checkpoint**: Can identify greedy opportunities và implement backtracking

---

#### **Tuần 18-19: Bit Manipulation & Advanced Topics**

**Thời gian**: 10-12 giờ

- **Bit Manipulation**
  - AND, OR, XOR operations
  - Bit tricks: power of 2, count bits
  - XOR problems
- **Advanced Data Structures**
  - Trie (Prefix Tree)
  - Segment Tree
  - Fenwick Tree (BIT)

**Checkpoint**: Comfortable với bit operations

---

#### **Tuần 20: Review & Mock Interviews**

**Thời gian**: 15-20 giờ | **Mục tiêu**: Consolidate knowledge

- Review tất cả patterns
- Làm 20 random problems (mix difficulty)
- Mock interviews (tự setup timer)
- Review mistakes và weak areas
- Update [Progress Tracker](progress_template.md)

**Final Checkpoint**: Ready for coding interviews! 🎉

---

## 📊 Thời gian học đề xuất

### **Lịch học theo mức độ**:

| Mức độ           | Giờ/ngày | Giờ/tuần  | Thời gian hoàn thành |
| ---------------- | -------- | --------- | -------------------- |
| **Intensive** 🔥 | 3-4 giờ  | 20-25 giờ | 4-5 tháng            |
| **Balanced** ⚖️  | 2-3 giờ  | 15-20 giờ | 6-7 tháng            |
| **Relaxed** 🌱   | 1-2 giờ  | 10-15 giờ | 9-10 tháng           |

### **Phân bổ thời gian mỗi ngày**:

```
📚 Theory:        30-40% (đọc, hiểu concepts)
💻 Implementation: 20-30% (code từ đầu, không copy)
📝 Practice:      30-40% (giải problems)
🔁 Review:        10% (ôn lại patterns)
```

### **Ví dụ lịch học Balanced (2h/ngày)**:

```
Thứ 2-6:
  - 30 phút: Đọc theory
  - 45 phút: Code implementation
  - 45 phút: Practice problems (2-3 bài)

Thứ 7:
  - 3 giờ: Focus practice (8-10 bài)
  - Review tuần qua

Chủ nhật:
  - 2 giờ: Ôn lại concepts
  - Làm 1-2 bài hard từ topics đã học
```

## 📖 Cách sử dụng Repository này

### 1️⃣ **Học Lý thuyết**

Mỗi topic có file `theory.md` giải thích:

- Khái niệm cơ bản
- Khi nào sử dụng
- Ưu/nhược điểm
- Complexity analysis
- Visual diagrams

### 2️⃣ **Đọc Implementation**

File `implementation.py` chứa:

- Code được comment chi tiết
- Nhiều cách tiếp cận khác nhau
- Best practices
- Common pitfalls

### 3️⃣ **Làm Bài tập**

File `practice.md` trong mỗi topic:

- Bài tập từ dễ đến khó
- Gợi ý approach
- Link đến solutions
- Test cases

### 4️⃣ **Xem Solutions**

File `solutions.py`:

- Multiple approaches
- Time/Space complexity
- Giải thích từng bước
- Trade-offs

### 5️⃣ **Test & Debug**

File `tests.py`:

- Unit tests
- Edge cases
- Performance testing

## ⏱️ Timeline Đề xuất

| Cấp độ           | Thời gian | Mục tiêu                                |
| ---------------- | --------- | --------------------------------------- |
| **Beginner**     | 3-4 tháng | Hoàn thành Phase 1-2, làm 100+ bài Easy |
| **Intermediate** | 2-3 tháng | Hoàn thành Phase 3, làm 100+ bài Medium |
| **Advanced**     | 2-3 tháng | Hoàn thành Phase 4, làm 50+ bài Hard    |

**Tổng cộng: 7-10 tháng** để nắm vững DSA từ cơ bản đến nâng cao.

## 🎯 Mục tiêu học tập theo tuần

### Beginner Goal:

- ✅ Hiểu rõ complexity analysis
- ✅ Thành thạo arrays, strings, linked lists
- ✅ Biết cách sử dụng stacks và queues
- ✅ Giải được 70%+ bài Easy

### Intermediate Goal:

- ✅ Hiểu và implement được các loại trees
- ✅ Thành thạo graph algorithms
- ✅ Nắm vững sorting & searching
- ✅ Giải được 60%+ bài Medium

### Advanced Goal:

- ✅ Thành thạo Dynamic Programming
- ✅ Biết khi nào dùng Greedy vs DP
- ✅ Giải quyết được complex problems
- ✅ Giải được 40%+ bài Hard

## 📊 Tracking Progress

Tạo file `progress.md` để theo dõi:

```markdown
- [x] Week 1: Complexity Analysis
- [x] Week 2: Arrays & Strings (15/15 problems)
- [ ] Week 3: Linked Lists (8/20 problems)
- [ ] ...
```

## 🛠️ Setup & Requirements

### Language: Python 3.8+

Tất cả code examples được viết bằng Python vì:

- Syntax dễ đọc, dễ hiểu
- Focus vào logic, không bị distract bởi syntax
- Rich built-in data structures
- Được sử dụng rộng rãi trong interviews

### Tools Recommended:

- **IDE**: VSCode, PyCharm
- **Testing**: pytest
- **Visualization**: Python Tutor, VisuAlgo
- **Practice**: LeetCode, HackerRank, Codeforces

## 📚 Tài liệu tham khảo

### Books:

- "Introduction to Algorithms" (CLRS)
- "Cracking the Coding Interview" - Gayle Laakmann McDowell
- "Grokking Algorithms" - Aditya Bhargava (dễ hiểu cho beginners)

### Online Resources:

- [LeetCode](https://leetcode.com) - Practice problems
- [VisuAlgo](https://visualgo.net) - Algorithm visualizations
- [CP-Algorithms](https://cp-algorithms.com) - In-depth explanations
- [Neetcode](https://neetcode.io) - Curated problem sets

### YouTube Channels:

- NeetCode
- Abdul Bari
- William Fiset
- Back To Back SWE

## 💡 Tips để học hiệu quả

1. **Consistency > Intensity**: Học 2 giờ/ngày tốt hơn 14 giờ/tuần chỉ vào cuối tuần
2. **Implement from scratch**: Đừng copy-paste, type lại code để hiểu sâu
3. **Teach to learn**: Giải thích cho người khác (hoặc rubber duck debugging)
4. **Track your progress**: Ghi chép những gì đã học, pattern đã thấy
5. **Don't memorize, understand**: Hiểu tại sao, không chỉ học thuộc code
6. **Practice daily**: Làm ít nhất 1-2 bài/ngày
7. **Review regularly**: Ôn lại các topic cũ mỗi tuần
8. **Focus on patterns**: Nhận diện patterns thay vì học từng bài riêng lẻ

## 🎓 Sau khi hoàn thành

Khi đã nắm vững DSA, bạn có thể:

- ✅ Tự tin trong coding interviews
- ✅ Giải quyết problems efficiently
- ✅ Design better software systems
- ✅ Contribute to open source projects
- ✅ Participate in competitive programming

## 🤝 Contributing

Nếu bạn muốn đóng góp:

- Thêm bài tập mới
- Cải thiện explanations
- Fix bugs trong code
- Thêm visualizations

## 📞 Support

Nếu có câu hỏi hoặc gặp khó khăn:

1. Đọc kỹ theory trước
2. Debug code từng bước
3. Google error messages
4. Tham khảo solutions
5. Hỏi trong communities (Reddit, Discord, Stack Overflow)

---

## 🚀 Bắt đầu ngay!

**Bước 1**: Đọc [Complexity Analysis](01_fundamentals/complexity_analysis/theory.md)

**Bước 2**: Làm 5 bài đầu tiên trong [Arrays Practice](02_linear_structures/arrays/practice.md)

**Bước 3**: Check [Cheat Sheet](resources/cheatsheets/complexity_cheatsheet.md)

**Good luck trên hành trình chinh phục DSA! 💪**

---

_Last updated: January 2026_
