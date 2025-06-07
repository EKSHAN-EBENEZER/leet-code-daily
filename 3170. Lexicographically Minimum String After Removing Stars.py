'''
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.
'''






class Solution:
    def clearStars(self, s: str) -> str:
        from collections import defaultdict

        freq = defaultdict(list)
        a_ord = ord('a')

        for i, ch in enumerate(s):
            if ch == '*':
                for j in range(26):
                    if freq[chr(a_ord + j)]:
                        freq[chr(a_ord + j)].pop()
                        break
            else:
                freq[ch].append(i)

        keep = [False] * len(s)
        for indices in freq.values():
            for idx in indices:
                keep[idx] = True

        return ''.join(s[i] for i in range(len(s)) if keep[i])
