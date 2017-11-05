# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#   	self.val = x
#     self.left = None
#     self.right = None

class Solution(object):
    # append doesn't return a new list 
    # so we can't do first.append(root.val) + second
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
			
	first = Solution.inorderTraversal(self, root.left)
	first.append(root.val)
	second = Solution.inorderTraversal(self, root.right)
        return first + second

    def inorder_short(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
			
        return Solution.inorder_short(self, root.left) + [root.val] + Solution.inorder_short(self, root.right)
