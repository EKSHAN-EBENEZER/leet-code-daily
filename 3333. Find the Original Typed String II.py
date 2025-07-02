'''
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: word = "aabbccdd", k = 7

Output: 5

Explanation:

The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

Example 2:

Input: word = "aabbccdd", k = 8

Output: 1

Explanation:

The only possible string is "aabbccdd".

Example 3:

Input: word = "aaabbb", k = 3

Output: 8

 

Constraints:

1 <= word.length <= 5 * 105
word consists only of lowercase English letters.
1 <= k <= 2000
'''






mod_mul = lambda a, b: (a * b) % 1_000_000_007
mod_add = lambda a, b: (a + b) % 1_000_000_007
mod_sub = lambda a, b: (a - b) % 1_000_000_007

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int: 
        segs = [1]
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                segs.append(1)
            else:
                segs[-1] += 1
        total = reduce(mod_mul, segs)
        if k <= len(segs):
            return total
        
        dp = [1] + ([0] * (k-1))
        for i in range(1, len(segs)+1):
            prefix = list(accumulate(dp, mod_add, initial=0))
            dp = [0] * k
            for j in range(i, k):
                dp[j] = mod_sub(prefix[j], prefix[j - min(segs[i-1], j-i+1)])
        less_than_k = reduce(mod_add, dp)
        return mod_sub(total, less_than_k)
