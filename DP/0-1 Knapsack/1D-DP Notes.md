# DP Knapsack Revision Notes

# 1. Core DP Conversion Rule

If recursion state is:

```python
f(index, state1, state2, ...)
```

Then memoization:

```python
memo[(index, state1, state2)]
```

Then bottom-up DP:

```python
dp[index][state1][state2]
```

Every recursive parameter becomes a DP dimension.

---

# 2. 0/1 Knapsack Pattern

## Signals

- Choose a subset of items
- Each item can be used at most once
- Capacity constraint exists
- Maximize / Minimize / Count / Feasibility

Examples:

- 0/1 Knapsack
- Subset Sum
- Partition Equal Subset Sum
- Target Sum
- Last Stone Weight II
- Ones and Zeroes

---

# 3. Classic 0/1 Knapsack

State:

```python
dp[i][w]
```

Meaning:

> Maximum value using first i items with capacity w.

Transition:

```python
dp[i][w] = max(
    dp[i-1][w],                    # skip
    value + dp[i-1][w-weight]      # take
)
```

Why `w-weight`?

If current item is taken:

```text
Remaining capacity = current capacity - item's weight
```

The remaining capacity must be solved using previous items only.

---

# 4. Why Previous Row?

For 0/1 Knapsack:

```python
dp[i][...]
```

must depend on:

```python
dp[i-1][...]
```

because current item cannot be reused.

We need the answer before current item existed.

---

# 5. Space Optimization

If:

```python
dp[i][state]
```

depends only on:

```python
dp[i-1][state]
```

then row `i-1` is the only row needed.

Compress:

```python
dp[state]
```

Space:

```text
O(n * capacity)
↓
O(capacity)
```

---

# 6. Forward vs Backward Traversal

This is the most important concept.

## Ask This Question

When updating:

```python
dp[state] ← dp[state-cost]
```

Should `dp[state-cost]` already include the current item?

---

## Case 1: Current Item MUST NOT Reuse Itself

Examples:

- 0/1 Knapsack
- Subset Sum
- Partition Equal Subset Sum
- Target Sum
- Last Stone Weight II
- Ones and Zeroes

Use:

```python
for state in range(max_state, cost-1, -1):
```

Backward.

Reason:

```text
dp[state-cost]
```

still contains previous row information.

Current item is used at most once.

---

## Case 2: Current Item CAN Reuse Itself

Examples:

- Coin Change
- Unbounded Knapsack
- Rod Cutting

Use:

```python
for state in range(cost, max_state+1):
```

Forward.

Reason:

```text
dp[state-cost]
```

may already contain current item.

Allows unlimited usage.

---

# 7. Target Sum

Original problem:

Assign:

```text
+ or -
```

to every number.

Equation:

```text
P - N = target
P + N = total
```

Add them:

```text
2P = target + total
```

Therefore:

```text
P = (target + total)/2
```

Problem becomes:

> Count subsets whose sum is P.

Now it is a 0/1 Knapsack counting problem.

---

State:

```python
dp[i][s]
```

Meaning:

> Number of ways to make sum s using first i numbers.

Transition:

```python
dp[i][s] =
dp[i-1][s] +
dp[i-1][s-num]
```

---

# 8. Last Stone Weight II

Key observation:

Every smash eventually becomes:

```text
±s1 ±s2 ±s3 ...
```

Equivalent to splitting stones into:

```text
Group A
Group B
```

Goal:

```text
minimize |A - B|
```

Let:

```text
Total = A + B
```

Then:

```text
|A-B|
= |2A - Total|
```

Need subset sum closest to:

```text
Total / 2
```

Problem becomes:

> Find largest subset sum ≤ Total/2

0/1 Knapsack.

Final answer:

```python
total - 2 * best_subset_sum
```

---

# 9. Ones and Zeroes (LeetCode 474)

Each string is an item.

Cost:

```text
zeros count
ones count
```

Value:

```text
1
```

Capacities:

```text
m zeros
n ones
```

---

State:

```python
dp[i][z][o]
```

Meaning:

> Maximum strings using first i strings with z zeros and o ones available.

Transition:

```python
dp[i][z][o] = max(
    dp[i-1][z][o],
    1 + dp[i-1][z-zeros][o-ones]
)
```

---

Space optimized:

```python
dp[z][o]
```

Transition:

```python
dp[z][o] = max(
    dp[z][o],
    1 + dp[z-zeros][o-ones]
)
```

Traversal:

```python
for z in range(m, zeros-1, -1):
    for o in range(n, ones-1, -1):
```

Backward in both dimensions.

Reason:

Each string can be chosen at most once.

---

# 10. How To Detect Overlapping Subproblems

Recursive state:

```python
(index, capacity)
```

or

```python
(index, cap1, cap2)
```

If multiple recursion paths reach the same state:

```text
same index
same capacity
```

then the entire subtree repeats.

Memoization stores the answer once.

---

# 11. Universal DP Derivation Checklist

Step 1:

Identify recursion state.

```python
f(index, state)
```

Step 2:

Convert to memoization.

```python
memo[(index, state)]
```

Step 3:

Convert to table.

```python
dp[index][state]
```

Step 4:

Copy recursion transition.

Step 5:

Check dependency.

If only previous row is used:

```python
dp[i-1]
```

compress space.

Step 6:

Decide traversal.

- Use backward if item is used once.
- Use forward if item can be reused.

---

# Golden Rule

Traversal direction is decided by one question:

> Should the current item be allowed to use its own update during the same iteration?

If NO:

```text
Backward
```

If YES:

```text
Forward
```

This single rule explains almost every knapsack-style DP optimization.
