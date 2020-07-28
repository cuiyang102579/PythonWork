import unittest

from example.ddtExcelTest import Testwork

CaseNames = unittest.TestLoader().getTestCaseNames(Testwork)
suiteTest = unittest.TestSuite()
L = ['test6']
suiteTest.addTests([Testwork("{0}".format(x)) for i in L for x in CaseNames if i == x[:len(i)]])
runner = unittest.TextTestRunner()
runner.run(suiteTest)


# unittest.main();