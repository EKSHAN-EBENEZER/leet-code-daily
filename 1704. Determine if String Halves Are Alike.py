'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
'''



'''
Intuition
The problem involves counting the number of vowels in two halves of a string. A straightforward approach is to iterate through each character in both halves and count the vowels. Afterward, compare the counts to determine if the halves are alike.
Approach
1. Define a helper function count_vowels to count the number of vowels in a given string.
2. Compute the length of the input string and find the midpoint.
3. Split the string into two halves: the first half (first_half) and the second half (second_half).
4. Use the count_vowels function to count the vowels in both halves.
5. Compare the counts of vowels in both halves. If they are equal, return True; otherwise, return False.
Complexity
Time complexity:
O(n)O(n)O(n), where nnn is the length of the input string. The function iterates through each character in the two halves to count the vowels.
Space complexity:
O(1)O(1)O(1), as the additional space used is constant, regardless of the input size.
'''


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            vowels = set('aeiouAEIOU')
            return sum(1 for char in string if char in vowels)

        length = len(s)
        mid_point = length // 2

        first_half = s[:mid_point]
        second_half = s[mid_point:]

        return count_vowels(first_half) == count_vowels(second_half)
