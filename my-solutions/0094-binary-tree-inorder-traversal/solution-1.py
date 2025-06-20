# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        def get_val(root):

            if not root:
                return
            
            get_val(root.left)
            lst.append(root.val)
            get_val(root.right)
    
        lst = []
        get_val(root)

        return lst
        