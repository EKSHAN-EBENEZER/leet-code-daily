'''
You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

 

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1.
Example 2:

Input: grid = [[1,0,1,0],[0,1,0,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
The 1 at (1, 1) is covered by a rectangle of area 1.
The 1 at (1, 3) is covered by a rectangle of area 1.
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is either 0 or 1.
The input is generated such that there are at least three 1's in grid.
 

'''









class Solution:
    def minimumSum(self, A: List[List[int]]) -> int:
        res = float("inf")
        for _ in range(4):
            n, m = len(A), len(A[0])
            for i in range(1, n):
                a1 = self.minimumArea(A[:i])
                for j in range(1, m):
                    part2 = [row[:j] for row in A[i:]]
                    part3 = [row[j:] for row in A[i:]]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
                for i2 in range(i + 1, n):
                    part2 = A[i:i2]
                    part3 = A[i2:]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
            A = self.rotate(A)
        return res

    def minimumArea(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        n, m = len(A), len(A[0])
        left, top, right, bottom = float("inf"), float("inf"), -1, -1
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    left = min(left, j)
                    top = min(top, i)
                    right = max(right, j)
                    bottom = max(bottom, i)
        if right == -1:
            return 0
        return (right - left + 1) * (bottom - top + 1)

    def rotate(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        return [[A[i][j] for i in range(n-1, -1, -1)] for j in range(m)]
