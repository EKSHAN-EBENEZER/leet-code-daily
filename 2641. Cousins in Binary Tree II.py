'''
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104
'''






class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])
        level_sum = []

        while q:
            level_size = len(q)
            level_total = 0
            for _ in range(level_size):
                node = q.popleft()
                level_total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(level_total)

        q.append(root)
        root.val = 0
        level = 0

        while q:
            level_size = len(q)
            next_level_sum = level_sum[level + 1] if level + 1 < len(level_sum) else 0

            for _ in range(level_size):
                node = q.popleft()
                child_sum = 0

                if node.left:
                    child_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    child_sum += node.right.val
                    q.append(node.right)

                if node.left:
                    node.left.val = next_level_sum - child_sum
                if node.right:
                    node.right.val = next_level_sum - child_sum

            level += 1

        return root
