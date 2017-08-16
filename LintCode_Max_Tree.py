class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution(object):
    """ Stack. 单调递减栈.
    For each new node, all the nodes in the stack occurs before him.
    The deepest node < him is his left node.
    The first node > him is his parent (he is the right child).
    """
    def maxTree(self, nums):
        """
        :param list nums: a list of numbers
        :return Node: root of max tree
        """
        stack = []
        for num in nums:
            new_node = TreeNode(num)
            while stack and new_node.val >= stack[-1].val:
                new_node.left = stack.pop()
            if stack:
                stack[-1].right = new_node
            stack.append(new_node)
        return stack[0] if stack else None

    def printNodes(self, nodes):
        print ' '.join([str(node.val) if node else 'None' for node in nodes])
        print '\n'

    def printTree(self, root):
        if not root:
            print 'Empty Tree'
            return
        queue = [root]
        while queue:
            self.printNodes(queue)
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)

root = Solution().maxTree([])
Solution().printTree(root)
root = Solution().maxTree([2, 3, 6, 0, 3, 9])
Solution().printTree(root)
root = Solution().maxTree([2, 3, 6, 0, 3, 9, 4, 2, 3, 7])
Solution().printTree(root)
