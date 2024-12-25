# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def tr(r1,r2):
            if not r1 and not r2:
                return None
            if r1 and r2:
                root=TreeNode(r1.val+r2.val)
                root.left=tr(r1.left,r2.left)
                root.right=tr(r1.right,r2.right)
            elif r1:
                root=TreeNode(r1.val)
                root.left=tr(r1.left,r2)
                root.right=tr(r1.right,r2)
            elif r2:
                root=TreeNode(r2.val)
                root.left=tr(r1,r2.left)
                root.right=tr(r1,r2.right)
            return root
        return tr(root1,root2)
        