# 📘 1-D Dynamic Programming Patterns – Complete Revision Notes

> **Goal:**
> Build a strong intuition for **why** a recurrence exists, so you can derive it yourself in interviews and contests.

---

## 🧠 Universal 1-D DP Thinking Process

For **any** 1-D DP problem, answer these in order:

1. **What does `dp[i]` represent?**
2. **What choices can I make at index `i`?**
3. **Which previous indices affect index `i`?**
4. **Combine choices → recurrence**
5. **Define base cases carefully**
6. **Optimize space if possible**

> Most 1-D DP problems are:
> **“Decision at index `i` using answers before `i`”**

---

## 🔹 General 1-D DP Template

```python
dp = [0] * (n + 1)

dp[base_cases...]

for i in range(start, n):
    dp[i] = best(dp[i-1], dp[i-2], ..., dp[i-k])
```

Where `best` can be:

* `max`
* `min`
* `sum`
* `count`

---

# 🧩 PATTERN 1: Fibonacci / Count Ways DP

### 🔹 Core Idea

Number of ways to reach index `i` equals sum of ways to reach valid previous indices.

---

### 🧠 Why the Recurrence?

To reach `i`, you must come from:

* `i-1`
* `i-2`

Each path is independent → **add them**

---

### 🧮 Recurrence

```
dp[i] = dp[i-1] + dp[i-2]
```

---

### 📌 Problems

* Climbing Stairs
  [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)
