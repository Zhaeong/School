class BTNode:
    '''A generic binary tree node that keeps a value and pointers to
    a left child, right child and parent.'''

    def __init__(self, v, p=None):
        '''(BTNode, object, BTNode) -> NoneType
        A new BTNode with value v, no left or right
        children and parent p. p is None by default.'''

        self.value = v
        self.parent = p
        self.left = None
        self.right = None

    def __str__(self):
        '''(BTNode) -> str
        Return the string representation of self.
        This method is called by print() and str()
        NOTE: This method is complete.'''

        return str(self.value)

    def __repr__(self):
        '''(BTNode) -> str
        Return the internal string representation of self.
        This method is called when a list of BTNodes is
        printed.
        NOTE: This method is complete.'''

        return "BTNode: {}".format(self.value)

    def set_right(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the right child of self.
        Set bidirectional links correctly.'''

        self.right = n
        n.parent = self

    def set_left(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the left child of self.
        Set bidirectional links correctly.'''

        self.left = n
        n.parent = self

    def is_left_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self is
        the left child of its parent.'''
        
        if self.parent != None and self.parent.left == self:
            return True
        else:
            return False


    def is_right_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self is
        the right child of its parent.'''
        
        if self.parent != None and self.parent.right == self:
            return True
        else:
            return False


    def is_leaf(self):
        '''(BTNode) -> bool
        Return True iff self is a leaf node.'''
        if self.left == None and self.right == None:
            return True
        else:
            return False


    def height(self):
        '''(BTNode) -> int
        Return the height of self. Height is defined as the length of the
        longest path by number of nodes from self to a leaf.
        The height of a leaf node is 1.'''

        if not self.left and not self.right:
            return 1
        elif not self.left:
            return self.right.height() + 1
        elif not self.right:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1

    def depth(self):
        '''(BTNode) -> int
        Return the depth of self. Depth is defined as the length of the
        path by number of nodes from the root of the tree to self.
        The depth of a root node is 1.'''
        
        if not self.parent:
            return 1
        else:
            return self.parent.depth() + 1



class BSTree:
    '''A Binary Search Tree that conforms to the BST property at every step.
    The BST property states that for every node with value k, its left child
    is a (possibly empty) BST with values strictly less than k and its right
    child is a (possibly empty) BST with values strictly greater than k.'''

    def __init__(self, root=None):
        '''(BSTree, BTNode) -> NoneType
        Create a new BST with an optional root.
        NOTE: This method is complete.'''

        self.root = root

    def print_tree(self):
        '''(BSTree) -> NoneType
        Print tree recursively (used for testing purposes)
        NOTE: This method is complete.'''

        _print_tree(self.root, 1)

    def insert(self, v):
        '''(BSTree, object) -> NoneType
        Insert a new node with value v into self. Do not duplicate values.
        NOTE: This method is complete.'''

        if not self.root:
            self.root = BTNode(v)
            return
        _insert(self.root, v)

    def height(self):
        '''(BSTree) -> int
        Return the height of this tree.'''

        if not self.root:
            return 0
        else:
            return self.root.height()

    def search(self, v):
        '''(BSTree, object) -> BTNode
        Return BTNode with value v if it exists in the tree. Return None if no
        such node exists. Assume unique node values.
        NOTE: This method is complete.'''

        return _search(self.root, v)

    def range(self, v_start, v_end):
        '''(BSTree, object, object) -> list
        Return a list of Node objects with values between v_start and
        v_end inclusive. Assume v_start and v_end can be ordered and
        v_start <= v_end. v_start and v_end may not be values that
        exist in the tree.
        NOTE: This method is complete.'''

        return _range(self.root, v_start, v_end)

    def delete(self, v):
        '''(BSTree, object) -> NoneType
        Delete node with value v from self. Change root if required.
        NOTE: This method is complete.'''

        self.root = _delete(self.root, v)


## HELPER RECURSIVE FUNCTIONS

def _print_tree(root, depth):
    '''(BTNode, int) -> NoneType
    Print the left subtree of root, print root preceded by four spaces for
    every unit of depth, then print the right subtree of root.
    depth is the depth of root.
    NOTE: This function is complete.'''

    if root is None:
        return
    _print_tree(root.right, depth + 1)
    print("    " * (depth - 1) + str(root))
    _print_tree(root.left, depth + 1)


def _insert(root, v):
    '''(BTNode, obj) -> NoneType
    Insert a new node with value v into BST rooted at root.
    Do not allow duplicates.
    NOTE: This function is complete.'''

    if root.value == v:
        return
    if v < root.value:
        if root.left:
            _insert(root.left, v)
        else:
            root.set_left(BTNode(v))
    elif v > root.value:
        if root.right:
            _insert(root.right, v)
        else:
            root.set_right(BTNode(v))


def _search(root, v):
    '''(BTNode, object) -> BTNode
    Return BTNode with value v if it exists in subtree rooted at
    root. Return None if no such BTNode exists.'''
    if root == None:
        return None
    elif root.value == v:
        return root
    elif v < root.value and root.left != None:
        return _search(root.left, v)
    elif v > root.value and root.right != None:
        return _search(root.right, v)
    else:
        return None


def _range(root, v_start, v_end):
    '''(BTNode, int, int) -> list
    Return an in-order list of BTNodes that have values between
    v_start and v_end, inclusive in subtree rooted at root.'''
    
    if root == None:
        return []

    elif root.left != None and root.left.value < v_start and \
    root.right != None and root.right.value > v_end:
        return [root]

    elif root.left == None and root.right == None and \
    root.value >= v_start and root.value <= v_end:
        return [root]

    else:
        return _range(root.left, v_start, v_end) + \
    _isintree(root, v_start, v_end) + _range(root.right, v_start, v_end)
    
def _isintree(val, v_start, v_end):
    '''(BTNode, int,int) -> list
    Returns the BTNode in a list if the value of the BTNode is between 
    v_start and v_end'''

    if val.value >= v_start and val.value <= v_end:
        return [val]
    else:
        return []


def _delete(root, v):
    '''(BTNode, object) -> BTNode
    Delete BTNode with value v from subtree rooted at root.
    Return root of subtree. Do nothing if value doesn't exist in subtree.'''
    if root == None:
        return
    
    if root.value > v and root.left != None:
        return _delete(root.left, v)

    elif root.value < v and root.right != None:
        return _delete(root.right, v)
    
    elif root.value != v:
        return _stemnode(root)

    else:
        if root.is_leaf and root.parent == None and root.value != v:
            return root
        
        if root.right == None and root.left == None and \
        root.parent == None and root.value == v:
            return       
        
        elif root.is_leaf():
    
            if root.parent.left == root:
                root.parent.left = None
                return _stemnode(root)
               
            elif root.parent.right == root:
                root.parent.right = None
                rootnode = root
                return _stemnode(root)
        
        elif root.left != None and root.right == None:
            if root.is_left_child and root.parent != None:
                root.parent.set_left(root.left)
                root.left = None
                return _stemnode(root)
            elif root.is_right_child and root.parent != None:
                root.parent.set_right(root.left)
                root.left = None
                return _stemnode(root)
            else:
                leftnode = root.left
                root.left = None
                return leftnode
                
        elif root.left == None and root.right != None:
            if root.is_right_child and root.parent != None:
                root.parent.set_right(root.right)
                root.right = None
                return _stemnode(root)
            elif root.is_left_child and root.parent != None:
                root.parent.set_left(root.right)
                root.right = None
                return _stemnode(root)
            else:
                rightnode = root.right
                root.right = None
                return rightnode            
        
        elif root.left and root.right:
            if root.left.height() > root.right.height():
                in_pre = in_order_predecessor(root)
                if root.parent != None and root.parent.left == root:
                    root.parent.set_left(in_pre)
                if root.parent != None and root.parent.right == root:
                    root.parent.set_right(in_pre)  
                    
                if root.left != in_pre: 
                    in_pre.set_left(root.left)
                if root.right != in_pre: 
                    in_pre.set_right(root.right)
                in_pre.parent = root.parent
                root.left = None
                root.right = None
                root.parent = None
                return _stemnode(in_pre)
            
            elif root.left.height() <= root.right.height():
                in_succ = in_order_successor(root)

                if root.parent != None and root.parent.left == root:
                    root.parent.set_left(in_succ)

                if root.parent != None and root.parent.right == root:
                    root.parent.set_right(in_succ)

                if root.left != in_succ: 
                    in_succ.set_left(root.left)
                if root.right != in_succ:
                    in_succ.set_right(root.right)
                    
                in_succ.parent = root.parent
                root.left = None
                root.right = None
                root.parent = None
                return _stemnode(in_succ)
            
def _stemnode(node):
    '''(BTNode) -> (BTNode)
    Takes a node and returns the stem of the node'''
    rootnode = node
    while rootnode.parent != None:
        rootnode = rootnode.parent
    return rootnode    
        

## NEIGHBOURS FUNCTIONS


def in_order_predecessor(node):
    '''(BTNode) -> BTNode
    Return the in-order predecessor of node.
    Return None if node is leftmost.'''

    if node.left != None:
        leftnode = node.left
        while leftnode.right != None:
            leftnode = leftnode.right
        return leftnode
    if node.left == None:
        parent = node.parent
        if parent.right == node:
            return parent
        while parent.parent.right != parent:
            parent = parent.parent
            if parent.parent == None:
                return None
        return parent.parent


def in_order_successor(node):
    '''(BTNode) -> BTNode
    Return the in-order successor of node.
    Return None if node is rightmost.'''
    
    if node.right != None:
        rightnode = node.right
        while rightnode.left != None:
            rightnode = rightnode.left
        return rightnode
    if node.right == None:
        parent = node.parent
        if parent.left == node:
            return parent
        while parent.parent.left != parent:
            parent = parent.parent
            if parent.parent == None:
                return None
        return parent.parent
        


if __name__ == '__main__':
    tree = BSTree()
    for val in [14,2,3,7,1,17,22,20,23]:
        tree.insert(val)
    #tree.print_tree()

    #x = tree.root
    #y = _delete(x, 1)
    #tree.print_tree()
    #tree.delete(14)
    #tree.print_tree()
    tree.delete(14)
    tree.print_tree()   
    
    tree2 = BSTree()
    for val in [5, 4, 3, 2, 1]:
        tree2.insert(val)    
    tree2.print_tree()
    tree2.delete(0)
    #tree2 = BSTree()
    #tree2.insert(2)
    #tree2.delete(0)

    