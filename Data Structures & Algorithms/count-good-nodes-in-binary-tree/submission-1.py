# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return(self.good_nodes_path(root, root.val))


    

    def good_nodes_path(self, root: TreeNode, path_max: int ) -> int:
        res = 0
        if not root:
            return 0 
        
        if root.val >= path_max:
            res += 1
            path_max = root.val
        
        return (res + self.good_nodes_path(root.left, path_max)  
                    + self.good_nodes_path(root.right, path_max))