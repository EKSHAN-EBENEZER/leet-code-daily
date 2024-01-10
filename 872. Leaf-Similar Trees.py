'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1 = self.getSequence(root1)
        s2 = self.getSequence(root2)
        if len(s1) != len(s2):
            return False
        return all(a == b for a, b in zip(s1, s2))

    def getSequence(self, root: TreeNode):
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(root.val)
            return
        self.dfs(root.left, result)
        self.dfs(root.right, result)

