import unittest
from shunting_yard import *
from myqueue import *
from stack import *

class SimpleTestCase(unittest.TestCase):
    '''Test behaviour of a simple expression 
    (no harder than two operands and an operator).'''
    
    def setUp(self):
        self.testQueue = Queue()
        
    def tearDown(self):
        pass
            
    def testSingleDigit(self):
        """6"""
        self.testQueue.enqueue("6")
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), "6")
        self.assertTrue(outQueue.is_empty())

    def testDoubleDigitStr(self):
        """12 (str)"""
        self.testQueue.enqueue("12")
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), "12")
        self.assertTrue(outQueue.is_empty())

    def testDoubleDigitInt(self):
        """12 (int)"""
        self.testQueue.enqueue(12)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 12)
        self.assertTrue(outQueue.is_empty())

    def testLowPriority(self):
        """4 + 5  ->  4 5 +"""
        self.testQueue.enqueue(4)
        self.testQueue.enqueue("+")
        self.testQueue.enqueue(5)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 4)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), "+")
        self.assertTrue(outQueue.is_empty())

    def testHighPriority(self):
        """8 / 4  ->  8 4 /"""
        self.testQueue.enqueue(8)
        self.testQueue.enqueue("/")
        self.testQueue.enqueue(4)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 4)
        self.assertEqual(outQueue.dequeue(), "/")
        self.assertTrue(outQueue.is_empty())



class OrderParenTestCase(unittest.TestCase):
    '''Test behaviour of expressions where
    order of operations and parentheses might be present.'''

    def setUp(self):
        self.testQueue = Queue()

    def tearDown(self):
        pass

    def testPlusTimes(self):
        """8 + 5 * 3  ->  8 5 3 * +"""

        for e in [8, "+", 5, "*", 3]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertEqual(outQueue.dequeue(), "+")
        self.assertTrue(outQueue.is_empty())

    def testDivideTimes(self):
        """8 / 5 * 3  ->  8 5 / 3 *"""

        for e in [8, "/", 5, "*", 3]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), "/")
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertTrue(outQueue.is_empty())


    def testPlusMinus(self):
        """8 + 5 - 3  ->  8 5 + 3 -"""

        for e in [8, "+", 5, "-", 3]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), "+")
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "-")
        self.assertTrue(outQueue.is_empty())

    def testParenPlus(self):
        """( 8 + 5 ) * 3  ->  8 5 + 3 *"""

        for e in ["(", 8, "+", 5, ")", "*", 3]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), "+")
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertTrue(outQueue.is_empty())

    def testParenTimes(self):
        """8 + ( 5 * 3 )  ->  8 5 3 * +"""

        for e in [8, "+", "(", 5, "*", 3, ")"]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertEqual(outQueue.dequeue(), "+")
        self.assertTrue(outQueue.is_empty())

    def testNestedParens(self):
        """( ( 5 * 3 ) )  ->  5 3 *"""

        for e in ["(", "(", 5, "*", 3, ")" , ")"]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertTrue(outQueue.is_empty())

    def testManyTimes(self):
        """8 + 5 * 3 * 4  ->  8 5 3 * 4 * +"""

        for e in [8, "+", 5, "*", 3, "*" , 4]:
            self.testQueue.enqueue(e)
        outQueue = convert_to_postfix(self.testQueue)
        self.assertEqual(outQueue.dequeue(), 8)
        self.assertEqual(outQueue.dequeue(), 5)
        self.assertEqual(outQueue.dequeue(), 3)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertEqual(outQueue.dequeue(), 4)
        self.assertEqual(outQueue.dequeue(), "*")
        self.assertEqual(outQueue.dequeue(), "+")
        self.assertTrue(outQueue.is_empty())


class ExceptionTestCase(unittest.TestCase):
    '''Test behaviour of expressions with
    mismatched parentheses.'''

    def setUp(self):
        self.testQueue = Queue()

    def tearDown(self):
        pass

    def testMismatchedOpen(self):
        """( 8 + 5  -> raise ParenMismatchException"""

        for e in ["(", 8, "+", 5]:
            self.testQueue.enqueue(e)
        self.assertRaises(ParenMismatchException, convert_to_postfix, self.testQueue)

    def testMismatchedClose(self):
        """8 + 5 )  -> raise ParenMismatchException"""

        for e in [8, "+", 5, "("]:
            self.testQueue.enqueue(e)
        self.assertRaises(ParenMismatchException, convert_to_postfix, self.testQueue)


def simple_suite():
    """Return the simple suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(SimpleTestCase)

def paren_suite():
    """Return the parenthesis suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(OrderParenTestCase)

def except_suite():
    """Return the exception suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(ExceptionTestCase)

    
if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(simple_suite())
    runner.run(paren_suite())
    runner.run(except_suite())