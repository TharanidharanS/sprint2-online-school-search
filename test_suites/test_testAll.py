import unittest
from package1.test_test1 import test1_Test
from package2.test_test2 import test2_Test
from package3.test_test3 import test3_Test

# Load all test Cases
testCase1=unittest.TestLoader().loadTestsFromTestCase(test1_Test)
testCase2=unittest.TestLoader().loadTestsFromTestCase(test2_Test)
testCase3=unittest.TestLoader().loadTestsFromTestCase(test3_Test)


# Creating Test Suit
testSuites01=unittest.TestSuite([testCase1,testCase2,testCase3])
#testSuites02=unittest.TestSuite([testCase2])

unittest.TextTestRunner().run(testSuites01)

