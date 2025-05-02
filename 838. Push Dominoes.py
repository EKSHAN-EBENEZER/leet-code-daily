'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
'''








class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        last_right = -1
        last_left = 0

        for i, d in enumerate(dominoes):
            if d == 'R':
                if last_right != -1:
                    for j in range(last_right + 1, i):
                        dominoes[j] = 'R'
                last_right = i
            elif d == 'L':
                if last_right != -1:
                    l, r = last_right + 1, i - 1
                    while l < r:
                        dominoes[l], dominoes[r] = 'R', 'L'
                        l += 1
                        r -= 1
                    last_right = -1
                else:
                    for j in range(last_left, i):
                        dominoes[j] = 'L'
                last_left = i

        if last_right != -1:
            for i in range(last_right + 1, n):
                dominoes[i] = 'R'

        return ''.join(dominoes)
