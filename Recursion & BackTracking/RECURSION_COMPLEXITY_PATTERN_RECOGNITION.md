# 🧠 Master Guide: Instantly Identifying Recursive Time Complexity

---

# 🚨 STEP 0 — Before Doing Anything

Whenever you see recursion, ask:

1. What defines a state?
2. Does the state repeat?
3. How many choices per level?
4. What is maximum depth?
5. Is the recursion tree full or pruned?

Then map it to one of the patterns below.

---

# 🔵 PATTERN 1 — Subset Pattern → 2^n

## Signature

- At each index → **Take or Skip**
- Index increases by 1
- Depth = n

## Code Shape

```python
def dfs(i):
    if i == n:
        return

    dfs(i+1)   # take
    dfs(i+1)   # skip
```

Recursion Tree

Level 0: 1 node
Level 1: 2 nodes
Level 2: 4 nodes
Level 3: 8 nodes
...
Level n: 2^n nodes

Total nodes ≈ 2^n

Complexity

Time = O(2^n)
Space = O(n) (recursion depth)
Output space = O(n × 2^n)

Example Problems

Subsets

Palindrome Partitioning (structure)

Binary decision problems

🔴 PATTERN 2 — Permutation Pattern → n!
Signature

Loop over remaining elements

Choices shrink every level

Depth = n

Code Shape
for i in remaining:
    recurse(without i)
Tree Structure

Level 0 → n choices
Level 1 → n-1 choices
Level 2 → n-2 choices
...
Level n → 1 choice

Total calls:

n × (n-1) × (n-2) × ... × 1 = n!

Complexity

Time = O(n!)
Space = O(n)
Output space = O(n × n!)

Example Problems

Permutations

N-Queens

Full arrangement problems

🟢 PATTERN 3 — Repeated State Explosion → Needs DP
Signature

Function arguments repeat.

Example:

f(5)
├── f(4)
│ ├── f(3)
├── f(3)

Repeated state detected → exponential recomputation.

Without Memoization

Time = Exponential
Common forms:

O(2^n)
O(n^target)

With Memoization

Time = Number of states × transition cost

Example: Combination Sum IV

States = target
Transitions = n

Time = O(target × n)
Space = O(target)

🟡 PATTERN 4 — Catalan Growth (Pruned Tree)
Signature

Binary-like branching

Invalid branches pruned

Counting valid structures

Examples:

Generate Parentheses

Unique BST

Mountain arrays

Example: Generate Parenthesis
if l < n:
    dfs(l+1, r)

if l > r:
    dfs(l, r+1)

Valid outputs count:

Catalan(n) ≈ 4^n / (n^(3/2))

Complexity

Time = O(Catalan(n))
Space = O(n)
Output = O(n × Catalan(n))

🟣 PATTERN 5 — Polynomial Recursion
Signature

Loop inside recursion

Depth small or bounded

No exponential explosion

Example:

for i in range(n):
    recurse(smaller_input)

If depth = k:

Time = O(n^k)

🧨 How to Instantly Detect Pattern
Case 1: Exactly 2 calls per level

→ 2^n

Case 2: Loop shrinks each level

→ n!

Case 3: Same argument appears twice

→ Needs memoization → DP

Case 4: Constraints prune branches

→ Count valid outputs → Catalan-like

Case 5: States countable directly

→ states × transitions

🧩 Full Comparison Table
Pattern	Branching	Depth	Time	Example
Subsets	2	n	2^n	Subsets
Permutations	n, n-1	n	n!	Permutations
Exponential DP	varies	target	n^target	Naive Comb IV
Memoized DP	states	—	states × trans	Comb IV
Catalan	pruned 2	2n	4^n / n^1.5	Parentheses
🔥 Visual Intuition Training
Why 2^n?

Each element:
Included or not.

Binary decision repeated n times.

Why n!?

Each position:
Pick 1 of remaining elements.

Arrangements explode factorially.

Why DP?

State repeats.
You are recomputing same question.

Why Catalan?

Binary-like growth
BUT only valid balanced paths survive.

🚀 Ultimate Mental Model

When you see recursion:

Is state repeating?
YES → DP
NO → continue

Does each level have 2 fixed choices?
YES → 2^n

Does choice pool shrink each level?
YES → n!

Is tree pruned by constraints?
YES → Count valid outputs

Can states be counted directly?
YES → states × transitions
