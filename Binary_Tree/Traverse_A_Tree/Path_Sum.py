# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)  # ルートノード
root.left = TreeNode(2)  # 左の子
root.right = TreeNode(3)  # 右の子
root.left.left = TreeNode(4)  # 左の左の子
root.left.right = TreeNode(5)  # 左の右の子

hoge = Solution()

hoge.hasPathSum(root, 5)
