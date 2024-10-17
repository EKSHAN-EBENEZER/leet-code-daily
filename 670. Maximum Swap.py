'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''






class Solution:
    def maximumSwap(self, v: int) -> int:
        res = s = str(v)
        for i,c in enumerate(s):
            for j in range(i+1,len(s)):
                res = max(res, s[:i]+s[j]+s[i+1:j]+c+s[j+1:])
        
        return int(res)
