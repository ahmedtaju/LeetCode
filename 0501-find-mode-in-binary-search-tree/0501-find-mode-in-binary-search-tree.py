# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs( node, cnt_dict):
            if not node: return 
            cnt_dict[node.val] += 1
            dfs(node.left, cnt_dict)
            dfs(node.right, cnt_dict)

        cnt_dict = defaultdict(int)
        dfs(root, cnt_dict)
        mode, res = max(cnt_dict.values()), []
        for k in cnt_dict: 
            if cnt_dict[k] == mode: res.append(k)
        return res 
