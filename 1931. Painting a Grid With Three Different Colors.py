'''
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''






class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def dfs(pos, prev_color, mask):
            if pos == m:
                states.append(mask)
                return
            for color in range(3):
                if color != prev_color:
                    dfs(pos + 1, color, mask * 3 + color)

        MOD, states = 10**9 + 7, []
        dfs(0, -1, 0)
        S = len(states)
        compat = [[] for _ in range(S)]
        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                x, y = s1, s2
                ok = True
                for _ in range(m):
                    if x % 3 == y % 3:
                        ok = False
                        break
                    x //= 3
                    y //= 3
                if ok:  compat[i].append(j)
        dp = [1] * S
        for _ in range(n - 1):
            new_dp = [0] * S
            for i in range(S):
                if dp[i]:
                    for j in compat[i]:
                        new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD 
