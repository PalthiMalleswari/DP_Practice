# Ones and Zeroes (LeetCode 474) - Complete DP Revision Notes

# Problem Statement

Given:

```python
strs = ["10","0001","111001","1","0"]
m = 5   # available zeros
n = 3   # available ones
```

Pick the maximum number of strings such that:

```text
Total zeros used <= m
Total ones used <= n
```

Each string can be chosen at most once.

---

# Step 1: Why Is This A Knapsack Problem?

Every string behaves like an item.

Example:

| String | Zeros | Ones | Value |
|----------|--------|--------|--------|
| "10" | 1 | 1 | 1 |
| "0001" | 3 | 1 | 1 |
| "111001" | 2 | 4 | 1 |
| "1" | 0 | 1 | 1 |
| "0" | 1 | 0 | 1 |

Capacity:

```text
m zeros
n ones
```

Value:

```text
1 string selected
```

Goal:

```text
maximize number of selected strings
```

This is:

0/1 Knapsack with TWO capacities.

---

# Step 2: Brute Force

For every string:

```text
Take
or
Skip
```

Recursion Tree:

                         index=0
                        /       \
                    take        skip
                    /             \
               index=1          index=1
                /   \           /   \
             take  skip      take   skip

Each string generates 2 choices.

Total complexity:

```text
O(2^len(strs))
```

---

# Step 3: Recursive State

Define:

```python
f(index, zeros_left, ones_left)
```

Meaning:

Using strings from:

```text
0 ... index
```

with:

```text
zeros_left zeros remaining
ones_left ones remaining
```

what is the maximum number of strings we can still pick?

---

# Transition

Current string:

```python
strs[index]
```

contains:

```python
z = count_zeros
o = count_ones
```

Option 1: Skip

```python
f(index-1, zeros_left, ones_left)
```

Option 2: Take

Only if:

```python
zeros_left >= z
ones_left >= o
```

Then:

```python
1 + f(
    index-1,
    zeros_left-z,
    ones_left-o
)
```

Answer:

```python
max(skip, take)
```

---

# Step 4: Overlapping Subproblems

State:

```python
(index, zeros_left, ones_left)
```

Example:

Different recursion paths may reach:

```python
(2,4,2)
```

Whenever the same state appears again:

```text
same index
same zeros_left
same ones_left
```

the future answer is identical.

Therefore memoization works.

---

# Memoized Complexity

States:

```text
len(strs) * (m+1) * (n+1)
```

Time:

```text
O(len(strs) * m * n)
```

Space:

```text
O(len(strs) * m * n)
```

---

# Step 5: Convert Recursion To DP

Recursive state:

```python
f(index, zeros_left, ones_left)
```

becomes

```python
dp[i][z][o]
```

---

# What Does dp[i][z][o] Mean?

VERY IMPORTANT

```python
dp[i][z][o]
```

means:

Using FIRST i strings,

with:

```text
z zeros available
o ones available
```

what is the maximum number of strings we can select?

---

# Dimensions

Row Dimension:

```text
i
```

Capacity Dimension 1:

```text
z
```

Capacity Dimension 2:

```text
o
```

Table Size:

```python
dp[len(strs)+1][m+1][n+1]
```

---

# 3D DP Transition

Current string:

```python
strs[i-1]
```

contains:

```python
zeros
ones
```

Skip:

```python
dp[i-1][z][o]
```

Take:

```python
1 + dp[i-1][z-zeros][o-ones]
```

Final:

```python
dp[i][z][o] = max(
    dp[i-1][z][o],
    1 + dp[i-1][z-zeros][o-ones]
)
```

---

# Why Previous Row?

This is the most important intuition.

Suppose current string:

```text
"10"
```

When we choose it,

we must solve the remaining problem using:

```text
ONLY previous strings
```

We cannot use the current string again.

Therefore:

```python
dp[i-1]
```

must be used.

Never:

```python
dp[i]
```

---

# Correct 3D DP Code

```python
for i in range(1, len(strs)+1):

    zeros = strs[i-1].count('0')
    ones  = strs[i-1].count('1')

    for z in range(m+1):
        for o in range(n+1):

            dp[i][z][o] = dp[i-1][z][o]

            if z >= zeros and o >= ones:

                dp[i][z][o] = max(
                    dp[i][z][o],
                    1 + dp[i-1][z-zeros][o-ones]
                )
```

---

# 3D DP Complexity

Time:

```text
O(len(strs) * m * n)
```

Space:

```text
O(len(strs) * m * n)
```

---

# Step 6: Space Optimization

Observe:

```python
dp[i][z][o]
```

depends only on:

```python
dp[i-1][...]
```

Therefore we don't need all rows.

Keep only:

```python
dp[z][o]
```

---

# What Does dp[z][o] Mean?

After processing some strings,

```python
dp[z][o]
```

means:

Maximum number of strings achievable using:

```text
z zeros
o ones
```

---

# Transition

For each string:

```python
zeros
ones
```

Update:

```python
dp[z][o] = max(
    dp[z][o],
    1 + dp[z-zeros][o-ones]
)
```

---

# Why Traverse Backwards?

This is THE MOST IMPORTANT optimization concept.

Suppose current string:

```text
"10"
```

Cost:

```text
1 zero
1 one
```

If we traverse forward:

```python
for z in range(zeros, m+1):
```

then:

```python
dp[z-zeros][o-ones]
```

might already contain the current string.

Result:

```text
Current string reused multiple times.
```

That would become:

```text
Unbounded Knapsack
```

which is WRONG.

---

# Backward Traversal

Use:

```python
for z in range(m, zeros-1, -1):
    for o in range(n, ones-1, -1):
```

Now:

```python
dp[z-zeros][o-ones]
```

still represents the previous row.

Current string has not contaminated it.

Therefore:

```text
Each string is used at most once.
```

---

# Final Space Optimized Solution

```python
dp = [[0]*(n+1) for _ in range(m+1)]

for s in strs:

    zeros = s.count('0')
    ones = s.count('1')

    for z in range(m, zeros-1, -1):
        for o in range(n, ones-1, -1):

            dp[z][o] = max(
                dp[z][o],
                1 + dp[z-zeros][o-ones]
            )

return dp[m][n]
```

---

# Complexity Comparison

Brute Force

Time:

```text
O(2^len(strs))
```

Space:

```text
O(len(strs))
```

---

Memoization

Time:

```text
O(len(strs) * m * n)
```

Space:

```text
O(len(strs) * m * n)
```

---

3D Bottom Up

Time:

```text
O(len(strs) * m * n)
```

Space:

```text
O(len(strs) * m * n)
```

---

2D Space Optimized

Time:

```text
O(len(strs) * m * n)
```

Space:

```text
O(m * n)
```

---

# Golden Rule

Whenever recursion state is:

```python
f(index, cap1, cap2)
```

Convert to:

```python
dp[index][cap1][cap2]
```

If transition only depends on:

```python
index-1
```

then:

```python
dp[cap1][cap2]
```

is possible.

For 0/1 problems:

```text
Traverse capacities backward.
```

For unbounded problems:

```text
Traverse capacities forward.
```
