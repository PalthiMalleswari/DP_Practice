# Fast Power (Binary Exponentiation) — Full Intuition Notes

## Problem
Compute:

xⁿ

Naive approach:
x × x × x × ... (n times) → **O(n)**

Efficient approach:
**Binary Exponentiation → O(log n)**

---

## 1. Core Law We Use

xᵃ⁺ᵇ = xᵃ × xᵇ

If we can break n into smaller pieces, we multiply those pieces.

---

## 2. Binary Representation — The Foundation

Every number can be written as sum of powers of 2.

Examples:

6  = 110₂ = 4 + 2  
13 = 1101₂ = 8 + 4 + 1  

So:

x⁶  = x⁴ × x²  
x¹³ = x⁸ × x⁴ × x¹  

👉 We only need **powers of 2**.

---

## 3. Why Powers of 2 Are Enough

Binary guarantees:

n = 2ᵏ + 2ᵐ + 2ᵖ + ...

Thus:

xⁿ = x^(2ᵏ) × x^(2ᵐ) × x^(2ᵖ)

All exponents can be built from powers of 2.

Example:

x⁵ = x⁴ × x¹  
x³ = x² × x¹  

We never need to compute x³ directly.

---

## 4. How We Build Powers of 2

Start with x¹:

x²  = x¹ × x¹  
x⁴  = x² × x²  
x⁸  = x⁴ × x⁴  
x¹⁶ = x⁸ × x⁸  

Each squaring jumps to the next power of 2.

After k squarings:

x = x^(2ᵏ)

---

## 5. Algorithm

```python
def power(x, n):
    result = 1

    while n > 0:
        if n % 2 == 1:     # last binary bit is 1
            result *= x    # include this power

        x *= x             # move to next power of 2
        n //= 2            # shift bits right

    return result
