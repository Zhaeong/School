import unittest
from bst import *


class SampleTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''Generate a tree to test.
                9
                    8
            7
        5
            3
                2
        '''

        self.tree = BSTree()
        for val in [5, 7, 3, 2, 9, 8]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        """Verify that 5 is the root of the tree."""

        self.assertEqual(self.tree.root.value, 5)
        
        
class BTNodeTestCase(unittest.TestCase):
    '''Tests methods for BTNode class'''
    
    def setUp(self):
        '''Generate binary tree to test
                4
            3
        1
            2
        '''
        
        # make nodes
        self.root = BTNode(1)
        self.left = BTNode(2)
        self.right = BTNode(3)
        self.secondary_right = BTNode(4)
        
        # make tree
        self.root.set_left(self.left)
        self.root.set_right(self.right)
        self.right.set_right(self.secondary_right)
        
    def tearDown(self):
        '''Perform cleanup actions.'''

        pass
        
    def testSetRight(self):
        '''Verify that right child of root is set to the node with value 3
        with bi-directional link'''
        
        self.assertEqual(self.root.right, self.right)
        self.assertEqual(self.right.parent, self.root)
        
    def testSetLeft(self):
        '''Verify that left child of root is set to the node with value 2 with
        bi-directional link'''
        
        self.assertEqual(self.root.left, self.left)
        self.assertEqual(self.left.parent, self.root)
        
    def testIsLeaf(self):
        '''Verify that a leaf node is one which has no children'''
        
        self.assertTrue(self.left.is_leaf())
        self.assertFalse(self.root.is_leaf())
        self.assertFalse(self.right.is_leaf())
        self.assertTrue(self.secondary_right.is_leaf())
        
    def testIsLeftChild(self):
        '''Verify nodes who are left children are accurately detected'''
        
        self.assertFalse(self.root.is_left_child())
        self.assertTrue(self.left.is_left_child())
        self.assertFalse(self.right.is_left_child())
        self.assertFalse(self.secondary_right.is_left_child())
        
    def testIsRightChild(self):
        '''Verify nodes who are right children are accurately detected'''

        self.assertFalse(self.root.is_right_child())
        self.assertFalse(self.left.is_right_child())
        self.assertTrue(self.right.is_right_child())
        self.assertTrue(self.secondary_right.is_right_child())
        
    def testHeight(self):
        '''Verify heights of nodes are accurately calculated'''
        
        self.assertEquals(self.root.height(), 3)
        self.assertEquals(self.left.height(), 1)
        self.assertEquals(self.right.height(), 2)
        self.assertEquals(self.secondary_right.height(), 1)
        
    def testDepth(self):
        '''Verify depths of nodes are accurately calculated'''
        
        self.assertEquals(self.root.depth(), 1)
        self.assertEquals(self.left.depth(), 2)
        self.assertEquals(self.right.depth(), 2)
        self.assertEquals(self.secondary_right.depth(), 3)
        

class BSTreeEmptyTestCase(unittest.TestCase):
    '''Test BSTree methods for an empty BSTree'''
    
    def setUp(self):
        '''Create an empty BSTree'''
        
        self.tree = BSTree()
    
    def tearDown(self):
        '''Perform cleanup actions.'''

        pass
    
    def testTreeHeight(self):
        '''Verify the height of an empty tree is 0'''
        
        self.assertEquals(self.tree.height(), 0)
        
    def testSearch(self):
        '''(int) -> None, because tree is empty'''
        
        self.assertIsNone(self.tree.search(0))
        self.assertIsNone(self.tree.search(123))
        
    def testRange(self):
        '''Return empty list for any given range, because tree has no nodes'''
        
        self.assertEquals(len(self.tree.range(1, 1)), 0)
        self.assertEquals(len(self.tree.range(2, 6)), 0)
        
    def testDelete(self):
        '''Verify that attempting to delete anything from an empty tree
        maintains the tree as empty'''
        
        self.tree.delete(1)
        self.assertIsNone(self.tree.root)
        self.tree.delete(2)
        self.assertIsNone(self.tree.root)
        
        
class BSTreeSingleTestCase(unittest.TestCase):
    '''Test BSTree methods for BSTree with only one node'''
    
    def setUp(self):
        '''Create a BSTree with one node'''
        
        self.tree = BSTree()
        self.tree.insert(2)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass
    
    def testTreeHeight(self):
        '''Verify the height of tree with single node is 1'''
        
        self.assertEquals(self.tree.height(), 1)
        
    def testSearch(self):
        '''(2) -> BTNode with value 2
        Any other int value returns None'''
        
        self.assertEquals(self.tree.search(2).value, 2)
        self.assertIsNone(self.tree.search(0))
        self.assertIsNone(self.tree.search(123))
        
    def testRange(self):
        '''Verify that any range which includes root node will have a list
        with root node as the only element'''
        
        # same value, value in tree
        self.assertEquals(self.tree.range(2, 2)[0], self.tree.root)
        self.assertEquals(len(self.tree.range(2, 2)), 1)
        # values not in tree
        self.assertEquals(len(self.tree.range(0, 1)), 0)
        # right value not in tree
        self.assertEquals(self.tree.range(2, 6)[0], self.tree.root)
        self.assertEquals(len(self.tree.range(2, 6)), 1)
        # left value not in tree
        self.assertEquals(self.tree.range(0, 2)[0], self.tree.root)
        self.assertEquals(len(self.tree.range(0, 2)), 1)
        
    def testDelete(self):
        '''Verify that deleting the root will yield an empty tree, while 
        deleting anything else will leave the tree unchanged.'''
        
        # deleting nonexistent node
        self.tree.delete(0)
        self.assertEquals(self.tree.root.value, 2)
        # deleting sole existing node
        self.tree.delete(2)
        self.assertEquals(self.tree.root, None)
        
        
class BSTreeLeftTestCase(unittest.TestCase):
    '''Test BSTree methods for BSTree with only left children.'''
    
    def setUp(self):
        '''Create a BSTree with only left children:
        5
           4
              3
                 2
                    1
        '''
        
        self.tree = BSTree()
        for val in [5, 4, 3, 2, 1]:
            self.tree.insert(val)
            
    def tearDown(self):
        '''Perform cleanup actions'''
        
        pass
    
    def testTreeHeight(self):
        '''Verify the height of tree is 5'''
        
        self.assertEquals(self.tree.height(), 5)
        
    def testSearch(self):
        '''Test that BTNodes with values 5 (root), 3(internal node), and 1(leaf)
        can be retrieved by search method'''
        
        self.assertEquals(self.tree.search(5).value, 5)
        self.assertEquals(self.tree.search(3).value, 3)
        self.assertEquals(self.tree.search(1).value, 1)
        self.assertIsNone(self.tree.search(0))
        self.assertIsNone(self.tree.search(123))
        
    def testRange(self):
        '''Test range method accurately returns ordered nodes with values 
        within and inclusive of input range'''
        
        # same value, value in tree
        self.assertEquals(self.tree.range(2, 2)[0].value, 2)
        self.assertEquals(len(self.tree.range(2, 2)), 1)
        # different values, values in tree
        self.assertEquals(self.tree.range(1, 2)[0].value, 1)
        self.assertEquals(self.tree.range(1, 2)[1].value, 2)
        self.assertEquals(len(self.tree.range(1, 2)), 2)
        # neither value in tree
        self.assertEquals(len(self.tree.range(9, 10)), 0)
        # left value not in tree
        self.assertEquals(self.tree.range(0, 2)[0].value, 1)
        self.assertEquals(self.tree.range(0, 2)[1].value, 2)
        self.assertEquals(len(self.tree.range(0, 2)), 2)
        # right value not in tree
        self.assertEquals(self.tree.range(3, 10)[0].value, 3)
        self.assertEquals(self.tree.range(3, 10)[1].value, 4)
        self.assertEquals(self.tree.range(3, 10)[2].value, 5)
        self.assertEquals(len(self.tree.range(3, 10)), 3)
        
    def testNoneAndLeafDelete(self):
        '''Test delete method accurately deletes leaf node while leaving the
        rest of the tree untouched; and leaves whole tree untouched if 
        deleting non-existent node'''
        
        # deleting nonexistent node
        self.tree.delete(0)
        self.assertEquals(self.tree.root.value, 5)
        # deleting leaf node
        self.tree.delete(1)
        self.assertEquals(self.tree.root.value, 5)
        self.assertEquals(self.tree.root.left.value, 4)
        self.assertIsNone(self.tree.root.right)
        self.assertEquals(self.tree.height(), 4)
        
    def testRootDelete(self):
        '''Test delete method accurately deletes root node while maintaining
        BSTree properties'''

        self.tree.delete(5)
        self.assertEquals(self.tree.root.value, 4)
        self.assertEquals(self.tree.root.left.value, 3)
        self.assertIsNone(self.tree.root.right)
        self.assertEquals(self.tree.height(), 4)

    def testOneChildDelete(self):
        '''Test delete method accurately deletes node with one child while
        maintaining BSTree properties'''
        
        self.tree.delete(4)
        self.assertEquals(self.tree.root.value, 5)
        self.assertEquals(self.tree.root.left.value, 3)
        self.assertIsNone(self.tree.root.right)
        self.assertIsNone(self.tree.root.left.right)
        self.assertEquals(self.tree.height(), 4)
        
        
class BSTreeRightTestCase(unittest.TestCase):
    '''Test BSTree methods for BSTree with only right children.'''
    
    def setUp(self):
        '''Create a BSTree with only right children:
                    4
                3
            2
        1
        '''
        
        self.tree = BSTree()
        for val in [1, 2, 3, 4]:
            self.tree.insert(val)
            
    def tearDown(self):
        '''Perform cleanup actions'''
        
        pass
    
    def testTreeHeight(self):
        '''Verify the height of tree is 4'''
        
        self.assertEquals(self.tree.height(), 4)
        
    def testSearch(self):
        '''Test that BTNodes with values 4 (root), 3(internal node), and 1(leaf)
        can be retrieved by search method'''
        
        self.assertEquals(self.tree.search(4).value, 4)
        self.assertEquals(self.tree.search(3).value, 3)
        self.assertEquals(self.tree.search(1).value, 1)
        self.assertIsNone(self.tree.search(0))
        self.assertIsNone(self.tree.search(123))
        
    def testRange(self):
        '''Test range method accurately returns ordered nodes with values 
        within and inclusive of input range'''
        
        # same value, value in tree
        self.assertEquals(self.tree.range(2, 2)[0].value, 2)
        self.assertEquals(len(self.tree.range(2, 2)), 1)
        # different values, values in tree
        self.assertEquals(self.tree.range(1, 2)[0].value, 1)
        self.assertEquals(self.tree.range(1, 2)[1].value, 2)
        self.assertEquals(len(self.tree.range(1, 2)), 2)
        # neither value in tree
        self.assertEquals(len(self.tree.range(9, 10)), 0)
        # left value not in tree
        self.assertEquals(self.tree.range(0, 2)[0].value, 1)
        self.assertEquals(self.tree.range(0, 2)[1].value, 2)
        self.assertEquals(len(self.tree.range(0, 2)), 2)
        # right value not in tree
        self.assertEquals(self.tree.range(3, 10)[0].value, 3)
        self.assertEquals(self.tree.range(3, 10)[1].value, 4)
        self.assertEquals(len(self.tree.range(3, 10)), 2)
        
    def testNoneAndLeafDelete(self):
        '''Test delete method accurately deletes leaf node while leaving the
        rest of the tree untouched; and leaves whole tree untouched if 
        deleting non-existent node'''
        
        # deleting nonexistent node
        self.tree.delete(0)
        self.assertEquals(self.tree.root.value, 1)
        # deleting leaf node
        self.tree.delete(4)
        self.assertEquals(self.tree.root.value, 1)
        self.assertEquals(self.tree.root.right.value, 2)
        self.assertIsNone(self.tree.root.left)
        self.assertEquals(self.tree.height(), 3)

    def testRootDelete(self):
        '''Test delete method accurately deletes root node while maintaining
        BSTree properties'''

        self.tree.delete(1)
        self.assertEquals(self.tree.root.value, 2)
        self.assertEquals(self.tree.root.right.value, 3)
        self.assertIsNone(self.tree.root.left)
        self.assertEquals(self.tree.height(), 3)

    def testOneChildDelete(self):
        '''Test delete method accurately deletes node with one child while
        maintaining BSTree properties'''
        
        self.tree.delete(2)
        self.assertEquals(self.tree.root.value, 1)
        self.assertEquals(self.tree.root.right.value, 3)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right.left)
        self.assertEquals(self.tree.height(), 3)
        
        
class BSTreeGeneralTestCase(unittest.TestCase):
    '''Test BSTree methods for BSTree with more complexity of structure'''
    
    def setUp(self):
        '''Generate a tree to test.
                    10
                9
                    8
            7
        5
            3
                2
        '''

        self.tree = BSTree()
        for val in [5, 7, 3, 2, 9, 8, 10]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass
    
    def testTreeHeight(self):
        '''Verify the height of tree is 4'''
        
        self.assertEquals(self.tree.height(), 4)
        
    def testSearch(self):
        '''Test that all BTNodes in tree can be retrived by search method'''
        
        self.assertEquals(self.tree.search(5).value, 5)
        self.assertEquals(self.tree.search(3).value, 3)
        self.assertEquals(self.tree.search(2).value, 2)
        self.assertEquals(self.tree.search(7).value, 7)
        self.assertEquals(self.tree.search(9).value, 9)
        self.assertEquals(self.tree.search(8).value, 8)
        self.assertEquals(self.tree.search(10).value, 10)
        self.assertIsNone(self.tree.search(0))
        self.assertIsNone(self.tree.search(123))
        
    def testRange(self):
        '''Test range method accurately returns ordered nodes with values 
        within and inclusive of input range'''
        
        # same value, value in tree
        self.assertEquals(self.tree.range(2, 2)[0].value, 2)
        self.assertEquals(len(self.tree.range(2, 2)), 1)
        # different values, values in tree
        self.assertEquals(self.tree.range(2, 5)[0].value, 2)
        self.assertEquals(self.tree.range(2, 5)[1].value, 3)
        self.assertEquals(self.tree.range(2, 5)[2].value, 5)
        self.assertEquals(len(self.tree.range(2, 5)), 3)
        # neither value in tree
        self.assertEquals(len(self.tree.range(14, 20)), 0)
        # left value not in tree
        self.assertEquals(self.tree.range(0, 2)[0].value, 2)
        self.assertEquals(len(self.tree.range(0, 2)), 1)
        # right value not in tree
        self.assertEquals(self.tree.range(3, 11)[0].value, 3)
        self.assertEquals(self.tree.range(3, 11)[1].value, 5)
        self.assertEquals(self.tree.range(3, 11)[2].value, 7)
        self.assertEquals(self.tree.range(3, 11)[3].value, 8)
        self.assertEquals(self.tree.range(3, 11)[4].value, 9)
        self.assertEquals(self.tree.range(3, 11)[5].value, 10)
        self.assertEquals(len(self.tree.range(3, 11)), 6)
        
    def testNoneAndLeafDelete(self):
        '''Test delete method accurately deletes leaf node while leaving the
        rest of the tree untouched; and leaves whole tree untouched if 
        deleting non-existent node'''
        
        # deleting nonexistent node
        self.tree.delete(0)
        self.assertEquals(self.tree.root.value, 5)
        # deleting leaf node
        self.tree.delete(2)
        self.assertEquals(self.tree.root.value, 5)
        self.assertEquals(self.tree.root.left.value, 3)
        self.assertIsNone(self.tree.root.left.left)
        self.assertEquals(self.tree.height(), 4)
        
    def testRootAndTwoChildrenRightDelete(self):
        '''Test delete method accurately deletes node while maintaining BSTree 
        properties: for when a node is the root of the tree, when node has 
        two children with taller right child, and when its neighbour has one 
        child'''

        self.tree.delete(5)
        self.assertEquals(self.tree.root.value, 7)
        self.assertEquals(self.tree.root.right.value, 9)
        self.assertEquals(self.tree.root.left.value, 3)
        self.assertEquals(self.tree.root.left.left.value, 2)
        self.assertEquals(self.tree.root.right.left.value, 8)
        self.assertEquals(self.tree.root.right.right.value, 10)
        self.assertEquals(self.tree.height(), 3)
        
    def testOneChildDelete(self):
        '''Test delete method accurately deletes node with one child while
        maintaining BSTree properties'''
        
        self.tree.delete(7)
        self.assertEquals(self.tree.root.value, 5)
        self.assertEquals(self.tree.root.right.value, 9)
        self.assertEquals(self.tree.root.right.left.value, 8)
        self.assertEquals(self.tree.root.right.right.value, 10)
        self.assertEquals(self.tree.root.left.value, 3)
        self.assertEquals(self.tree.height(), 3)
        
    def testTwoChildrenEqualDelete(self):
        '''Test delete method accurately deletes node while maintaining BSTree 
        properties, when a node has two children with equal heights, and
        when the node's neighbour is a leaf node'''
        
        self.tree.delete(9)
        self.assertEquals(self.tree.root.value, 5)
        self.assertEquals(self.tree.root.right.value, 7)
        self.assertEquals(self.tree.root.right.right.value, 10)
        self.assertEquals(self.tree.root.right.right.left.value, 8)
        self.assertIsNone(self.tree.root.right.right.right)
        
    def testTwoChildrenLeftDelete(self):
        '''Test delete method accurately deletes node while maintaining BSTree 
        properties, when a node has two children with taller left child'''
        
        # increase height of subtree rooted at 5
        self.tree.insert(1)
        self.tree.insert(0)
        # height of left subtree rooted at 5: 4
        # height of right subtree rooted at 5: 3
        self.tree.delete(5)
        self.assertEquals(self.tree.root.value, 3)
        self.assertEquals(self.tree.root.right.value, 7)
        self.assertEquals(self.tree.root.left.value, 2)
        self.assertEquals(self.tree.height(), 4)


