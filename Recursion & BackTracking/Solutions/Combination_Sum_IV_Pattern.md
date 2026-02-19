# Combination Sum IV — Why Pure Recursion Fails & Why Memoization Is Required

This document explains:

- Why naive recursion is NOT optimized
- Where unnecessary recomputation happens
- How to detect overlapping subproblems
- Time & Space complexity (before and after memoization)
- When to use memoization
- How to think about this problem structurally

---

# 🔎 Problem Context

We are solving:

**Combination Sum IV**

- Given `nums`
- Count number of ways to reach `target`
- Order matters
- You can reuse numbers unlimited times

Example:

```
nums = [1,2]
target = 4

Valid combinations:
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2

Answer = 5
```

---

# ❌ Naive Recursive Implementation

```python
n = len(nums)

def get_comb(tar):

    if tar == 0:
        return 1

    cnt = 0
    for i in range(n):
        if tar >= nums[i]:
            cnt += get_comb(tar - nums[i])

    return cnt

return get_comb(target)
```

---

# 🚨 Why This Is Not Optimized

The function state depends ONLY on:

```
tar
```

But we recompute the same `tar` multiple times.

---

# 🌳 Recursion Tree Example

Example:

```
nums = [1,2]
target = 4
```

Recursion tree:

```
f(4)
 ├─ f(3)
 │   ├─ f(2)
 │   │   ├─ f(1)
 │   │   │   └─ f(0)
 │   │   └─ f(0)
 │   └─ f(1)
 │       └─ f(0)
 └─ f(2)
     ├─ f(1)
     │   └─ f(0)
     └─ f(0)
```

Notice:

- `f(2)` computed twice
- `f(1)` computed three times
- `f(0)` computed many times

This is **overlapping subproblems**.

---

# ⏱ Time Complexity (Without Memoization)

Worst case:

- Each state calls `n` recursive calls
- Depth ≈ `target` (if nums contains 1)

\[
Time ≈ O(n^{target})
\]

Exponential growth.

Very slow.

---

# 📦 Space Complexity (Without Memoization)

| Component | Space |
|-----------|--------|
| Recursion Stack | O(target) |
| No extra storage | O(1) |

Total:

\[
Space = O(target)
\]

---

# 🧠 Core Insight

Whenever recursion looks like:

```
f(x) calls f(x - something)
```

And state depends on ONE variable:

```
State = x
```

Then:

- Unique states = x + 1
- Overlapping happens
- Memoization is required

This is **1D Dynamic Programming**.

---

# ✅ Optimized Version (Memoization)

```python
from functools import lru_cache

@lru_cache(None)
def get_comb(tar):

    if tar == 0:
        return 1

    cnt = 0
    for num in nums:
        if tar >= num:
            cnt += get_comb(tar - num)

    return cnt

return get_comb(target)
```

---

# 🚀 Why Memoization Fixes It

Now:

Each `tar` value is computed ONLY once.

Total unique states:

```
0,1,2,...,target
```

Count = `target + 1`

For each state → loop over `n` numbers

\[
Time = O(n × target)
\]

Massive improvement from exponential.

---

# 📦 Space Complexity (With Memoization)

| Component | Space |
|-----------|--------|
| Memo table | O(target) |
| Recursion stack | O(target) |

\[
Total Space = O(target)
\]

---

# 🔥 Why This Is Different From Subsets

| Problem | State Definition | Growth |
|----------|----------------|--------|
| Subsets | Decision per element | 2ⁿ |
| Combination Sum IV | Remaining target | O(target) states |

Subsets depend on element inclusion.

Combination Sum IV depends only on numeric remainder.

---

# 🧠 When Should You Use Memoization?

Use memoization when:

1. State is clearly identifiable.
2. Same state can be reached through multiple paths.
3. Recursion tree shows repeated subtrees.
4. State space is small compared to recursion tree size.

Here:

```
State = tar
```

And it repeats heavily.

So memoization is mandatory.

---

# 🧮 Bottom-Up Version (Even Cleaner)

```python
dp = [0] * (target + 1)
dp[0] = 1

for t in range(1, target + 1):
    for num in nums:
        if t >= num:
            dp[t] += dp[t - num]

return dp[target]
```

---

# Complexity (Bottom-Up)

\[
Time = O(n × target)
\]
\[
Space = O(target)
\]

---

# 🎯 Final Mental Model

Always ask:

1. What defines my state?
2. How many unique states exist?
3. Am I recomputing states?
4. Can I cache them?

If state count << recursion tree size  
→ You must memoize.

---

# 🔥 Final Comparison

| Version | Time | Space |
|----------|------|-------|
| Pure Recursion | O(n^target) | O(target) |
| Memoized | O(n × target) | O(target) |
| Bottom-Up DP | O(n × target) | O(target) |

---

# 🚀 Key Takeaway

Combination Sum IV is NOT a subset problem.

It is a **1D DP counting problem**.

If you don't memoize, recursion explodes.

If you memoize, it becomes linear DP.

---

This is foundational for understanding:

- Coin Change
- Target Sum
- Integer Partition
- Climbing Stairs
- 1D DP patterns
