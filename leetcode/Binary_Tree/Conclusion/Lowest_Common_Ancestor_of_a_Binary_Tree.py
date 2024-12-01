# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def helper(node: "TreeNode"):
            # 終点
            if not node:
                return None

            if node == q or node == p:
                return node

            left_val = helper(node.left)
            right_val = helper(node.right)

            if left_val and right_val:
                return node

            return left_val if left_val else right_val

        return helper(root)
