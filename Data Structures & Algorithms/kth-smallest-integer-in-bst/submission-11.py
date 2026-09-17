# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            k -= 1
            cur = stack.pop()
            if k == 0:
                return cur.val
            cur = cur.right

                

