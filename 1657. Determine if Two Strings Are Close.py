'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
'''

'''
Approaches
(Also explained in the code)

Frequency Counting:

Two vectors (freq1 and freq2) are used to count the frequency of each letter in word1 and word2.
freq1[i] stores the count of the i-th letter in the English alphabet in word1, and similarly for freq2.
Checking Presence of Characters:

Iterate over each character in the alphabet.
If a character is present in one word and not in the other (or vice versa), return false.
This ensures that both words contain the same set of characters.
Sorting Frequencies:

Sort the frequency vectors (freq1 and freq2).
This step is necessary because the order of frequencies doesn't matter, only their values.
Comparing Sorted Frequencies:

Iterate through the sorted frequency vectors and compare corresponding elements.
If any corresponding elements are not equal, return false.
Final Result:

If all the checks pass, return true, indicating that the two words are "close" as per the problem definition.
Complexity
Time complexity:
O(n)O(n)O(n)
(Sorting on a constant Array (n=26) does not affect the time complexity of the algorithm)

Space complexity:
O(1)O(1)O(1)
'''



class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True
