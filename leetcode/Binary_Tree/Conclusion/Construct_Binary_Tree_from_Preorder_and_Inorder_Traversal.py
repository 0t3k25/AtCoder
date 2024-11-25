# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])  # ルートノードを取得
        idx = inorder.index(root.val)  # inorder内のルートのインデックス

        # 左右部分木を構築（preorderを正しくスライスして渡す）
        root.left = self.buildTree(preorder[1 : 1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx :], inorder[idx + 1 :])

        return root
