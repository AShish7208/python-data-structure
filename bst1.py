class BstNode:
    def __init__(self,key,value):
        self.key =key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self,key,value):
        if self is None:
            node = BstNode(key,value)
        elif key < node.key:
            node.left = BstNode.insert(node.left,key,value)
            node.left.parent = node
        elif key > node.key:
            node.right = BstNode.insert(node.right,key,value)
            node.right.parent = node
        return node
    def find(self,key):
        if self is None:
            return None
        if key == node.key:
            return node
        if key< node.key:
            return find(node.left,key)
        if key> node.key:
            return find(node.right,key)


    def update(self,key,value):
        target = BstNode.find(self,key)
        if target is not None:
            target.value = value


    def list_all(self):
        if self is None:
            return []
        return BstNode.list_all(self.left)+[self.key,self.value]+BstNode.list_all(self.right)
        
    def is_balanced(self):
        if self is None:
            return True,0
        balanced_l,height_l = BstNode.is_balanced(self.left)
        balanced_r,height_r = BstNode.is_balanced(self.right)

        balanced = balanced_l and balanced_r and abs(height_l - height_r)<=1
        height = 1+max(height_l,height_r)
        return balanced,height


    def make_balanced_bst(data,lo = 0, hi = None,parent= None):
        if hi is None :
            hi = len(data -1)

        if lo>hi:
            return None

        mid = lo+(hi-lo)//2
        key,value = data[mid]
        root = BstNode(key,value)
        root.parent = parent
        root.left = make_balanced_bst(data,lo,mid-1,root)
        root.right = make_balanced_bst(data,lo,mid+1,root)

        return root


    
