# 🚀 Quick Start Guide

## 🎯 Bắt đầu học DSA từ đây!

### Step 1: Hiểu Complexity Analysis (Week 1)

**Tại sao quan trọng?** Đây là nền tảng để đánh giá hiệu quả của algorithms.

📖 **Đọc**: [Complexity Analysis Theory](01_fundamentals/complexity_analysis/theory.md)
💻 **Chạy**: [Examples Code](01_fundamentals/complexity_analysis/examples.py)
📝 **Làm**: [Practice Problems](01_fundamentals/complexity_analysis/practice.md)

**Mục tiêu**:

- ✅ Hiểu Big O notation
- ✅ Phân tích được time & space complexity
- ✅ Nhận biết O(1), O(n), O(n²), O(log n)

---

### Step 2: Master Arrays (Week 2-3)

Arrays là cấu trúc đơn giản nhất nhưng có **nhiều techniques quan trọng**.

📖 **Đọc**: [Arrays Theory](02_linear_structures/arrays/theory.md)
💻 **Code**: [Arrays Implementation](02_linear_structures/arrays/implementation.py)

**Key Techniques cần học**:

1. **Two Pointers** - Most common pattern
2. **Sliding Window** - Optimize subarray problems
3. **Prefix Sum** - Efficient range queries
4. **Binary Search** - O(log n) search

**Suggested Learning Order**:

1. Day 1-2: Đọc theory + chạy examples
2. Day 3-5: Implement Two Pointers problems (5 bài)
3. Day 6-8: Implement Sliding Window problems (5 bài)
4. Day 9-10: Binary Search + Prefix Sum (5 bài)

---

### Step 3: Practice Daily (Ongoing)

**Rule of thumb**: Làm ít nhất **2 problems/day**.

#### Easy Problems (Start here)

1. Two Sum
2. Remove Duplicates from Sorted Array
3. Move Zeros
4. Best Time to Buy and Sell Stock
5. Maximum Subarray

#### After mastering Easy:

- Move to Medium (1 problem/day)
- Review Easy problems weekly
- Track progress trong [progress.md](progress.md)

---

## 📅 Sample Weekly Schedule

### Week 1: Fundamentals

| Day | Topic                     | Tasks                                     |
| --- | ------------------------- | ----------------------------------------- |
| Mon | Big O Introduction        | Read theory, understand O(1), O(n), O(n²) |
| Tue | Logarithmic & Exponential | Learn O(log n), O(2ⁿ), practice problems  |
| Wed | Space Complexity          | Understand call stack, recursion space    |
| Thu | Practice                  | Analyze 10 code snippets                  |
| Fri | Optimization              | Two Sum: O(n²) → O(n)                     |
| Sat | Review                    | Redo all problems                         |
| Sun | Rest / Light reading      | Prepare for next week                     |

### Week 2-3: Arrays

| Day | Topic              | Tasks                                    |
| --- | ------------------ | ---------------------------------------- |
| Mon | Arrays Basics      | Read theory, understand array operations |
| Tue | Two Pointers (1)   | Learn pattern, solve 3 problems          |
| Wed | Two Pointers (2)   | Solve 3 more problems                    |
| Thu | Sliding Window (1) | Fixed size window, 2 problems            |
| Fri | Sliding Window (2) | Variable size window, 3 problems         |
| Sat | Binary Search      | Learn pattern, 3 problems                |
| Sun | Review             | Redo all problems from scratch           |

**Week 3**: Repeat với harder problems + Prefix Sum + Kadane's Algorithm

---

## 💡 Learning Tips

### 1. **Active Learning**

❌ Đừng chỉ đọc code
✅ Type lại code từ đầu
✅ Modify và experiment
✅ Giải thích code cho người khác (hoặc rubber duck)

### 2. **Pattern Recognition**

Sau mỗi problem, hỏi:

- Pattern gì được dùng?
- Khi nào apply pattern này?
- Variations của pattern?

### 3. **Spaced Repetition**

- Day 1: Solve problem
- Day 3: Redo problem
- Week 2: Redo again
- Month 1: Final review

### 4. **Don't Memorize**

❌ Học thuộc code
✅ Hiểu logic và approach
✅ Có thể derive solution from scratch

---

## 🎯 How to Practice Effectively

### When stuck on a problem:

**Timelimit**: Nghĩ 20-30 phút trước khi xem hint/solution.

```
Step 1: Understand (5 phút)
- Đọc kỹ problem
- Clarify constraints
- Test với example

Step 2: Brute Force (5-10 phút)
- Nghĩ cách đơn giản nhất
- Phân tích complexity
- Code nếu reasonable

Step 3: Optimize (10-15 phút)
- Có thể optimize không?
- Pattern nào có thể apply?
- Trade space for time?

Step 4: Implement (15-20 phút)
- Code clean solution
- Handle edge cases
- Test với examples

Step 5: Review (5 phút)
- Analyze complexity
- Any better approach?
- Learn from solution
```

