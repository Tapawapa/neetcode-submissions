# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #do something
        
        if p is None and q is None:
            return True
        if q is None:
            return False
        if p is None:
            return False
        if q.val != p.val:
            return False
        
        left_call = self.isSameTree(p.left, q.left)
        right_call = self.isSameTree(p.right, q.right)

        return left_call and right_call
        
  