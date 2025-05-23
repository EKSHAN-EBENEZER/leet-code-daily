'''
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
'''








class Solution:
    def countLargestGroup(self, n: int) -> int:
        s = str(n + 1)
        sm = len(s) * 9 + 1
        dp = [0] * sm
        x = 0
        
        for ch in s:
            digit = int(ch)
            dp2 = [0] * sm
            
            for j in range(sm):
                for k in range(10):
                    if j + k < sm:
                        dp2[j + k] += dp[j]
            
            dp = dp2
            for j in range(digit):
                if x + j < sm:
                    dp[x + j] += 1
            x += digit
        
        dp[0] = 0
        max_freq = max(dp)
        return dp.count(max_freq)
