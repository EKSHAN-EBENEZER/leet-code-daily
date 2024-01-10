'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.
'''
'''
Intution
The key to solving this problem is to consider the binary tree as an undirected graph, where an edge exists between parent and child nodes.
Perform a breadth-first search (BFS) starting from the start node since BFS processes nodes level by level, which naturally aligns with the passage of minutes as the infection spreads.
Approach
Graph Construction:
The solution creates a graph representation of the tree using a default dictionary g of lists in the dfs (Depth-First Search) function.

def dfs(root):
    if root is None:
        return
    if root.left:
        g[root.val].append(root.left.val)
        g[root.left.val].append(root.val)
    if root.right:
        g[root.val].append(root.right.val)
        g[root.right.val].append(root.val)
    dfs(root.left)
    dfs(root.right)
Initialization:

Initialize an empty set vis to keep track of visited nodes (infected nodes) and a queue q to maintain the BFS's order of node processing, with the start node as the initial node to be processed.
vis = set()
q = deque([start])
BFS Algorithm:

The solution sets up a while loop that continues until the queue q is empty, signifying that there are no more nodes to be infected.
ans = -1
while q:
    ans += 1
    for _ in range(len(q)):
        i = q.popleft()
        vis.add(i)
        for j in g[i]:
            if j not in vis:
                q.append(j)
Inside the loop, ans is incremented to count the minutes.
For each iteration of the while loop, it processes all nodes currently in the queue, which are the nodes that got infected in the previous minute.
It pops each node from the queue, adds it to the vis set, and then iterates over its adjacent nodes. If any adjacent node has not been visited (infected), it is added to the queue to be processed in the next minute.
Return Value:

By the end of the BFS loop, ans holds the number of minutes it took to infect the entire tree since each loop iteration represents one minute of infection time passing.
The return value ans represents the required number of minutes for the infection to spread through the entire tree, as determined by our BFS algorithm.
return ans
Complexity
Time complexity: The time complexity of the provided code is O(N) where N is the number of nodes in the tree
Space complexity: The space complexity of the code is also O(N)
'''


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time
