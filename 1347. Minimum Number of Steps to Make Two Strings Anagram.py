'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
'''

'''
Intuition
The idea is to compare the character counts in both strings to determine the number of steps required to make them anagrams. We can achieve this by counting the occurrences of each character in both strings and then calculating the absolute differences in counts.
Approach
1. Initialize two arrays count_s and count_t of size 26 to represent the count of each character in the alphabet for both strings s and t.
2. Iterate through each character in string s and increment the corresponding count in count_s.
3. Iterate through each character in string t and increment the corresponding count in count_t.
4. Calculate the absolute differences in counts for each character and sum them up to get the total number of steps.
5. Return the total number of steps divided by 2 since each step involves changing one character, and we count each change twice.
Complexity
Time complexity:
O(n)O(n)O(n), where n is the length of the input strings s and t. We iterate through each character in both strings once.
Space complexity:
O(1)O(1)O(1), since the size of the arrays count_s and count_t is constant (26 characters).
'''


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            count_s[ord(char) - ord('a')] += 1

        for char in t:
            count_t[ord(char) - ord('a')] += 1

        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])

        return steps // 2
