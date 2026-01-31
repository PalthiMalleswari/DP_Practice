# Recursion Tree Analysis — Subsets vs Permutations

This document explains:

- Why **subsets = 2ⁿ**
- Why **permutations = n!**
- How loop recursion hides skip decisions
- How to calculate **time AND space complexity**

---

# 🌿 PART 1 — SUBSETS (Combinations Style)

Given:
```
arr = [1,2,3]
```

We want all subsets.

---

## ✅ Version 1 — TAKE / SKIP (Binary Recursion)

```python
def f(i, path):
    if i == len(arr):
        print(path)
        return

    # TAKE arr[i]
    f(i+1, path + [arr[i]])

    # SKIP arr[i]
    f(i+1, path)
```

---

### 🌳 Recursion Tree

```
Level 0 (i=0)
                    []
               /            \
           [1]                []
        /      \           /      \
     [1,2]    [1]       [2]        []
     /   \    /  \      /  \      /  \
[1,2,3][1,2][1,3][1][2,3][2][3][]
```

Each level = decision about one element  
Each element → 2 choices

\[
Total subsets = 2^3 = 8
\]

---

## ✅ Version 2 — LOOP STYLE (Same Logic Hidden)

```python
def f(start, path):
    print(path)

    for i in range(start, len(arr)):
        f(i+1, path + [arr[i]])
```

---

### 🌳 Recursion Tree

```
                      []
         /              |              \
       [1]             [2]             [3]
     /     \             \
 [1,2]   [1,3]          [2,3]
   |
[1,2,3]
```

---

## 🔥 Where did "SKIP" happen?

| Loop Move | Meaning |
|----------|---------|
| start=0 → i=1 | Skipped element 1 |
| start=0 → i=2 | Skipped 1 and 2 |

Loop compresses skip decisions into index jumps.

---

## 🎯 SUBSET COMPLEXITY

### ⏱ Time Complexity

Each element has 2 states:

| Element | In subset? |
|---------|------------|
| Yes | No |

\[
Time = 2^n
\]

---

### 📦 Space Complexity

| Type | Reason | Space |
|------|--------|-------|
| Recursion Stack | Depth = n decisions | **O(n)** |
| Temporary Path | Stores up to n elements | **O(n)** |
| Output Storage | Stores all subsets | **O(n × 2^n)** |

---

# 🌳 PART 2 — PERMUTATIONS

Here order matters.

```python
def perm(path, used):
    if len(path) == len(arr):
        print(path)
        return

    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            perm(path + [arr[i]], used)
            used[i] = False
```

---

## 🌳 Recursion Tree

```
Level 0:
      [1]   [2]   [3]

Level 1:
[1] → choose 2 or 3
[2] → choose 1 or 3
[3] → choose 1 or 2

Level 2:
Only 1 choice left
```

---

## 🎯 PERMUTATION COMPLEXITY

### ⏱ Time Complexity

At each position:

| Position | Choices |
|----------|---------|
| 1st | n |
| 2nd | n-1 |
| 3rd | n-2 |

\[
Time = n!
\]

---

### 📦 Space Complexity

| Type | Reason | Space |
|------|--------|-------|
| Recursion Stack | Depth = n levels | **O(n)** |
| Path Storage | Stores n elements | **O(n)** |
| Used Array | Tracks n elements | **O(n)** |
| Output Storage | Stores all permutations | **O(n × n!)** |

---

# 🧠 CORE DIFFERENCE

| Problem | Decision Type | Growth |
|--------|----------------|--------|
| Subsets | Each element exists or not | 2ⁿ |
| Permutations | Each position chooses from remaining | n! |

---

# 💡 Memory Trick

| Code Pattern | Complexity |
|--------------|------------|
| `recurse(i+1)` | Subsets → 2ⁿ |
| `choose from unused` | Permutations → n! |

---

# 🧮 Recursion Complexity Formula

\[
Time = BranchingFactor^{Depth}
\]

| Case | Branching | Depth |
|------|-----------|-------|
| Subsets | 2 | n |
| Permutations | decreasing (n, n-1, ...) | n |

---

# 🚀 Final Understanding

Loop does **NOT** increase branching.

It just represents **multiple skip decisions at once**.

True logical model:

```
Each element → Include or Exclude
Binary choices → 2ⁿ
```

Permutations instead decide:

```
Which element goes at each position → n!
```

---

**This is the foundation of backtracking complexity analysis.**
