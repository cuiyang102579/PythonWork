import unittest
# from demo import RunMain
# import HtmlTestRunner


class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDown(self):
        print("类执行之后的方法")

    def setUp(self):
        print("每次方法之前执行setup")

    def test_01(self):
        print("test_01")
        self.assertEqual("1","1")

    def test_02(self):
        print("test_02")
        self.assertEqual("2","2")

    def tearDown(self):
        print("每次方法之后执行teardown")

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_02"))
    unittest.TextTestRunner().run(suite)