def sample_suite():
    """Return the sample test suite."""

    return unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)

def btnode_suite():
    '''Return the BTNode test suite'''
    
    return unittest.TestLoader().loadTestsFromTestCase(BTNodeTestCase)

def bstree_empty_suite():
    '''Return the empty BSTree test suite'''
    
    return unittest.TestLoader().loadTestsFromTestCase(BSTreeEmptyTestCase)

def bstree_single_suite():
    '''Return the one-node BSTree test suite'''
    
    return unittest.TestLoader().loadTestsFromTestCase(BSTreeSingleTestCase)

def bstree_left_suite():
    '''Return the left-children-only BSTree test suite'''
    
    return unittest.TestLoader().loadTestsFromTestCase(BSTreeLeftTestCase)

def bstree_right_suite():
    '''Return the right-children-only BSTree test suite'''
    
    return unittest.TestLoader().loadTestsFromTestCase(BSTreeRightTestCase)

def bstree_general_suite():
    '''Return the general BSTree test suite'''
    
    return unittest.TestLoader().loadTestsFromTestCase(BSTreeGeneralTestCase)


if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(sample_suite())
    runner.run(btnode_suite())
    runner.run(bstree_empty_suite())
    runner.run(bstree_single_suite())
    runner.run(bstree_left_suite())
    runner.run(bstree_right_suite())
    runner.run(bstree_general_suite())
