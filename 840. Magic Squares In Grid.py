'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
'''




class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            once=[False]*10
            rowSum=[0]*3
            colSum= [0]*3

            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    x= grid[a][b]
                    if x < 1 or x > 9: return False
                    rowSum[a-i+1] += x
                    colSum[b-j+1] += x
                    if once[x]: 
                        return False 
                    once[x]=True

            for b in once[1:]: 
                if not b: return False

            for sum in rowSum:
                if sum!=15: return False
            for sum in colSum:
                if sum!=15: return False
            
            return grid[i-1][j-1]+grid[i+1][j+1]==10 and grid[i+1][j-1]+grid[i-1][j+1]==10
        
        r, c = len(grid), len(grid[0])
        if r < 3 or c < 3: 
            return 0

        cnt=0
        for i in range(1, r-1):
            for j in range(1, c-1):
                if grid[i][j] == 5 and isMagic(i, j): 
                    cnt+=1
        return cnt



        
