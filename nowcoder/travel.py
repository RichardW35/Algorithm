class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solutuion:
    def preOrder(self, root):
        if root != None:
            stack = [root]
            while len(stack) > 0:
                node = stack.pop()
                print(node.val)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)

    def midOrder(self, root):
        if root != None:
            stack = []
            while len(stack) > 0 or root != None:
                if root != None:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    print(root.val)
                    root = root.right

    def posOrder(self, root):
        if root != None:
            stack1 = [root]
            stack2 = []
            while len(stack1) > 0:
                node = stack1.pop()
                stack2.append(node)
                if node.left != None:
                    stack1.append(node.left)
                if node.right != None:
                    stack2, append(node.right)
            while len(stack2) > 0:
                print(stack2.pop().val)
