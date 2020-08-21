import readConfig as readConfig
from common import configHttpC
import unittest
import json
from common.Log import Log

localReadConfig = readConfig.ReadConfig()
url = localReadConfig.get_tools("logisticsUpload")
log = Log()

class tools(unittest.TestCase):
    ''' 河姆渡面单上传工具'''
    def test_tools(self):
        ''' 面单上传-单张上传'''
        headers = {'Content-Type': 'application/json'}
        data = [ {
                    "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg",
                    "expressNumber": "8888"}]
        run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
        # print(run.response)
        respCode=run.response['respCode']
        if respCode != '0000':
            log.error(run.response)
        self.assertEqual("0000",respCode)

    def test_tools2(self):
        ''' 面单上传-多张上传 '''
        headers = {'Content-Type': 'application/json'}
        data = [{
            "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_M站.jpg",
            "expressNumber": "8888"}, {
            "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg",
            "expressNumber": "8888"}]
        run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
        # print(run.response)
        respCode = run.response['respCode']
        if respCode != '0000':
            log.error(run.response)
        self.assertEqual("0000", respCode)


if __name__=="__main__":
    unittest.main();
