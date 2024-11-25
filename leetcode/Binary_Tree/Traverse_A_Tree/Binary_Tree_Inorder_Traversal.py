# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# deal inorder traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, result):
            if not node:
                return
            helper(node.left, result)
            result.append(node.val)
            helper(node.right, result)

            return result

        result = []
        helper(root, result)

        return result
