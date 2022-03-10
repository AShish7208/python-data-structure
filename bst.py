class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def getLeft(self):
        return self.left
    def getright(self):
        return self.right



    def preorder(root,result):
        if not root:
            return
        result.append(root.data)
        preorder(root.left,result)
        preorder(root.right,result)

    def inorder(root,result):
        if not root:
            return
        inorder(root.left,result)
        result.append(root.data)
        inorder(root.right,result)

    def postorder(root,result):
        if not root:
            return
        postorder(root.left,result)
        postorder(root.right,result)
        result.append(root.data)
        













































        
