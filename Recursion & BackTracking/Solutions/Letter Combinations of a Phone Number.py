# Problem - https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        n = len(digits)
        op = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        comb = []
        ans = []

        def letter_combinations(k):            
            
            if k == n:
                ans.append("".join(comb[:]))
                return
            if k>n:
                return

            for let in op.get(digits[k],[]):
 
                comb.append(let)
                letter_combinations(k+1)
                comb.pop()
            
        letter_combinations(0)
        return ans
      

#============= Time Complexiy ==========
For each digit:
You choose one letter.
Then move to the next digit.
Continue until all digits are used.
If length of digits = n

Each digit gives:

3 letters (most digits)

4 letters (7 and 9)

Worst case → assume 4 letters per digit

🌳 Recursion Structure

At each level:

You have up to 4 choices

Depth of recursion = n
4 × 4 × 4 × ... (n times)
= 4^n


At every valid combination:

"".join(comb)

This takes O(n) time (joining n characters).
So total time:  Number of combinations × work per combination => 4^n × n
✅ Final Time Complexity: O(n × 4^n)

#============= Space Complexity ========

1️⃣ Recursion stack depth

Max depth = n
→ O(n)

2️⃣ Temporary list comb

Stores at most n characters
→ O(n)
