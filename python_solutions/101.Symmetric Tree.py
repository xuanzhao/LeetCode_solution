# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def loop(curr_left, curr_right):

        if curr_left == None and curr_right == None: return True
        if curr_left == None or curr_right == None: return False

        return (curr_left.val == curr_right.val) and
                loop(curr_left.right, curr_right.left) and
                  loop(curr_left.left, curr_right.right)


    return loop(root,root)


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    nodes = []
    nodes.append(root)
    nodes.append(root)

    while(nodes != []):
        t2 = nodes.pop()
        t1 = nodes.pop()
        if (t1 == None and t2 == None): return continue
        if (t1 == None or t2 == None): return False
        if (t1.val != t2.val): return False
        nodes.append(t1.left)
        nodes.append(t2.right)
        nodes.append(t1.right)
        nodes.append(t2.left)

    return True



