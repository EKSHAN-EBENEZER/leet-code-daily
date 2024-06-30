'''
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
'''





class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        auf = UnionFind(n)
        buf = UnionFind(n)
        res = 0
        for edge in edges:
            if edge[0] == 3:
                if auf.union(edge[1], edge[2]) == 1:
                    buf.union(edge[1], edge[2])
                    res += 1
            if auf.is_connected() and buf.is_connected():
                return len(edges) - res
        for edge in edges:
            if edge[0] == 1:
                res += auf.union(edge[1], edge[2])
            if edge[0] == 2:
                res += buf.union(edge[1], edge[2])
            if auf.is_connected() and buf.is_connected():
                return len(edges) - res
        return -1

class UnionFind:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.node_count = n
    def find(self, x):
        if self.parent[x] == 0 or self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 0
        self.parent[py] = px
        self.node_count -= 1
        return 1
    def is_connected(self):
        return self.node_count == 1
