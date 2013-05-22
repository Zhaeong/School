import unittest
from solver import *
from myqueue import *
from stack import *

class DecimalTestCase(unittest.TestCase):
    '''Test simple panda code with decimal numbers.'''
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
            
    def testVal(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/01val.pnd").value(), 6)
            
    def testAdd(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/02add.pnd").value(), 11)

    def testDivide(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/03div.pnd").value(), 8)

    def testIntDivide(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/04intdiv.pnd").value(), 5)

    def testOrderOps(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/05orderops.pnd").value(), 23)

    def testParens(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/06parens.pnd").value(), 35)

class OperandTestCase(unittest.TestCase):
    '''Test simple panda code with arbitrary base numbers.'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVal(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/11val.pnd").value(), 14)

    def testMix(self):
        """test a mix of values"""

        self.assertEqual(Solver("pandatests/12mix.pnd").value(), 194)

class VariableTestCase(unittest.TestCase):
    '''Test simple panda code with arbitrary base numbers.'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSimpleAssign(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/21assign.pnd").value(), 8)

    def testSimpleBaseAssign(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/22baseassign.pnd").value(), 17)

    def testLongVar(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/23longvar.pnd").value(), 43)

    def testVarInExpr(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/24varinexpr.pnd").value(), 3)

    def testMultiVar(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/25multivar.pnd").value(), 22)

    def testMultiVarAssign(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/26multivarassign.pnd").value(), 7)

    def testMutualVarAssign(self):
        """test a single value"""

        self.assertEqual(Solver("pandatests/27mutualvarassign.pnd").value(), 3)

    def testNameNotFound(self):
        """test a single value"""

        self.assertRaises(NameNotFoundException, Solver("pandatests/28namenotfound.pnd").value)

class SyntaxTestCase(unittest.TestCase):
    '''Test simple panda code with arbitrary base numbers.'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOddBegin(self):
        """test a single value"""

        try:
            Solver("pandatests/31oddbegin.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "haha")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

    def testVarAfterReturn(self):
        """test a single value"""
        try:
            Solver("pandatests/32varafterreturn.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "var")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

        

    def testEndNotLastLine(self):
        """test a single value"""

        try:
            Solver("pandatests/33endnotlastline.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "notend")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

    def testReturnNotSecondLastLine(self):
        """test a single value"""

        try:
            Solver("pandatests/34returnnotsecondlastline.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "something")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")


    def testSomethingAfterEnd(self):
        """test a single value"""
        try:
            Solver("pandatests/35somethingafterend.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "haha")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

    def testMultipleTokensAfterEnd(self):
        """test a single value"""
        try:
            Solver("pandatests/36thingsafterend.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "haha")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

    def testNotEqualSign(self):
        """test a single value"""
        try:
            Solver("pandatests/37notequalsign.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "=")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

    def testVarNameKeyword(self):
        """test a single value"""
        try:
            Solver("pandatests/38varnamekeyword.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "var")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")

    def testVarNameUppercase(self):
        """test a single value"""
        try:
            Solver("pandatests/39varnameupper.pnd").value()
        except SyntaxException as se:
            self.assertEqual(se.token, "X")
        except Exception as e:
            self.fail("Non-SyntaxException raised! {}".format(e))
        else:
            self.fail("No exception raised!")


class ExpressionTestCase(unittest.TestCase):
    '''Test simple panda code with arbitrary base numbers.'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTooManyOperands(self):
        """test a single value"""
        
        self.assertRaises(InvalidExpressionException, Solver("pandatests/41toomanyoperands.pnd").value)

    def testTooManyOperators(self):
        """test a single value"""

        self.assertRaises(InvalidExpressionException, Solver("pandatests/42toomanyoperators.pnd").value)

def simple_suite():
    """Return a test suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(DecimalTestCase)

def operand_suite():
    """Return a test suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(OperandTestCase)

def variable_suite():
    """Return a test suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(VariableTestCase)

def syntax_suite():
    """Return a test suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(SyntaxTestCase)
    
def expr_suite():
    """Return a test suite for the Shunting Yard algorithm."""

    return unittest.TestLoader().loadTestsFromTestCase(ExpressionTestCase)

if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(simple_suite())
    runner.run(operand_suite())
    runner.run(variable_suite())
    runner.run(syntax_suite())
    runner.run(expr_suite())