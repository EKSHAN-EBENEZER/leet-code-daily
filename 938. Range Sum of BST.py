'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
'''

'''
Intuition
The problem requires finding the sum of values of all nodes in a binary search tree (BST) that fall within a specified range. Since it's a BST, we can take advantage of its properties to efficiently identify the nodes within the given range.
Approach
To solve this problem, we can perform a depth-first search (DFS) traversal of the BST. At each node, we check whether its value falls within the specified range [low, high]. If the current node's value is within the range, we include it in the sum. We then recursively traverse the left and right subtrees.
The algorithm follows these steps:
1. If the current node is null, return 0.
2. If the current node's value is within the range [low, high], include it in the sum; otherwise, exclude it.
3. Recursively calculate the sum for the left subtree and the sum for the right subtree.
4. Return the sum of the current node, left subtree sum, and right subtree sum.
Complexity
Time complexity:
O(n)O(n)O(n), where n is the number of nodes in the tree. In the worst case, we may need to visit all nodes in the tree.
Space complexity:
O(h)O(h)O(h), where h is the height of the tree. This represents the maximum depth of the recursive call stack. In the worst case, for an unbalanced tree, the space complexity can be O(n)O(n)O(n), but for a balanced tree, it is O(logn)O(log n)O(logn).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)
