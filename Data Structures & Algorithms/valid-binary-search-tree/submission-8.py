# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.bst(-1000000000, root,1000000000 )

    
    def bst(self, left, node, right) -> bool:

        if not node:
            return True
        if left >= node.val or right <= node.val:
            return False
        
        return(self.bst(left,node.left, node.val) 
            and self.bst( node.val,node.right,right))


node = TreeNode(5, TreeNode(3), TreeNode(8))
print(Solution().isValidBST(node))  
 


        