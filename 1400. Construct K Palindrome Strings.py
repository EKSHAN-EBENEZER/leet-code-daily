'''
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105
'''














class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        sorted_s = sorted(s)
        
        odd_count = 0
        i = 0
        
        while i < len(sorted_s):
            char = sorted_s[i]
            count = 0
            while i < len(sorted_s) and sorted_s[i] == char:
                count += 1
                i += 1
            if count % 2 == 1:
                odd_count += 1
        
        return odd_count <= k
