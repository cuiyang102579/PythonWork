import readConfig as readConfig
from common import configHttpC
import unittest
import json
localReadConfig = readConfig.ReadConfig()


class tools(unittest.TestCase):

    def test_tools(self):
        url = localReadConfig.get_tools("logisticsUpload")
        headers = {'Content-Type': 'application/json'}
        data = [{
                    "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_M站.jpg",
                    "expressNumber": "8888"}, {
                    "imageUrl": "https://project-homedo.oss-cn-shanghai.aliyuncs.com/3f75f6aa-69a1-4adf-be65-b86e96337aa4_上传业务免单活动.jpg",
                    "expressNumber": "8888"}]
        # run = configHttpC.ConfigHttpC(url, params=None, data=json.dumps(data), headers=headers, method='POST')
        # print(run.response)
        self.assertEqual("1","2")



