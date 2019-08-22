class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SerializeAndReconstructTree:
    def preSerialize(self, head):
        if head == None:
            return "#!"
        str = head.val + '!'
        str = str + preSerialize(head.left)
        str = str + preSerialize(head.right)
        return str

    def reconByPreString(self, arr):
        new_arr = arr.split('!')
        return reconPreOrder(new_arr)

    def reconPreOrder(self, arr):
        value = arr.pop(0)
        if value == '#':
            return None
        root = TreeNode(value)
        root.left = reconPreOrder(arr)
        root.right = reconPreOrder(arr)
        return root

    def serializeBylevel(self, head):
        if head == None:
            return "#!"
        res = head.val + "!"
        arr = [head]
        while arr != None:
            node = arr.pop(0)
            if node.left != None:
                res = res + node.left.val + '!'
                arr.append(node.left)
            else:
                res += '#!'
            if node.right != None:
                res = res + node.right.val + '!'
                arr.append(node.right)
            else:
                res += '#!'
        return res
