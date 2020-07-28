import unittest,os
import xlrd
from ddt import ddt,data,unpack,file_data
import rootPath
from common.StringUtils import readExcel

report_dirc = os.path.join(rootPath.root_dirc, "testdata/test.xlsx")


@ddt
class Testwork(unittest.TestCase):

    # 元组数据

    # @data(1,2,3)
    # def test(self,value):
    #     print(value)
    #
    # @data((1,2,3),(1,2,3))
    # def test2(self,value):
    #     print(value)
    #
    # @data((1,2,3),(1,2,3))
    # # 拆分数据
    # @unpack
    # def test3(self,value1,value2,value3):
    #     print(str(value1)+"  "+str(value2)+"  "+str(value3))

    # 列表数据
    # @data([{'name':'lili','age':12},{'sex':'male','job':'teacher'}])
    # @unpack
    # def test4(self,value,v2):
    #     print("####")
    #     print(value)

    # @data({'name':'lili','age':'12'},{'name':'lilei','age':'30'})
    # @unpack
    # def test5(self,name,age):
    #     print(name,age)
    #     print(1)

    @data(*readExcel(report_dirc))
    @unpack
    def test6(self,name,age,url):
        print(name+" "+str(age)+"  "+url)

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Testwork("test6"))
    return suiteTest

if __name__ == "__main__":
    unittest.main();


