'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
'''


'''
Approaches
(Also explained in the code)

Initialization: Initialize a 2D vector dp to store the minimum falling path sum for each cell. Initialize ans to INT_MAX as the result.

Base Cases: If the matrix has only one row or one column, return the only element in the matrix as the minimum falling path sum.

Iterative Over First Row: Iterate over the elements in the first row of the matrix and find the minimum falling path sum by calling a recursive function minFallingPathSum for each element.

Recursive Function: The minFallingPathSum function calculates the minimum falling path sum recursively. It uses memoization to avoid redundant calculations. If the result for a particular cell is already calculated, it is directly returned from the memoized table.

Dynamic Programming: For each cell, calculate the minimum falling path sum considering three possible directions: left, straight, and right. Update the memoized table with the minimum sum.

Return Result: Return the minimum falling path sum obtained from iterating over the first row.

Complexity
Time complexity:
O(m∗n)O(m*n)O(m∗n)

Space complexity:
O(m∗n)O(m*n)O(m∗n)
'''


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        if m == 1 or n == 1:
            return A[0][0]

        dp = [[float('inf')] * n for _ in range(m)]
        ans = float('inf')

        for i in range(len(A)):
            ans = min(ans, self.minFallingPathSumHelper(A, 0, i, dp))

        return ans

    def minFallingPathSumHelper(self, A, row, col, dp):
        m, n = len(A), len(A[0])

        if dp[row][col] != float('inf'):
            return dp[row][col]

        if row == m - 1:
            return A[row][col]

        left = right = float('inf')

        if col > 0:
            left = self.minFallingPathSumHelper(A, row + 1, col - 1, dp)

        straight = self.minFallingPathSumHelper(A, row + 1, col, dp)

        if col < n - 1:
            right = self.minFallingPathSumHelper(A, row + 1, col + 1, dp)

        dp[row][col] = min(left, min(straight, right)) + A[row][col]

        return dp[row][col]

