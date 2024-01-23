'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
'''


'''
Approach 1: Bit Operation
Intuition:
The idea is to use bit manipulation to represent the presence of characters in a string.
We use an integer to represent a set of characters where each bit corresponds to the presence of a character.
By using bitwise operations, we can efficiently check for duplicate characters in a string.
We iterate through the given array of strings, updating our bitset and checking for uniqueness.
We maintain a dynamic programming list (dp) to store the bitsets of valid subsequences.
Approach:
Initialize dp list with a single element 0 (empty string).
For each string s in the input array:
a. Initialize variables a and dup.
b. Iterate through characters in s:
Update dup using bitwise OR to check for duplicate characters.
Update a using bitwise OR to represent the set of characters in s.
c. If dup > 0, continue to the next iteration as s has duplicate characters.
d. Iterate through dp in reverse and update it by adding new bitsets.
e. Update the result by finding the maximum length among valid subsequences.
Complexity Analysis:
Time Complexity: O(N * M), where N is the number of strings in the array and M is the maximum length of a string in the array.
Space Complexity: O(2^M), where M is the maximum length of a string. The dp list can have up to 2^M elements.
Code
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [0]
        res = 0
        
        for s in arr:
            a, dup = 0, 0
            for c in s:
                dup |= a & (1 << (ord(c) - ord('a')))
                a |= 1 << (ord(c) - ord('a'))
            
            if dup > 0:
                continue
            
            for i in range(len(dp) - 1, -1, -1):
                if (dp[i] & a) > 0:
                    continue
                dp.append(dp[i] | a)
                res = max(res, bin(dp[i] | a).count('1'))
        
        return res
Approach 2: DFS
Intuition:
The idea is to use Depth-First Search (DFS) to explore all possible combinations of strings in the array.
At each step, we concatenate a string to the existing path and check for uniqueness.
We keep track of the maximum length of valid subsequences during the DFS traversal.
Approach:
Initialize the result variable to 0.
Define a DFS function that takes the array, current path, and current index as parameters.
In the DFS function:
a. Check if the current path has unique characters using a helper function isUniqueChars.
b. If the path is unique, update the result with the maximum length.
c. If the current index is equal to the array size or the path is not unique, return.
d. Iterate through the array starting from the current index and make recursive calls to the DFS function.
Call the DFS function with the initial parameters.
Complexity Analysis:
Time Complexity: Exponential, O(2^M), where M is the maximum length of a string in the array. The DFS explores all possible combinations.
Space Complexity: O(M), where M is the maximum length of a string. The space is used for the recursive call stack.
Code
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [0]
        self.dfs(arr, "", 0, result)
        return result[0]

    def dfs(self, arr, path, idx, result):
        if self.isUniqueChars(path):
            result[0] = max(result[0], len(path))

        if idx == len(arr) or not self.isUniqueChars(path):
            return

        for i in range(idx, len(arr)):
            self.dfs(arr, path + arr[i], i + 1, result)

    def isUniqueChars(self, s):
        char_set = set()
        for c in s:
            if c in char_set:
                return False
            char_set.add(c)
        return True
Conclusion:
Both approaches aim to find the maximum length of a concatenated string with unique characters.
The bit manipulation approach uses dynamic programming to efficiently store and update valid subsequences.
The DFS approach explores all possible combinations of strings to find the maximum length.
The bit manipulation approach has a better time complexity but may require more space.
The DFS approach has a higher time complexity but consumes less space.
'''
