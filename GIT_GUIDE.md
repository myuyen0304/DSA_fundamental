# 🔧 HƯỚNG DẪN GIT & COMMIT CHO DSA REPOSITORY

## 📚 MỤC LỤC

1. [Git Basics](#git-basics)
2. [Commit Từng File](#commit-từng-file)
3. [Commit Folder](#commit-folder)
4. [Commit Messages Best Practices](#commit-messages-best-practices)
5. [Workflow Cho DSA Repository](#workflow-cho-dsa-repository)
6. [Git Commands Cheatsheet](#git-commands-cheatsheet)

---

## GIT BASICS

### **Kiểm tra Git status**

```bash
# Xem files đã thay đổi
git status

# Xem chi tiết thay đổi
git diff

# Xem diff của file cụ thể
git diff path/to/file.py
```

### **Git workflow cơ bản**

```
Working Directory → Staging Area → Local Repository → Remote Repository
    (edit)      →  (git add)    →  (git commit)    →  (git push)
```

---

## COMMIT TỪNG FILE

### **Cách 1: Add và commit từng file riêng lẻ**

```bash
# Add 1 file vào staging
git add 01_fundamentals/complexity_analysis/theory.md

# Commit file đó
git commit -m "docs: add complexity analysis theory"

# Push lên remote
git push
```

### **Cách 2: Add nhiều files cụ thể**

```bash
# Add nhiều files cùng lúc
git add file1.py file2.md file3.py

# Commit
git commit -m "feat: add implementations for arrays and linked lists"

# Push
git push
```

### **Ví dụ thực tế: Commit từng file trong Binary Trees**

```bash
# Commit theory trước
git add 03_trees/binary_trees/theory.md
git commit -m "docs(trees): add binary trees theory and concepts"
git push

# Commit implementation sau
git add 03_trees/binary_trees/implementation.py
git commit -m "feat(trees): implement binary tree with all traversals"
git push

# Commit practice cuối cùng
git add 03_trees/binary_trees/practice.md
git commit -m "docs(trees): add 20 binary tree practice problems"
git push
```

**Lợi ích**: Commit history rõ ràng, dễ track changes cho từng file

---

## COMMIT FOLDER

### **Cách 1: Commit cả folder cùng lúc**

```bash
# Add toàn bộ folder
git add 03_trees/binary_trees/

# Commit
git commit -m "feat(trees): complete binary trees module"

# Push
git push
```

### **Cách 2: Commit folder theo từng loại file**

```bash
# Add chỉ các file .md trong folder
git add 03_trees/binary_trees/*.md
git commit -m "docs(trees): add binary trees documentation"

# Add chỉ các file .py trong folder
git add 03_trees/binary_trees/*.py
git commit -m "feat(trees): add binary trees implementation"

# Push tất cả
git push
```

### **Cách 3: Interactive staging (chọn từng thay đổi)**

```bash
# Mode interactive - chọn từng file/change
git add -i

# Hoặc patch mode - review từng chunk
git add -p 03_trees/binary_trees/implementation.py
```

### **Ví dụ: Commit toàn bộ BST module**

```bash
# Commit cả module BST một lần
git add 03_trees/bst/
git commit -m "feat(trees): complete BST module with theory, implementation, and practice"
git push
```

---

## COMMIT MESSAGES BEST PRACTICES

### **Format chuẩn (Conventional Commits)**

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### **Types phổ biến**

| Type         | Mô tả                  | Ví dụ                                           |
| ------------ | ---------------------- | ----------------------------------------------- |
| **feat**     | Thêm feature mới       | `feat(arrays): add two pointers implementation` |
| **docs**     | Thay đổi documentation | `docs(complexity): update Big O examples`       |
| **fix**      | Fix bug                | `fix(trees): correct height calculation`        |
| **refactor** | Refactor code          | `refactor(stacks): optimize stack operations`   |
| **test**     | Thêm tests             | `test(arrays): add unit tests for sorting`      |
| **style**    | Format code            | `style: fix indentation in all files`           |
| **chore**    | Maintenance tasks      | `chore: update .gitignore`                      |

### **Scopes cho DSA repository**

- `fundamentals` - Complexity analysis, problem solving
- `arrays` - Array implementations
- `lists` - Linked lists
- `stacks` - Stack implementations
- `queues` - Queue implementations
- `trees` - Tree structures (binary trees, BST, AVL, heaps)
- `graphs` - Graph algorithms
- `sorting` - Sorting algorithms
- `searching` - Search algorithms
- `dp` - Dynamic programming
- `greedy` - Greedy algorithms

### **Good Commit Messages Examples**

✅ **GOOD**:

```bash
git commit -m "feat(trees): implement binary tree traversals (inorder, preorder, postorder)"
git commit -m "docs(arrays): add sliding window pattern explanation"
git commit -m "fix(bst): correct delete operation for nodes with two children"
git commit -m "feat(practice): add 20 medium problems for graphs"
```

❌ **BAD**:

```bash
git commit -m "update"
git commit -m "fix bug"
git commit -m "add stuff"
git commit -m "work in progress"
```

### **Multi-line commit message**

```bash
git commit -m "feat(trees): implement BST with all operations" -m "
- Add insert, delete, search methods
- Implement min/max finding
- Add validate BST function
- Include range query support
- Add comprehensive examples
"
```

---

## WORKFLOW CHO DSA REPOSITORY

### **Workflow 1: Commit từng module hoàn chỉnh**

**Khi bạn hoàn thành 1 module (ví dụ: Binary Trees)**

```bash
# Step 1: Check status
git status

# Step 2: Add toàn bộ module
git add 03_trees/binary_trees/

# Step 3: Commit với message rõ ràng
git commit -m "feat(trees): complete binary trees module

- Add comprehensive theory with examples
- Implement all traversal methods (DFS & BFS)
- Add tree properties (height, diameter, balance)
- Include 20 practice problems (Easy to Hard)
- Add test cases and examples
"

# Step 4: Push
git push
```

---

### **Workflow 2: Commit theo progress hàng ngày**

**Cuối mỗi ngày học**

```bash
# Xem những gì đã thay đổi
git status

# Add files đã làm hôm nay
git add .

# Commit với progress note
git commit -m "progress: Day 5 - Binary Trees practice

Completed:
- Solved 8 Easy problems
- Understood tree traversal patterns
- Practiced recursive thinking

Tomorrow:
- Continue with Medium problems
- Study BST theory
"

# Push
git push
```

---

### **Workflow 3: Commit theo từng concept**

**Khi học từng khái niệm nhỏ**

```bash
# Concept 1: Tree traversals
git add 03_trees/binary_trees/implementation.py
git commit -m "feat(trees): implement inorder, preorder, postorder traversals"
git push

# Concept 2: Tree properties
git add 03_trees/binary_trees/implementation.py
git commit -m "feat(trees): add height, size, and balance check methods"
git push

# Concept 3: Practice problems
git add 03_trees/binary_trees/practice.md
git commit -m "docs(trees): add 10 tree traversal practice problems"
git push
```

---

### **Workflow 4: Feature branch workflow (Advanced)**

**Khi làm việc với các tính năng lớn**

```bash
# Tạo branch mới cho feature
git checkout -b feature/heaps-module

# Làm việc và commit trên branch
git add 03_trees/heaps/
git commit -m "feat(trees): implement heap data structure"

# Push branch
git push -u origin feature/heaps-module

# Khi hoàn thành, merge vào main
git checkout main
git merge feature/heaps-module
git push

# Xóa branch (optional)
git branch -d feature/heaps-module
```

---

## GIT COMMANDS CHEATSHEET

### **Staging & Committing**

```bash
# Add specific file
git add path/to/file.py

# Add all files in directory
git add path/to/directory/

# Add all files with extension
git add *.py
git add *.md

# Add all changes
git add .
git add -A

# Remove from staging
git reset path/to/file.py

# Commit
git commit -m "message"

# Commit with detailed message
git commit -m "title" -m "description"

# Amend last commit
git commit --amend -m "new message"
```

### **Viewing Changes**

```bash
# Status
git status
git status -s    # Short format

# Differences
git diff                           # Working directory vs staging
git diff --staged                  # Staging vs last commit
git diff HEAD                      # Working directory vs last commit
git diff file.py                   # Specific file

# History
git log                            # All commits
git log --oneline                  # Compact view
git log --graph --oneline --all    # Visual graph
git log -5                         # Last 5 commits
git log --author="name"            # By author
```

### **Undoing Changes**

```bash
# Discard changes in working directory
git checkout -- file.py

# Unstage file (keep changes)
git reset HEAD file.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️
git reset --hard HEAD~1

# Revert commit (create new commit)
git revert <commit-hash>
```

### **Branching**

```bash
# List branches
git branch
git branch -a    # Include remote

# Create branch
git branch branch-name

# Switch branch
git checkout branch-name
git switch branch-name   # Newer command

# Create and switch
git checkout -b branch-name

# Delete branch
git branch -d branch-name

# Merge branch
git merge branch-name
```

### **Remote Operations**

```bash
# Add remote
git remote add origin <url>

# View remotes
git remote -v

# Push
git push
git push origin main
git push -u origin main   # Set upstream

# Pull
git pull
git pull origin main

# Fetch (without merge)
git fetch
```

### **Helpful Commands**

```bash
# Show commit details
git show <commit-hash>

# Show file at specific commit
git show <commit-hash>:path/to/file

# List files in commit
git show --name-only <commit-hash>

# Search in code
git grep "search-term"

# Blame (who changed what)
git blame file.py

# Stash changes
git stash
git stash pop
git stash list
```

---

## CÁC TÌNH HUỐNG THƯỜNG GẶP

### **Tình huống 1: Commit nhầm file**

```bash
# Gỡ file khỏi staging (chưa commit)
git reset HEAD unwanted-file.py

# Đã commit rồi - undo commit
git reset --soft HEAD~1
git reset HEAD unwanted-file.py
git commit -m "correct commit message"
```

### **Tình huống 2: Sửa commit message cuối cùng**

```bash
# Chưa push
git commit --amend -m "new message"

# Đã push (cẩn thận với force push!)
git commit --amend -m "new message"
git push --force
```

### **Tình huống 3: Commit nhiều thay đổi nhỏ thành 1 commit lớn**

```bash
# Interactive rebase
git rebase -i HEAD~5

# Trong editor, đổi 'pick' thành 'squash' cho commits muốn gộp
# Save và exit
```

### **Tình huống 4: Xem history của 1 file**

```bash
# History của file
git log -- path/to/file.py

# Xem changes trong mỗi commit
git log -p -- path/to/file.py
```

### **Tình huống 5: Rollback về version cũ của file**

```bash
# Xem file ở commit cụ thể
git show <commit-hash>:path/to/file.py

# Restore file từ commit cụ thể
git checkout <commit-hash> -- path/to/file.py
```

---

## WORKFLOW ĐỀ XUẤT CHO DSA REPOSITORY

### **Option A: Daily Commits (Recommended for learning)**

```bash
# Cuối mỗi session học
git add .
git commit -m "progress: [topic] - completed [what you learned]"
git push
```

**Example**:

```bash
git add .
git commit -m "progress: Binary Trees Day 2 - completed traversals

- Implemented inorder, preorder, postorder
- Solved 5 easy problems
- Understood recursion patterns
"
git push
```

### **Option B: Feature-based Commits (Recommended for projects)**

```bash
# Mỗi khi hoàn thành 1 concept/module
git add [specific files]
git commit -m "feat([scope]): [description]"
git push
```

**Example**:

```bash
git add 03_trees/binary_trees/
git commit -m "feat(trees): complete binary trees module with 20 problems"
git push
```

### **Option C: Granular Commits (Best for collaboration)**

```bash
# Commit từng file/concept nhỏ
git add specific-file.py
git commit -m "feat([scope]): [specific change]"
git push
```

**Example**:

```bash
git add 03_trees/binary_trees/theory.md
git commit -m "docs(trees): add binary tree theory and visualization"
git push

git add 03_trees/binary_trees/implementation.py
git commit -m "feat(trees): implement tree traversal methods"
git push
```

---

## GIT BEST PRACTICES

### **✅ DO**

1. **Commit thường xuyên** - Small, focused commits
2. **Write meaningful messages** - Explain WHAT and WHY
3. **Review changes before commit** - `git diff`
4. **Keep commits atomic** - 1 commit = 1 logical change
5. **Pull before push** - Avoid conflicts
6. **Use branches** cho features lớn
7. **Backup thường xuyên** - Push daily

### **❌ DON'T**

1. **Commit generated files** - \*.pyc, **pycache**, .DS_Store
2. **Commit sensitive data** - Passwords, API keys
3. **Use vague messages** - "update", "fix"
4. **Commit half-done work** - Use stash instead
5. **Push directly to main** nếu làm việc nhóm
6. **Force push** nếu không hiểu rõ
7. **Commit everything with `git add .`** mà không review

---

## SETUP .GITIGNORE

Tạo file `.gitignore` trong root directory:

```bash
# .gitignore for DSA repository

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Personal notes (nếu không muốn commit)
personal_notes/
draft/

# Test output
*.log
test_results/
```

Sau khi tạo:

```bash
git add .gitignore
git commit -m "chore: add .gitignore for Python and IDE files"
git push
```

---

## QUICK REFERENCE

### **Everyday Commands**

```bash
# Morning routine
git pull                    # Get latest changes

# Work on code...

# End of day
git status                  # Check what changed
git add .                   # Stage changes
git commit -m "progress: topic - what you did"
git push                    # Backup to remote
```

### **Before Starting New Topic**

```bash
git pull                    # Get latest
git checkout -b topic-name  # Create branch (optional)
# Work...
git add .
git commit -m "feat(topic): implement X"
git push
```

---

## TÓM TẮT

### **Commit 1 File**

```bash
git add path/to/file.py
git commit -m "type(scope): description"
git push
```

### **Commit 1 Folder**

```bash
git add path/to/folder/
git commit -m "type(scope): description"
git push
```

### **Commit Everything**

```bash
git add .
git commit -m "type(scope): description"
git push
```

### **Recommended Workflow**

```bash
# Hàng ngày
git pull                                    # Start
# ... code ...
git add .                                   # Stage
git commit -m "progress: what you did"     # Commit
git push                                    # Backup

# Hoàn thành module
git add module-folder/
git commit -m "feat(module): complete with implementation and practice"
git push
```

---

**Happy Coding! 🚀**

_Tài liệu này được thiết kế để giúp bạn quản lý DSA repository hiệu quả._
