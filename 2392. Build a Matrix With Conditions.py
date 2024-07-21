'''
You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

 

Example 1:


Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
Example 2:

Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
 

Constraints:

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 104
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
'''




class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order1 = self.generate_topological_sort(rowConditions, k)
        order2 = self.generate_topological_sort(colConditions, k)
        
        if len(order1) < k or len(order2) < k:
            return []
        
        m = {order2[i]: i for i in range(k)}
        ans = [[0] * k for _ in range(k)]
        
        for i in range(k):
            ans[i][m[order1[i]]] = order1[i]
        
        return ans

    def generate_topological_sort(self, A: List[List[int]], k: int) -> List[int]:
        deg = [0] * k
        order = []
        graph = defaultdict(list)
        q = deque()
        
        for c in A:
            graph[c[0] - 1].append(c[1] - 1)
            deg[c[1] - 1] += 1
        
        for i in range(k):
            if deg[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            order.append(x + 1)
            for y in graph[x]:
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)
        
        return order
