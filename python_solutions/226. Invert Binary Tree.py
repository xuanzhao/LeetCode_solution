# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(root):
	"""
	:type root: TreeNode
	:rtype: TreeNode
	"""
	
	def loop(root):
	
		if root.left or root.right:
			root.left, root.right = root.right, root.left
	
		if root.left:
			loop(root.left)
		elif root.right:
			loop(root.right)
	
	if not root: return 
	elif root.left == None and root.right == None: return root
	loop(root)
	return root


