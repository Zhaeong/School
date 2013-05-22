import unittest
from operand import *
from myqueue import *
from stack import *

class SimpleTestCase(unittest.TestCase):
    '''Test values in several bases.'''
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
            
    def testBin(self):
        """1101b2 == 13"""

        self.assertEqual(Operand("1101b2").value(), 13)
            
    def testDec(self):
        """1054 == 1054"""

        self.assertEqual(Operand("1054").value(), 1054)

    def testHept(self):
        """563b7 == 290"""

        self.assertEqual(Operand("563b7").value(), 290)

    def testHex(self):
        """ABb16 == 171"""

        self.assertEqual(Operand("ABb16").value(), 171)


class ExceptionTestCase(unittest.TestCase):
    '''Test with Operands that should raise exceptions.'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def trytwo(self, astring):
        a = Operand(astring)
        return a.value()
        
    def testNonDecimal(self):
        """hello  -> raise InvalidNumeralStringError
        Non-decimal string that does not contain 'b'"""
        try:
            Operand("hello").value()
            self.fail()
        except InvalidNumeralStringError:
            pass

    def testHighBase(self):
        """41b24  -> raise InvalidNumeralStringError
        Base is above 16."""
        try:
            Operand("41b24").value()
            self.fail()
        except InvalidNumeralStringError:
            pass


    def testLowBase(self):
        """11b1  -> raise InvalidNumeralStringError
        Base is below 2"""

        try:
            Operand("11b1").value()
            self.fail()
        except InvalidNumeralStringError:
            pass

    def testLargeDigit(self):
        """1113b2  -> raise InvalidNumeralStringError
        Digit too large for the base present in digit substring"""

        try:
            Operand("1113b2").value()
            self.fail()
        except InvalidNumeralStringError:
            pass

    def testNonDigit(self):
        """342Xb16  -> raise InvalidNumeralStringError
        Non-digit present in digit substring"""

        try:
            Operand("342Xb16").value()
            self.fail()
        except InvalidNumeralStringError:
            pass
            

    def testNonBase(self):
        """342bqq  -> raise InvalidNumeralStringError
        Non-decimal base specified"""

        try:
            Operand("342bqq").value()
            self.fail()
        except InvalidNumeralStringError:
            pass

def simple_suite():
    """Return the simple test suite for the Operand class."""

    return unittest.TestLoader().loadTestsFromTestCase(SimpleTestCase)

def except_suite():
    """Return the exception-raising test suite for the Operand class."""

    return unittest.TestLoader().loadTestsFromTestCase(ExceptionTestCase)


    
if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(simple_suite())
    runner.run(except_suite())