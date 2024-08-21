'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''




class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def f(i, j):
            if i==j: return 1
            if s[i]==s[j]: return f(i, j-1)
            ans=f(i, j-1)+1
            k=i+1
            while k<j-1:
                if s[k]==s[j]:
                    ans=min(ans, f(i, k-1)+f(k, j-1))
                    k+=1
                k+=1
            return ans

        s=[c for c, _ in groupby(s)]
        return f(0, len(s)-1)
        