---

## 🛠️ Setup Your Environment

### Required:

- **Python 3.8+** (hoặc ngôn ngữ bạn chọn)
- **Code Editor**: VSCode (recommended), PyCharm, Sublime
- **Terminal/Command Line**

### Recommended Extensions (VSCode):

- Python
- Python Debugger
- Code Runner
- Better Comments

### Testing Setup:

```python
# Create test file: test_arrays.py
def test_two_sum():
    from arrays.implementation import two_sum_hash
    assert two_sum_hash([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_hash([3, 2, 4], 6) == [1, 2]
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_two_sum()
```

---

## 📊 Track Your Progress

Create `progress.md` file:

```markdown
# My DSA Progress

## Week 1: Complexity Analysis

- [x] Big O Notation
- [x] Time Complexity
- [x] Space Complexity
- [x] Practice Problems (10/10)

## Week 2-3: Arrays

- [x] Arrays Theory
- [x] Two Pointers (5/5 problems)
- [ ] Sliding Window (3/5 problems) ← Currently here
- [ ] Binary Search (0/5 problems)
- [ ] Prefix Sum (0/3 problems)

## Problems Solved: 23

- Easy: 15
- Medium: 8
- Hard: 0

## Weak Areas to Review:

- Sliding Window variable size
- Binary Search edge cases
```

---

## 🎓 Resources

### Books (Choose one):

- **"Grokking Algorithms"** (Easiest, visual) ⭐ Recommended for beginners
- **"Cracking the Coding Interview"** (Interview focus)
- **"Introduction to Algorithms"** (CLRS - Advanced)

### Online Platforms:

- **LeetCode**: Best for interview prep
- **HackerRank**: Good for beginners
- **Codeforces**: Competitive programming
- **NeetCode**: Curated problem lists

### Video Resources:

- **NeetCode**: Clear explanations
- **Abdul Bari**: Deep algorithm analysis
- **William Fiset**: Data structures

### Visualization Tools:

- **VisuAlgo**: Algorithm visualizations
- **Python Tutor**: Step-by-step execution
- **LeetCode Playground**: Test code quickly

---

## ❓ FAQ

### Q: Tôi nên học ngôn ngữ nào?

**A**: Python (recommended), Java, C++, hoặc JavaScript. Chọn một và stick với nó.

### Q: Bao lâu để giỏi DSA?

**A**:

- **Basic proficiency**: 3-4 months (2-3 hours/day)
- **Interview ready**: 6-8 months
- **Advanced**: 12+ months

### Q: Tôi nên làm bao nhiêu bài/ngày?

**A**:

- **Beginner**: 1-2 Easy problems
- **Intermediate**: 1 Medium hoặc 2-3 Easy
- **Advanced**: 1 Hard hoặc 2 Medium

Quality > Quantity. Hiểu sâu 1 bài tốt hơn làm qua loa 5 bài.

### Q: Tôi luôn xem solution, có sao không?

**A**:

- Nghĩ ít nhất 20-30 phút trước khi xem
- Xem hint trước, không phải full solution
- Sau khi xem, implement lại without looking
- Redo problem sau vài ngày

### Q: Pattern nào quan trọng nhất?

**A**: Top 5 cho interviews:

1. Two Pointers / Sliding Window
2. Hash Table
3. Binary Search
4. DFS/BFS (Graphs/Trees)
5. Dynamic Programming

---

## 🏁 Your First Week Challenge

Complete này trong 7 ngày:

### Day 1-2: Setup & Theory

- [ ] Clone/Setup repository
- [ ] Đọc Complexity Analysis theory
- [ ] Chạy examples.py
- [ ] Understand Big O

### Day 3-4: Practice

- [ ] Làm 5 Complexity Analysis practice problems
- [ ] Analyze 10 code snippets
- [ ] Create progress.md file

### Day 5-6: Arrays Introduction

- [ ] Đọc Arrays theory
- [ ] Implement Two Pointers examples
- [ ] Solve 3 Easy problems

### Day 7: Review

- [ ] Review tất cả concepts
- [ ] Redo 3 problems without looking
- [ ] Plan Week 2

**After completing**: You're ready for Week 2! 🎉

---

## 📞 Need Help?

### Debugging Tips:

1. Print intermediate results
2. Test với small inputs
3. Check edge cases: empty, single element, duplicates
4. Use debugger (not just prints)

### Common Mistakes:

- Off-by-one errors
- Not handling empty input
- Integer overflow in binary search
- Modifying array while iterating

---

**Ready to start? Go to**: [Complexity Analysis Theory](01_fundamentals/complexity_analysis/theory.md)

**Good luck on your DSA journey! 🚀**