* Fibonacci Number
  [https://leetcode.com/problems/fibonacci-number/](https://leetcode.com/problems/fibonacci-number/)
* N-th Tribonacci
  [https://leetcode.com/problems/n-th-tribonacci-number/](https://leetcode.com/problems/n-th-tribonacci-number/)

---

# 🧩 PATTERN 2: Take or Skip (Non-Adjacent)

### 🔹 Core Idea

At index `i`, you either:

* take it → skip adjacent
* skip it → take previous best

---

### 🧠 Why the Recurrence?

You **cannot take adjacent elements**, so if you take `i`, the previous allowed state is `i-2`.

---

### 🧮 Recurrence

```
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

---

### 📌 Problems

* House Robber
  [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)
* House Robber II
  [https://leetcode.com/problems/house-robber-ii/](https://leetcode.com/problems/house-robber-ii/)
* Delete and Earn
  [https://leetcode.com/problems/delete-and-earn/](https://leetcode.com/problems/delete-and-earn/)

---

# 🧩 PATTERN 3: Min Cost to Reach End

### 🔹 Core Idea

Minimize total cost to reach index `i`.

---

### 🧠 Why the Recurrence?

To reach `i`, you must come from:

* `i-1`
* `i-2`

Choose the **cheapest path**, then add current cost.

---

### 🧮 Recurrence

```
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

---

### 📌 Problems

* Min Cost Climbing Stairs
  [https://leetcode.com/problems/min-cost-climbing-stairs/](https://leetcode.com/problems/min-cost-climbing-stairs/)

---

# 🧩 PATTERN 4: Jump With K Steps

### 🔹 Core Idea

From index `i`, you can jump up to `k` steps.

---

### 🧠 Why the Recurrence?

To reach `i`, you could come from **any index in the range** `[i-k, i-1]`.

---

### 🧮 Recurrence

```
dp[i] = min(dp[i-j]) for j in range(1, k+1)
```

---

### 📌 Problems

* Jump Game II
  [https://leetcode.com/problems/jump-game-ii/](https://leetcode.com/problems/jump-game-ii/)
* Frog Jump (variants)

---

# 🧩 PATTERN 5: Reachability (Boolean DP)

### 🔹 Core Idea

Determine **whether** an index can be reached.

---

### 🧠 Why the Recurrence?

Index `i` is reachable if **any previous reachable index** can jump to it.

---

### 🧮 Recurrence

```
dp[i] = True if ∃ j < i such that dp[j] and j + nums[j] >= i
```

---

### 📌 Problems

* Jump Game
  [https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)
* Jump Game III
  [https://leetcode.com/problems/jump-game-iii/](https://leetcode.com/problems/jump-game-iii/)

---

# 🧩 PATTERN 6: Count All Valid Paths

### 🔹 Core Idea

Count all ways to form a target.

---

### 🧠 Why the Recurrence?

To form sum `i`, choose a number `num`, then count ways to form `i - num`.

---

### 🧮 Recurrence

```
dp[i] += dp[i - num]
```

---

### 📌 Problems

* Combination Sum IV
  [https://leetcode.com/problems/combination-sum-iv/](https://leetcode.com/problems/combination-sum-iv/)
* Perfect Squares
  [https://leetcode.com/problems/perfect-squares/](https://leetcode.com/problems/perfect-squares/)

---

# 🧩 PATTERN 7: Maximum Subarray (Kadane’s DP)

### 🔹 Core Idea

At index `i`, either:

* extend previous subarray
* start fresh

---

### 🧠 Why the Recurrence?

If previous sum is negative, it hurts the current sum → restart.

---

### 🧮 Recurrence

```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

---

### 📌 Problems

* Maximum Subarray
  [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
* Maximum Circular Subarray
  [https://leetcode.com/problems/maximum-sum-circular-subarray/](https://leetcode.com/problems/maximum-sum-circular-subarray/)

---

# 🧩 PATTERN 8: Partition / Break DP

### 🔹 Core Idea

Break a number/string into parts for optimal result.

---

### 🧠 Why the Recurrence?

Try **every possible split**, choose the best.

---

### 🧮 Recurrence

```
dp[i] = max(j * (i-j), j * dp[i-j]) for j in range(1, i)
```

---

### 📌 Problems

* Integer Break
  [https://leetcode.com/problems/integer-break/](https://leetcode.com/problems/integer-break/)
* Word Break
  [https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)

---

# 🧩 PATTERN 9: Stock Buy/Sell (State Compression)

### 🔹 Core Idea

Profit depends on previous day’s decision.

---

### 🧠 Why the Recurrence?

You either:

* hold stock
* sell stock
* do nothing

---

### 📌 Problems

* Best Time to Buy and Sell Stock
  [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* Stock with Cooldown
  [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

---

# 🧩 PATTERN 10: LIS-Style DP (1-D + Inner Loop)

### 🔹 Core Idea

Best sequence ending at index `i`.

---

### 🧠 Why the Recurrence?

To extend a sequence, previous element must be smaller.

---

### 🧮 Recurrence

```
dp[i] = max(dp[j] + 1) for j < i if nums[j] < nums[i]
```

---

### 📌 Problems

* Longest Increasing Subsequence
  [https://leetcode.com/problems/longest-increasing-subsequence/](https://leetcode.com/problems/longest-increasing-subsequence/)
* Longest Arithmetic Subsequence
  [https://leetcode.com/problems/longest-arithmetic-subsequence/](https://leetcode.com/problems/longest-arithmetic-subsequence/)

---

# 🧩 PATTERN 11: Decode / String DP (1-D)

### 🔹 Core Idea

Single or double character decisions.

---

### 🧠 Why the Recurrence?

At index `i`:

* decode one digit → `dp[i-1]`
* decode two digits → `dp[i-2]`

---

### 🧮 Recurrence

```
dp[i] = dp[i-1] + dp[i-2]
```

---

### 📌 Problems

* Decode Ways
  [https://leetcode.com/problems/decode-ways/](https://leetcode.com/problems/decode-ways/)

---

## ✅ Final DP Checklist

* What does `dp[i]` mean?
* What decisions exist at `i`?
* Which previous states matter?
* Base cases correct?
* Can space be optimized?

---

## 🏁 Key Insight

> **DP is not about memorizing formulas.**
> It is about **turning brute-force decisions into stored results**.

---
