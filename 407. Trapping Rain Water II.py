'''
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
'''





import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        minHeap = []

        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(minHeap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                if not visited[i][j]:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        waterTrapped = 0

        while minHeap:
            height, x, y = heapq.heappop(minHeap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    waterTrapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return waterTrapped
