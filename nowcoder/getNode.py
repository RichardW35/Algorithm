 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.parent = None
         self.left = None
         self.right = None

/*获取后继节点*/

class solutuion:
          def getrightNone(self,node):
                    if node == None:
                              return
                    if node.right == None:
                              return getLeftMost(node)
                    else:
                              parent = node.parent
                              while parent != None and parent.left != node:
                                        node = parent
                                        parent = node.parent
                              return parent
          def getLeftMost(self,node):
                    if node == None:
                              return
                    while node != None:
                              node = node.left
                    return node
                    
