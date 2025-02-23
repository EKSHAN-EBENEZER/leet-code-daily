'''
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''






class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        index = [0] 
        return self.construct(pre, post, index, 0, len(pre) - 1)

    def construct(self, pre, post, index, l, h):
        if index[0] >= len(pre) or l > h:
            return None

        root = TreeNode(pre[index[0]])
        index[0] += 1
        if l == h:
            return root

        i = l
        while i <= h and post[i] != pre[index[0]]:
            i += 1

        if i <= h:
            root.left = self.construct(pre, post, index, l, i)
            root.right = self.construct(pre, post, index, i + 1, h - 1)

        return root
